import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from pipeline.cognee_client import _dataset_field, _filter_hits_for_dataset, forget


class DatasetFilterTests(unittest.TestCase):
    def test_dataset_field_supports_cognee_model_objects(self) -> None:
        class DatasetRecord:
            id = "dataset-id"
            name = "wikipedia_2017"

        self.assertEqual(_dataset_field(DatasetRecord(), "name"), "wikipedia_2017")
        self.assertEqual(_dataset_field(DatasetRecord(), "id"), "dataset-id")

    def test_keeps_hit_whose_document_id_is_dataset_member(self) -> None:
        hit = {"document_id": "ABC", "document_name": "text_x", "text": "body"}
        self.assertEqual(
            _filter_hits_for_dataset([hit], "eve_memory", allowed_ids={"abc"}),
            [hit],
        )

    def test_keeps_nested_payload_and_stamped_dataset_marker(self) -> None:
        hit = {"payload": {"text": "dataset: eve_memory\nunique fact"}}
        self.assertEqual(_filter_hits_for_dataset([hit], "eve_memory"), [hit])

    def test_keeps_curated_fuel_marker(self) -> None:
        hit = {"text": "fuel: curated_primitives\nFriction & Flow"}
        self.assertEqual(_filter_hits_for_dataset([hit], "primitives_test"), [hit])

    def test_rejects_prefixed_dataset_marker(self) -> None:
        hit = {"text": "dataset: eve_memory_archive\nother corpus"}
        self.assertEqual(_filter_hits_for_dataset([hit], "eve_memory"), [])

    def test_keeps_hit_by_allowed_name_case_insensitive(self) -> None:
        hit = {"document_name": "TEXT_Foo", "document_id": "x", "text": "body"}
        self.assertEqual(
            _filter_hits_for_dataset([hit], "eve_memory", allowed_names={"text_foo"}),
            [hit],
        )

    def test_keeps_nested_payload_document_id(self) -> None:
        hit = {"payload": {"document_id": "1B41DC7C-1FDC", "text": "chunk body"}}
        self.assertEqual(
            _filter_hits_for_dataset(
                [hit],
                "primitives_test",
                allowed_ids={"1b41dc7c-1fdc-581b-b88b-5604187fcb4a"},
            ),
            [hit],
        )

    def test_rejects_non_uuid_id_prefix_false_positive(self) -> None:
        hit = {"document_id": "abc", "document_name": "text_x", "text": "body"}
        self.assertEqual(
            _filter_hits_for_dataset(
                [hit],
                "eve_memory",
                allowed_ids={"abcdef-1234-5678-90ab-cdef12345678"},
            ),
            [],
        )

    def test_dataset_marker_is_case_insensitive(self) -> None:
        hit = {"text": "dataset: EVE_MEMORY\nfact"}
        self.assertEqual(_filter_hits_for_dataset([hit], "eve_memory"), [hit])

    def test_curated_selector_is_case_insensitive(self) -> None:
        hit = {"text": "fuel: Curated_Primitives\nFriction & Flow"}
        self.assertEqual(_filter_hits_for_dataset([hit], "PRIMITIVES_TEST"), [hit])


class ForgetDatasetTests(unittest.IsolatedAsyncioTestCase):
    async def test_forget_removes_dataset_record_and_confirms_absence(self) -> None:
        target = SimpleNamespace(id="dataset-id", name="eve_verify_123")
        datasets = SimpleNamespace(
            list_datasets=AsyncMock(side_effect=[[target], []]),
            empty_dataset=AsyncMock(),
        )
        cognee = SimpleNamespace(datasets=datasets)

        async def run_direct(operation):
            return await operation()

        with (
            patch("pipeline.cognee_client._cognee_module", return_value=cognee),
            patch("pipeline.cognee_client.run_with_cognee_lock", side_effect=run_direct),
        ):
            removed = await forget("eve_verify_123")

        self.assertTrue(removed)
        datasets.empty_dataset.assert_awaited_once_with(dataset_id="dataset-id")
        self.assertEqual(datasets.list_datasets.await_count, 2)


if __name__ == "__main__":
    unittest.main()
