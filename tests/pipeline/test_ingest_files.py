import asyncio
import json
import os
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import AsyncMock, Mock, patch

from pipeline.ingest_files import (
    MAX_BATCH_FILES,
    MAX_FILE_BYTES,
    MemoryConversionError,
    _merge_content_index,
    convert_pdf,
    ingest_files,
    ingest_files_async,
    prepare_document,
    validate_dataset,
    validate_memory_file,
)


class IngestFilesValidationTests(unittest.TestCase):
    def test_dataset_accepts_safe_name(self) -> None:
        self.assertEqual(validate_dataset("eve_memory-2"), "eve_memory-2")

    def test_dataset_accepts_boundary_length(self) -> None:
        name = "a" * 64
        self.assertEqual(validate_dataset(name), name)

    def test_dataset_rejects_unsafe_names(self) -> None:
        for name in ("", "../memory", "two words", "a" * 65, "memory.name", " memory"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate_dataset(name)

    def test_directive_filenames_are_rejected_case_insensitively(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            for filename in ("SYSTEM.md", "system.MD", "LENS_RULES.txt", "lens_notes.PDF"):
                path = Path(tmp) / filename
                path.write_bytes(b"content")
                with self.subTest(filename=filename), self.assertRaises(ValueError):
                    validate_memory_file(path)

    def test_directives_path_component_is_rejected_case_insensitively(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "DiReCtIvEs" / "notes.md"
            path.parent.mkdir()
            path.write_text("content", encoding="utf-8")
            with self.assertRaises(ValueError):
                validate_memory_file(path)

    def test_supported_file_types_are_accepted_case_insensitively(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            for filename in ("notes.md", "notes.TXT", "paper.Pdf"):
                path = Path(tmp) / filename
                path.write_bytes(b"content")
                with self.subTest(filename=filename):
                    self.assertEqual(validate_memory_file(path), path)

    def test_unsupported_file_type_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "notes.docx"
            path.write_bytes(b"content")
            with self.assertRaises(ValueError):
                validate_memory_file(path)

    def test_empty_file_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "notes.txt"
            path.touch()
            with self.assertRaises(ValueError):
                validate_memory_file(path)

    def test_missing_path_and_directory_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(ValueError):
                validate_memory_file(root / "missing.md")
            directory = root / "folder.md"
            directory.mkdir()
            with self.assertRaises(ValueError):
                validate_memory_file(directory)

    def test_file_over_size_limit_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "large.txt"
            with path.open("wb") as stream:
                stream.truncate(MAX_FILE_BYTES + 1)
            with self.assertRaises(ValueError):
                validate_memory_file(path)


class PreparedDocumentTests(unittest.TestCase):
    def test_prepared_text_has_traceable_header_and_hash(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "notes.txt"
            path.write_text("unique fact", encoding="utf-8")
            doc = prepare_document(path, "eve_memory", "job-1")

        self.assertEqual(doc.source_path, path)
        self.assertIn("source_file: notes.txt", doc.content)
        self.assertIn("dataset: eve_memory", doc.content)
        self.assertIn("upload_job_id: job-1", doc.content)
        self.assertIn(f"content_hash: {doc.content_hash}", doc.content)
        self.assertTrue(doc.content.endswith("unique fact"))
        self.assertEqual(len(doc.content_hash), 64)

    def test_prepare_document_validates_dataset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "notes.txt"
            path.write_text("content", encoding="utf-8")
            with self.assertRaises(ValueError):
                prepare_document(path, "../unsafe", "job-1")

    def test_prepare_pdf_uses_converted_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "paper.pdf"
            path.write_bytes(b"%PDF-local")
            converted = Path(tmp) / "converted.md"
            converted.write_text("# Extracted\n\nPDF fact", encoding="utf-8")
            with patch("pipeline.ingest_files.convert_pdf", return_value=converted) as converter:
                doc = prepare_document(path, "eve_memory", "job-2")

        converter.assert_called_once()
        self.assertTrue(doc.content.endswith("# Extracted\n\nPDF fact"))


class PdfConversionTests(unittest.TestCase):
    def test_convert_pdf_writes_local_docling_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "paper.pdf"
            source.write_bytes(b"%PDF-local")
            output = root / "out"
            document = Mock()
            document.export_to_markdown.return_value = "# Local result"
            conversion = Mock(document=document)
            converter = Mock()
            converter.convert.return_value = conversion

            with patch("pipeline.ingest_files.DocumentConverter", return_value=converter):
                result = convert_pdf(source, output)

            self.assertEqual(result, output / "paper.md")
            self.assertEqual(result.read_text(encoding="utf-8"), "# Local result")
            converter.convert.assert_called_once_with(source)

    def test_convert_pdf_rejects_empty_conversion(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "paper.pdf"
            source.write_bytes(b"%PDF-local")
            document = Mock()
            document.export_to_markdown.return_value = " \n"
            converter = Mock()
            converter.convert.return_value = Mock(document=document)

            with patch("pipeline.ingest_files.DocumentConverter", return_value=converter):
                with self.assertRaisesRegex(MemoryConversionError, "no text"):
                    convert_pdf(source, root / "out")

    def test_convert_pdf_wraps_docling_errors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "paper.pdf"
            source.write_bytes(b"%PDF-local")
            converter = Mock()
            converter.convert.side_effect = RuntimeError("model failure")

            with patch("pipeline.ingest_files.DocumentConverter", return_value=converter):
                with self.assertRaisesRegex(MemoryConversionError, "paper.pdf"):
                    convert_pdf(source, root / "out")


class BatchIngestionTests(unittest.IsolatedAsyncioTestCase):
    def _write(self, root: Path, name: str, content: str) -> Path:
        path = root / name
        path.write_text(content, encoding="utf-8")
        return path

    async def test_rejects_empty_and_oversized_batches_before_adapter_calls(self) -> None:
        with patch("pipeline.ingest_files.remember_many", new_callable=AsyncMock) as remember:
            with self.assertRaises(ValueError):
                await ingest_files_async([], "eve_memory", "job-1")
            remember.assert_not_awaited()

        paths = [Path(f"file-{index}.txt") for index in range(MAX_BATCH_FILES + 1)]
        with patch("pipeline.ingest_files.remember_many", new_callable=AsyncMock) as remember:
            with self.assertRaises(ValueError):
                await ingest_files_async(paths, "eve_memory", "job-1")
            remember.assert_not_awaited()

    async def test_fast_batch_remembers_then_embeds_without_cognify(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            local_app_data = root / "state"
            paths = [self._write(root, "one.md", "first"), self._write(root, "two.txt", "second")]
            events: list[str] = []

            async def remember(contents: list[str], dataset: str, mode: str) -> None:
                self.assertEqual(len(contents), 2)
                self.assertEqual((dataset, mode), ("eve_memory", "fast"))
                events.append("remember")

            async def embed(dataset: str) -> None:
                self.assertEqual(dataset, "eve_memory")
                events.append("embed")

            with (
                patch.dict(os.environ, {"LOCALAPPDATA": str(local_app_data)}),
                patch("pipeline.ingest_files.remember_many", side_effect=remember),
                patch("pipeline.ingest_files.embed_dataset", side_effect=embed),
                patch("pipeline.ingest_files.cognify_dataset", new_callable=AsyncMock) as cognify,
            ):
                result = await ingest_files_async(paths, "eve_memory", "job-1")

            self.assertEqual(events, ["remember", "embed"])
            cognify.assert_not_awaited()
            self.assertEqual(result["dataset"], "eve_memory")
            self.assertEqual(result["files"], ["one.md", "two.txt"])
            self.assertEqual(result["documents"], 2)
            self.assertEqual(result["skipped"], [])
            self.assertEqual(len(result["hashes"]), 2)

    async def test_full_graph_runs_only_after_embedding(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self._write(root, "one.md", "first")
            events: list[str] = []

            async def remember(contents: list[str], dataset: str, mode: str) -> None:
                events.append("remember")

            async def embed(dataset: str) -> None:
                events.append("embed")

            async def cognify(dataset: str) -> None:
                events.append("cognify")

            with (
                patch.dict(os.environ, {"LOCALAPPDATA": str(root / "state")}),
                patch("pipeline.ingest_files.remember_many", side_effect=remember),
                patch("pipeline.ingest_files.embed_dataset", side_effect=embed),
                patch("pipeline.ingest_files.cognify_dataset", side_effect=cognify),
            ):
                await ingest_files_async([path], "eve_memory", "job-1", full_graph=True)

            self.assertEqual(events, ["remember", "embed", "cognify"])

    async def test_hash_is_recorded_only_after_successful_embedding(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            local_app_data = root / "state"
            path = self._write(root, "one.md", "same content")
            index_path = local_app_data / "EMPIRE" / "memory-jobs" / "content-index.json"

            with (
                patch.dict(os.environ, {"LOCALAPPDATA": str(local_app_data)}),
                patch("pipeline.ingest_files.remember_many", new_callable=AsyncMock),
                patch(
                    "pipeline.ingest_files.embed_dataset",
                    new_callable=AsyncMock,
                    side_effect=RuntimeError("embedding failed"),
                ),
            ):
                with self.assertRaisesRegex(RuntimeError, "embedding failed"):
                    await ingest_files_async([path], "eve_memory", "job-1")

            self.assertFalse(index_path.exists())

            with (
                patch.dict(os.environ, {"LOCALAPPDATA": str(local_app_data)}),
                patch("pipeline.ingest_files.remember_many", new_callable=AsyncMock) as remember,
                patch("pipeline.ingest_files.embed_dataset", new_callable=AsyncMock),
            ):
                result = await ingest_files_async([path], "eve_memory", "job-2")

            remember.assert_awaited_once()
            self.assertEqual(result["documents"], 1)
            self.assertEqual(result["skipped"], [])
            index = json.loads(index_path.read_text(encoding="utf-8"))
            self.assertIn(f"eve_memory:{result['hashes'][0]}", index)

    async def test_successful_content_is_skipped_for_same_dataset_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            local_app_data = root / "state"
            path = self._write(root, "one.md", "same content")

            with (
                patch.dict(os.environ, {"LOCALAPPDATA": str(local_app_data)}),
                patch("pipeline.ingest_files.remember_many", new_callable=AsyncMock),
                patch("pipeline.ingest_files.embed_dataset", new_callable=AsyncMock),
            ):
                await ingest_files_async([path], "eve_memory", "job-1")

            with (
                patch.dict(os.environ, {"LOCALAPPDATA": str(local_app_data)}),
                patch("pipeline.ingest_files.remember_many", new_callable=AsyncMock) as remember,
                patch("pipeline.ingest_files.embed_dataset", new_callable=AsyncMock) as embed,
            ):
                skipped = await ingest_files_async([path], "eve_memory", "job-2")

            remember.assert_not_awaited()
            embed.assert_not_awaited()
            self.assertEqual(skipped["documents"], 0)
            self.assertEqual(skipped["files"], [])
            self.assertEqual(skipped["skipped"], ["one.md"])

            with (
                patch.dict(os.environ, {"LOCALAPPDATA": str(local_app_data)}),
                patch("pipeline.ingest_files.remember_many", new_callable=AsyncMock) as remember,
                patch("pipeline.ingest_files.embed_dataset", new_callable=AsyncMock),
            ):
                await ingest_files_async([path], "other_dataset", "job-3")
            remember.assert_awaited_once()

    async def test_concurrent_ingests_preserve_both_index_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            local_app_data = root / "state"
            first = self._write(root, "one.md", "first concurrent content")
            second = self._write(root, "two.md", "second concurrent content")
            both_embedding = asyncio.Event()
            embed_calls = 0

            async def embed(dataset: str) -> None:
                nonlocal embed_calls
                embed_calls += 1
                if embed_calls == 2:
                    both_embedding.set()
                await both_embedding.wait()

            with (
                patch.dict(os.environ, {"LOCALAPPDATA": str(local_app_data)}),
                patch("pipeline.ingest_files.remember_many", new_callable=AsyncMock),
                patch("pipeline.ingest_files.embed_dataset", side_effect=embed),
            ):
                results = await asyncio.gather(
                    ingest_files_async([first], "eve_memory", "job-1"),
                    ingest_files_async([second], "eve_memory", "job-2"),
                )

            index_path = local_app_data / "EMPIRE" / "memory-jobs" / "content-index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            expected_keys = {
                f"eve_memory:{result['hashes'][0]}"
                for result in results
            }
            self.assertEqual(set(index), expected_keys)

    async def test_full_graph_failure_is_retried_without_reembedding(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self._write(root, "one.md", "graph retry content")

            with (
                patch.dict(os.environ, {"LOCALAPPDATA": str(root / "state")}),
                patch("pipeline.ingest_files.remember_many", new_callable=AsyncMock) as remember,
                patch("pipeline.ingest_files.embed_dataset", new_callable=AsyncMock) as embed,
                patch(
                    "pipeline.ingest_files.cognify_dataset",
                    new_callable=AsyncMock,
                    side_effect=[RuntimeError("graph failed"), None],
                ) as cognify,
            ):
                with self.assertRaisesRegex(RuntimeError, "graph failed"):
                    await ingest_files_async([path], "eve_memory", "job-1", full_graph=True)
                result = await ingest_files_async(
                    [path],
                    "eve_memory",
                    "job-2",
                    full_graph=True,
                )

            remember.assert_awaited_once()
            embed.assert_awaited_once()
            self.assertEqual(cognify.await_count, 2)
            self.assertEqual(result["documents"], 0)
            self.assertEqual(result["skipped"], ["one.md"])


class ContentIndexPersistenceTests(unittest.TestCase):
    def test_concurrent_merges_preserve_entries_and_use_distinct_temporary_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            index_path = Path(tmp) / "content-index.json"
            temporary_paths: list[Path] = []
            original_write_text = Path.write_text

            def record_temporary_path(path: Path, *args: object, **kwargs: object) -> int:
                written = original_write_text(path, *args, **kwargs)
                if path.suffix == ".tmp":
                    temporary_paths.append(path)
                return written

            with (
                patch.object(Path, "write_text", record_temporary_path),
                ThreadPoolExecutor(max_workers=2) as executor,
            ):
                futures = [
                    executor.submit(_merge_content_index, index_path, {f"key-{index}": True})
                    for index in range(2)
                ]
                for future in futures:
                    future.result(timeout=10)
            self.assertEqual(
                json.loads(index_path.read_text(encoding="utf-8")),
                {"key-0": True, "key-1": True},
            )
            self.assertEqual(len(set(temporary_paths)), 2)


class SyncWrapperTests(unittest.TestCase):
    def test_sync_wrapper_runs_async_ingestion(self) -> None:
        expected = {"dataset": "eve_memory", "documents": 0}
        with patch("pipeline.ingest_files.ingest_files_async", new_callable=AsyncMock, return_value=expected):
            result = ingest_files([], "eve_memory", "job-1", False)
        self.assertEqual(result, expected)

    def test_maximum_batch_constant_matches_global_constraint(self) -> None:
        self.assertEqual(MAX_BATCH_FILES, 20)


if __name__ == "__main__":
    unittest.main()
