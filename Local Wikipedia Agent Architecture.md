# **Architecting Offline Encyclopedic Agents: Advanced Topologies for Local Wikipedia Integration**

The deployment of massive, encyclopedic datasets—such as a complete 2026 Wikipedia snapshot—within local, resource-constrained agentic frameworks presents formidable architectural challenges. When attempting to embed the entirety of Wikipedia into a dense vector database like Weaviate, the underlying assumption is that semantic similarity serves as an effective mechanism for entity resolution. In practice, this approach frequently results in systemic failures1. Dense retrieval systems naturally optimize for spatial embedding proximity rather than absolute ontological existence, which leads directly to false-positive entity matches1. A prime example of this failure mode occurs when a model confuses a highly specific television series, such as *The Following*, with the generalized abstract concept of a "Cult following" merely because they share lexical and spatial characteristics1.

When an autonomous agent queries a local encyclopedic resource, the fundamental requirement is not general semantic proximity, but exact entity resolution, deterministic multi-hop contextual synthesis, and absolute tool compliance, all executed without reliance on external cloud APIs1. The initial implementation of a "Title DNS" system—acting as an exact-match index or phone book to facilitate quick topic location and link traversal—is a structurally sound architectural starting point1. However, relying on endless regular expression patching to route natural language queries through this index renders the system fragile and ultimately unusable1.

This report presents an exhaustive analysis of advanced computational methodologies for utilizing a static Wikipedia resource in an offline agentic ecosystem. It examines the fundamental mechanics of corpus parsing and relational storage, the resurgence of lexical scaling laws, the neurobiological paradigms underlying modern graph-based retrieval, and the implementation of CPU-optimized intent classification. By synthesizing these paradigms, a robust architecture can be established that eliminates brittle routing patches, mathematically enforces deterministic tool execution, and transforms the encyclopedic corpus into a highly navigable, structured cognitive environment.

## **Deconstructing the MediaWiki Corpus: Parsing and Relational Metadata**

The foundation of any encyclopedic agent lies in how the raw data is extracted, parsed, and stored. Managing millions of raw Markdown files introduces substantial file-system overhead and complicates the extraction of structured metadata1. The native MediaWiki architecture relies on a highly relational SQL schema, which provides critical topological information that is often lost during naive text extraction.

### **Extracting Disambiguation and Alias Metadata**

To resolve complex entity queries, the agent must be able to navigate the inherent ambiguity of human language. A naive vector database cannot easily distinguish between the 1983 miniseries 'V' and the 1984 television series 'V', nor can it reliably map single-letter queries without aggressive regular expression interventions1. The native MediaWiki SQL schema provides built-in mechanisms to resolve these ambiguities, which must be preserved in any offline index.

The page\_props table is critical for local entity disambiguation3. This table contains properties set by the parser during the rendering of wikitext. Specifically, it utilizes the pp\_propname and pp\_value columns to store metadata3. When a Wikipedia article includes the \_\_DISAMBIG\_\_ magic word, the parser automatically records this in the page\_props table6. By executing targeted SQL queries against an offline extraction of this table, the agent's routing logic can instantly determine if a user's query has landed on a disambiguation hub rather than a definitive article5.

Furthermore, the MediaWiki redirect table (rd\_from, rd\_namespace, rd\_title) is essential for mapping aliases and common misspellings4. While basic redirects.tsv dumps frequently lack comprehensive alias mapping, a direct import of the native redirect SQL schema ensures that programmatic suffixes and alternative titles are mathematically linked to the correct primary article1. By integrating these relational tables into the Title DNS, the system can systematically reject false friends without invoking the generative language model.

### **High-Fidelity Wikitext Parsing**

Converting the raw XML dumps of Wikipedia into a format suitable for Large Language Models (LLMs) requires specialized parsing infrastructure. Traditional Python-based tools, such as WikiExtractor, have historically served as the default mechanism for this conversion9. However, these legacy tools are computationally slow and are notorious for silently dropping or mangling complex structural elements like infoboxes, templates, and intricate tables9.

Alternative parsers have been developed to address these deficiencies by constructing full Abstract Syntax Trees (ASTs) from the wikitext markup. Libraries such as MwParserFromScratch (available in C\# and Python) parse the markup into a navigable object tree, allowing programmatic extraction of specific templates and structural components10. More recently, Rust-based parsers like wikrs have demonstrated exponential performance gains9. Utilizing parallel processing across modern CPU architectures, wikrs achieves extraction speeds up to 32 times faster than WikiExtractor, processing hundreds of megabytes per second9. Crucially, it preserves the internal link structure, table integrity, and document hierarchy while emitting precise diagnostics when it encounters pathological markup, preventing the silent corruption of the knowledge base9.

## **The Storage Substrate: ZIM Archives and Analytical Query Engines**

An optimized local architecture requires treating the encyclopedic corpus as a structured library, explicitly separating the storage of the raw textual data from the analytical processing of the link web. This prevents the computational bottlenecks associated with managing 7.1 million individual text files1.

### **ZIM Archives and the Model Context Protocol (MCP)**

For complete offline deployments, the ZIM (Zeno IMproved) file format is the industry standard for highly compressed, read-only data storage11. The entire Wikipedia corpus, encompassing text, structural metadata, and media, can be encapsulated within a single, highly portable ZIM archive11. The libzim reference implementation library provides a shallow, highly efficient C++ interface for reading these files, which can be accessed via Python bindings to achieve near-instantaneous article retrieval12.

The integration of ZIM archives into agentic workflows has been drastically simplified by the advent of the Model Context Protocol (MCP). MCP servers, such as openzim-mcp, operate as a standardized interface layer between the LLM and the local filesystem15. These servers expose the contents of modern ZIM archives directly to the agent as queryable tools15. By leveraging openzim-mcp, an agent can execute sub-second retrieval operations entirely offline, bypassing the need for bespoke text parsing pipelines within the agent's core memory loop16. This transforms the encyclopedic corpus into a reliable, static infrastructure component, removing the latency and volatility of injecting massive documents directly into the context window.

### **SQLite Versus DuckDB for Topology Traversal**

While the ZIM archive handles the retrieval of raw article content, navigating the complex link web—which comprises approximately 188 million edges linking Wikipedia titles—requires a dedicated, highly performant database engine1. The choice of database architecture dictates the speed and efficiency of the agent's pathfinding capabilities.

| Architectural Feature | SQLite (Row-Oriented OLTP) | DuckDB (Column-Oriented OLAP) |
| :---- | :---- | :---- |
| **Storage Paradigm** | Row-based storage; keeps entire records together on disk. | Columnar storage; groups values of the same column together. |
| **Execution Model** | Iterator-based (row-at-a-time processing). | Vectorized execution (batch processing utilizing CPU SIMD parallelism). |
| **Optimal Workload** | High-frequency point queries, exact title lookups, and transactional state management. | Massive data aggregations, wide network scans, and multi-hop link web analysis. |
| **Memory Consumption** | Extremely lightweight; optimized for minimal footprint. | Higher memory usage during complex joins; capable of spilling overflow to disk. |
| **Primary Use Case in RAG** | The "Title DNS" exact-match phone book index. | Analyzing the 188-million edge link web to rank question-intent neighbors. |

For the "Title DNS" system—where the objective is to verify the existence of a specific title or resolve an alias almost instantaneously—SQLite is the uncontested optimal choice1. SQLite is an Online Transaction Processing (OLTP) engine designed for fast, row-based retrieval18. It excels at pinpointing a single record out of millions with minimal overhead19.

Conversely, when the agent must analyze the 188 million outgoing links to rank multi-hop pathways (e.g., determining the strongest semantic path bridging *Stranger Things* and *Running Up That Hill*), a row-based engine struggles1. For these operations, DuckDB, an Online Analytical Processing (OLAP) engine, provides a distinct advantage18. DuckDB's columnar format and vectorized query execution allow it to scan millions of relational edges and perform complex aggregations exponentially faster than SQLite19. Furthermore, DuckDB includes native support for querying ZIM archives directly via its libzim extension, enabling seamless analytical operations across the compressed data structures11. A dual-engine architecture—where SQLite manages the immediate, exact-match Title DNS routing and DuckDB processes the offline, bulk ranking of the link web—provides a balanced, highly scalable indexing tier.

## **Scaling Laws and the Dominance of Lexical Retrieval**

A fundamental question when architecting an encyclopedia-driven agent is whether computationally expensive LLM-driven graph indexing or dense semantic retrieval is strictly necessary for all queries. Recent scaling studies analyzing RAG paradigms across strictly nested tiers—ranging from roughly 1,000 documents to over 512,000 documents (spanning 1.7 million to 601 million tokens)—have revealed a definitive scale-dependent crossover22.

While agentic file-system exploration and dense embedding retrieval perform admirably on small, tightly constrained corpora, their efficacy degrades severely as the search space expands23. Agentic search, where an LLM iteratively explores a directory structure, becomes prohibitively expensive at scale, consuming up to 39 times more query tokens while suffering significant accuracy drops as the volume of distractor documents increases23. Similarly, heavy GraphRAG methodologies frequently hit a "construction wall," where the generative LLM tokens required to extract entities and relations across the entire corpus become financially and computationally unjustifiable, often halting indexing before completing even 2% of a massive dataset23.

The scaling studies demonstrate that at approximately the 10-million token threshold, traditional sparse lexical retrieval—specifically BM25—overtakes both dense retrieval and complex agentic exploration in overall accuracy22. At the full corpus scale of 601 million tokens, BM25 leads alternative scalable variants by a margin approaching 20 accuracy points22. BM25 anchors the low-cost end of the Pareto frontier because it requires zero LLM-based construction time and maintains a nearly scale-invariant query cost22.

The sustained superiority of BM25 at scale is primarily attributed to the inherent nature of encyclopedic queries. Questions regarding specific historical events, media franchises, or scientific theorems rely on highly precise lexical anchors23. Distractor documents in massive corpora are often semantically similar but factually incorrect; dense embedding models frequently fall into these semantic traps because they evaluate contextual proximity rather than exact string matches23. Therefore, for a global Wikipedia deployment, exact lexical matching and relational Title DNS should serve as the foundational default for initial candidate discovery, while expensive agentic reasoning and graph traversals are reserved exclusively for post-retrieval synthesis and explicit multi-hop inquiries1.

## **Entity Disambiguation and CPU-Optimized Intent Routing**

The existing architecture struggles with routing conversational natural language through a rigid, exact-match index, resulting in an unsustainable reliance on regular expression patching1. Attempting to treat conversational NLP as a direct encyclopedia index leads to endless edge cases, such as failing to map decade years (e.g., matching "1980" inside "1980s") or failing to properly parse single-letter quoted titles1.

While employing a generative LLM to classify user intent prior to executing a database lookup is theoretically effective, it introduces severe latency bottlenecks due to token generation overhead and context window management25. To achieve sub-second response times without invoking the primary generative model, the architecture must leverage highly optimized local entity disambiguation and intent classification models.

### **Unsupervised Entity Linking and Disambiguation**

Resolving named entities against a local knowledge base is a well-studied problem in computational linguistics. Systems such as BLINK and REL (Radboud Entity Linker) have historically been utilized to map text mentions to specific Wikipedia URIs27. However, models like BLINK, which rely heavily on dense retrieval, often struggle with out-of-domain text or highly ambiguous, low-resource queries where they fail to find suitable matches28.

For unsupervised entity disambiguation, approaches leveraging Group Steiner Trees (GST) have demonstrated success in identifying the most relevant candidates by calculating contextual similarities across all entity mentions present in a document30. By examining the collective context of the query, these algorithms can disambiguate terms locally without requiring a massive, pre-trained dense index30.

### **The SetFit Architecture for Latency Reduction**

To completely eliminate regex patching and resolve conversational ambiguity instantly, the SetFit (Sentence Transformer Fine-tuning) framework offers an unparalleled solution. SetFit is an efficient, prompt-free architecture for few-shot text classification31. It utilizes contrastive learning to fine-tune standard Sentence Transformers on highly constrained datasets, achieving exceptional accuracy with as few as 8 to 16 examples per class26.

Because SetFit is fundamentally an embedding-based classification head rather than a generative autoregressive model, it can be executed natively on consumer CPUs with negligible latency25. By exporting the trained SetFit model to the ONNX (Open Neural Network Exchange) format and applying INT8 post-training quantization, the model's memory footprint is reduced by up to 75% while maintaining over 98% of its original accuracy2.

Extensive benchmarking demonstrates that an optimized, 22M-parameter SetFit model operating on a CPU can classify user intent in approximately 2.4 to 5 milliseconds26. In direct comparisons, this tiny 22M-parameter model achieved 91.1% accuracy on intent classification tasks, vastly outperforming a 20B-parameter LLM (which achieved only 68.8% accuracy) while operating at more than 700 times lower latency26. SetFit also demonstrates a superior precision and recall trade-off when compared to legacy algorithms like TF-IDF or FastText, particularly in complex linguistic domains36.

Within the offline Wikipedia agent architecture, a localized SetFit model completely replaces the fragile regex routing tier. It acts as an ultra-fast, pre-generation classifier that interprets the user's conversational input in real-time. For instance, if a user queries "the 1984 one" following a disambiguation prompt, the SetFit classifier instantly detects the intent as a temporal clarification and routes the exact parameters directly to the SQLite Title DNS1. This constraint-driven architectural decision bypasses the generative LLM for up to 80% of standard navigational queries, dramatically reducing end-to-end latency and reserving GPU compute strictly for complex text synthesis2.

## **Graph-Based Retrieval and the Hippocampal Paradigm**

When lexical retrieval is insufficient for answering multi-hop queries that require connecting disjointed facts across disparate articles, the system must employ graph-based retrieval. Traditional GraphRAG approaches construct massive knowledge graphs from raw text, but they frequently suffer from poor accuracy when the necessary reasoning path is obscured by high-density topological noise38.

### **The HippoRAG Architecture and Personalized PageRank**

The HippoRAG framework addresses the limitations of standard vector similarity by modeling its retrieval process on the hippocampal indexing theory of human long-term memory40. According to this neurobiological theory, the mammalian neocortex stores the actual complex memory representations, while the hippocampus maintains a specialized index of pointers and associations connecting these memories40.

In the artificial HippoRAG system, the LLM acts as the neocortex, while a schema-less knowledge graph—built using Open Information Extraction (OpenIE) to generate subject-relation-object triples—functions as the artificial hippocampus41. When a query is received, the system extracts the named entities and maps them to seed nodes within the graph42. The system then executes the Personalized PageRank (PPR) algorithm, which performs a rapid, single-step multi-hop graph traversal to discover structurally connected information40.

The mathematical foundation of this traversal updates the probability distribution over the graph nodes at step ![][image1] using the following equation:

![][image2]

In this formulation, ![][image3] represents the personalized probability distribution over the initial seed nodes, ![][image4] is the row-normalized transition matrix of the graph, and ![][image5] is the damping factor43. This mechanism allows the probability mass to flow outward from the seed entities across the relation edges, illuminating structurally connected concepts that may lack direct lexical overlap with the original query41. The subsequent iteration, HippoRAG 2, refines this process by integrating actual passage nodes into the knowledge graph alongside entity phrases, closing the gap between abstract conceptual linking and contextual reading42.

### **The Static Graph Fallacy and Semantic Drift**

While PPR over a knowledge graph excels at associative reasoning, it introduces a severe, critical failure mode characterized in recent literature as the "Static Graph Fallacy"43. In standard HippoRAG implementations, the transition matrix ![][image4] is fixed during the offline indexing phase43. This static rigidity ignores the reality that the relevance of any given edge is highly dependent on the specific context of the user's query43.

When the PPR algorithm executes on a static graph, the probability mass is frequently siphoned into high-degree "hub" nodes—broad, generic entities such as "French", "Nobel Prize", or "Television Series"43. This phenomenon, known as semantic drift, causes the stochastic random walk to divert into entirely irrelevant topological clusters before it can reach the critical downstream evidence required to answer the query43. Consequently, the system exhibits a deceptive failure mode: standard retrieval metrics like Recall may appear high because the initial entity is successfully retrieved, but the actual reasoning chain is completely broken, preventing the LLM from synthesizing an accurate answer43.

### **Steering the Graph: CatRAG and Context-Aware Traversal**

To counteract semantic drift and overcome the Static Graph Fallacy, the CatRAG (Context-Aware Traversal for robust RAG) framework actively transforms the static knowledge graph into a query-adaptive navigation structure43. CatRAG introduces a multi-faceted optimization layer that actively steers the random walk based on the user's intent:

> 1. **Symbolic Anchoring:** Rather than relying exclusively on dense vector alignment to link the query to the graph, CatRAG extracts explicit entities from the prompt and injects them as "weak seeds" with small reset probabilities43. This serves as a regulatory function, creating a gravitational pull that forces the PPR propagation to recurrently ground itself to the exact entities mentioned by the user, successfully resisting diffusion into generic graph hubs43.  
> 2. **Query-Aware Dynamic Edge Weighting:** Before traversal begins, CatRAG dynamically modulates the weights of the relation edges. By utilizing a lightweight LLM call to assess the relevance of outgoing edges from the seed entities, the framework generates a query-specific transition matrix ![][image6]43. This proactively amplifies the structural paths that align with the user's intent while aggressively pruning irrelevant branches43. To manage the computational overhead of this step, CatRAG employs conditional summarization: it generates concise summaries for evaluating high-degree nodes only when their connected facts exceed a defined density threshold, otherwise utilizing raw triples43.  
> 3. **Key-Fact Passage Weight Enhancement:** This mechanism structurally anchors the traversal to the physical documents containing verified evidentiary triples, boosting the weight of context edges that lead to distinct, substantive evidence rather than superficial entity mentions43.

By implementing dynamic graph steering, CatRAG substantially improves "Full Chain Retrieval"—the metric defining the system's capacity to recover complete, multi-hop evidence paths without logical gaps43. For an agent attempting to navigate a Wikipedia link web, applying dynamic edge weighting based on the query (e.g., artificially amplifying edges related to "soundtrack" when querying about a song from *Stranger Things*) ensures the agent traverses directly to the correct neighbor node (such as *Running Up That Hill*) without being absorbed by irrelevant hub nodes1.

## **Advanced Knowledge Topologies: Trees, Propositions, and Error Books**

Beyond node-based GraphRAG, alternative structural methodologies have been developed to manage document-level reasoning and mitigate the immense indexing costs associated with knowledge graphs.

### **Hierarchical Trees and Proposition Paths**

The Ψ-RAG (Psi-RAG) framework abandons traditional entity-relation graphs entirely, in favor of a hierarchical abstract tree index46. It utilizes an iterative "merging and collapse" process to adapt to textual data distributions without a priori assumptions46. Ψ-RAG deploys a multi-granular retrieval agent that interacts simultaneously with a dense tree index (for thematic matching) and a sparse BM25 keyword index (for precise token-level matching)46. In direct benchmarking on multi-hop QA datasets like HotpotQA, this well-structured tree model combined with an agentic retriever outperformed HippoRAG 2 by 7.4% in average F1 score, indicating that intelligent hierarchical summarization can match or exceed the capabilities of triple-based graph systems46.

Alternatively, the PropRAG architecture shifts the fundamental retrieval unit from extracted entities to context-rich propositions47. Rather than ranking nodes via automated graph diffusion, PropRAG utilizes an explicit, LLM-free online beam search to discover complete reasoning paths across proposition graphs47. This highlights a crucial architectural principle: the graph topology should not merely serve as a passive navigation map to locate text chunks; the sequential path itself must be validated for logical coherence before the evidence is presented to the generative model for final synthesis47. Furthermore, systems like IndexRAG attempt to shift this cross-document reasoning entirely to the offline indexing stage by generating "bridging facts" as independently retrievable units, eliminating the need for iterative graph traversal during online inference50.

### **LLM-Wiki and the Self-Evolving Error Book**

The LLM-Wiki framework operationalizes a "Retrieval-as-Reasoning" paradigm that directly addresses the challenges of routing agents through encyclopedic structures51. Rather than treating Wikipedia as a static retrieval index that returns a fixed top\-![][image1] context array, the external knowledge is treated as a compilable, composable, and self-evolving structure51. The autonomous agent is equipped with specific traversal tools—such as wiki\_search and wiki\_read—and is tasked with composing its own logical path based on intermediate observations51.

If a query requires a bridging inference, the agent actively reads the lead of the initial page, identifies the hyperlink to the secondary entity, and traverses the link web autonomously, terminating the search loop only when it assesses that the accumulated evidence is sufficient51. To maintain the integrity of this process, LLM-Wiki introduces the "Error Book"—a persistent self-correction mechanism52. The Error Book operates through a lifecycle of discovering structural errors, attributing their root cause, formalizing them as natural-language constraints, and injecting these constraints into subsequent compilation prompts52. This allows the agent's navigational logic to evolve iteratively without requiring a full rebuild of the encyclopedic knowledge base52.

## **Local Hardware Constraints and Foundation Model scaling**

Executing complex agentic reasoning and graph traversals entirely offline requires strict adherence to local hardware constraints. The architecture must balance the need for high reasoning capacity against the physical limits of consumer Graphical Processing Unit (GPU) Video RAM (VRAM).

### **The Qwen2.5 27B/32B Tier**

In the landscape of open-weight models, the 8B to 32B parameter class occupies a critical strategic threshold for local deployments53. The Qwen2.5 lineage, specifically the 27B and 32B models, establishes the optimal VRAM-and-latency sweet spot for single-GPU workstations53. While massive 70B+ parameter models provide superior reasoning, they cannot be served locally without expensive multi-GPU arrays.

By utilizing the GGUF (GPT-Generated Unified Format) and applying 4-bit activation quantization (such as Q4\_K\_M), a 27B or 32B model can be compressed to fit comfortably within the 24GB VRAM limit of a single consumer GPU (e.g., NVIDIA RTX 3090 or 4090\)53. These models couple decoder-only causal Transformer architectures with advanced mechanisms like Grouped-Query Attention (GQA) and SwiGLU, delivering benchmark performance that approaches 70B-class models53. Within the llama.cpp ecosystem, these 4-bit quantized models are capable of achieving 25 to 30 tokens per second decode speeds, enabling real-time, fluid agentic interactions53.

While models like Qwen2.5 support massive theoretical context windows up to 128,000 tokens, fully utilizing this context requires substantial KV-cache memory allocation, which rapidly exhausts available VRAM53. Therefore, relying on massive context windows to ingest raw, unfiltered Wikipedia articles is a hardware-inefficient strategy. The agent must instead rely on highly precise, constrained retrieval to minimize context bloat and preserve GPU memory for complex inference tasks.

## **Deterministic Tool Execution via Constrained Decoding**

One of the most persistent, resource-draining failure modes in agentic systems is the "slow fail" loop1. This occurs when the model ignores injected context, hallucinates tool parameters, or attempts to call tools that are offline (e.g., continuously attempting to trigger wiki\_scout\_search when the Weaviate endpoint is unreachable)1. Relying purely on prompt engineering to force an LLM to follow precise JSON schemas is statistically fragile; the agent must be mathematically forced to adhere to valid operational schemas.

### **The Mechanics of Grammar-Constrained Generation**

Constrained decoding ensures that a generative model literally cannot produce invalid output. Instead of relying on the LLM to follow prompt instructions, the inference engine applies a strict formal grammar to the sampling phase. It computes the logit scores for every token in the vocabulary, but before the softmax layer selects the final token, the engine masks out any probabilities that would violate the required structural format56. Modern inference engines, including llama.cpp and vLLM, support highly sophisticated structured outputs through various backend compilers56.

&nbsp;

| Constraint Engine | Core Compilation Mechanism | Compilation Overhead | Masking Latency | Primary Architectural Use Case |
| :---- | :---- | :---- | :---- | :---- |
| **Outlines** | FSM-based regex/schema compilation | 3–12 seconds | Moderate | Static schemas in batch processing where heavy compilation costs are amortized58. |
| **llguidance** | Prefix trie traversal via regular expression derivatives | \< 60 milliseconds | \< 50 microseconds | High-throughput cloud environments with frequently changing JSON schemas58. |
| **XGrammar** | Precomputed context-independent vocabulary validation | 0.12–0.30 seconds | \< 40 microseconds | Production deployments requiring ultra-fast, dynamic schema enforcement58. |
| **GBNF (llama.cpp)** | GGML Backus-Naur Form custom grammars | Negligible (Native C++) | Low | Embedded systems and local inference nodes utilizing GGUF quantized models58. |

### **GBNF and XGrammar Integration**

Within the llama.cpp ecosystem, formal grammars are defined using GBNF (GGML Backus-Naur Form)59. GBNF extends standard BNF notation with regex-like features to define exact string sequences, structural repetitions, and valid JSON hierarchies59. When a specific JSON schema is provided for a local tool (e.g., wiki\_read(paths)), llama.cpp automatically converts that schema into a GBNF grammar, enforcing the exact parameters required by the offline agent56.

Historically, Finite State Machine (FSM) parsing for large vocabularies introduced significant computational latency. The recent implementation of the XGrammar backend has revolutionized this process58. XGrammar relies on the architectural insight that over 99% of a model's vocabulary tokens possess context-independent validity relative to a specific grammar58. Because this validity is precomputed during the brief compilation phase, the inference engine only needs to evaluate a microscopic fraction of tokens at runtime58. This optimization reduces the mask computation time to under 40 microseconds, yielding end-to-end inference speedups of up to 14x over legacy constraint libraries57. By generating precomputed bitmasks for tool JSON schemas, the agent is mathematically blocked from hallucinating API calls, guaranteeing 100% schema-valid output every time and completely eliminating the latency associated with prompt-and-pray retry loops56.

### **Mitigating the Greedy-Local Trap**

While constrained decoding guarantees structural perfection, it introduces the risk of the "greedy-local trap"57. Masking algorithms optimize locally; they force the selection of the best legal token at the current step without knowing if that choice forces the model into a semantic corner later in the sequence, severely degrading output quality57. Furthermore, forcing a model into a strict JSON format from the very first generated token actively prevents Chain-of-Thought (CoT) reasoning, as the model is forbidden from "thinking out loud" before committing to a final answer57.

To maximize the multi-hop reasoning capabilities of local models like Qwen2.5, the architecture must implement an agentic "scratchpad" protocol57. The enforced GBNF grammar should permit the model to generate free-form text within a designated \<thought\> block before restricting it to a rigid JSON structure for the final tool call or factual answer57. This allows the model to internally map out its logical synthesis while maintaining absolute deterministic control over the programmatic output passed back to the local system.

## **Context Engineering and Active Memory Management**

To prevent local agentic models from being overwhelmed by massive Wikipedia markdown dumps, the system must practice deliberate context engineering. The context window is a scarce, finite computational resource62. Indiscriminately injecting full articles limits the model's ability to maintain coherent conversational state and execute complex planning algorithms.

Managing what information remains in the active context window across multiple interactions requires sophisticated active memory management63. Irreversible decisions to selectively retain or discard context can lead to catastrophic conversational failures if future turns require historical information that was prematurely deleted by the system64.

To resolve this, advanced memory architectures employ protocols such as the Co-Forgetting Protocol, which utilizes a quorum-based voting mechanism enabling the agentic system to collaboratively decide whether to retain or discard specific memory segments based on their ongoing relevance66. By dynamically analyzing the utility of past evidence against the current conversational trajectory, the system can smoothly compress short-term episodic data while continuously offloading factual Wikipedia leads into a stable, long-term semantic store62. Furthermore, adopting underlying foundation models that utilize selective state spaces—such as the Mamba architecture—allows for highly advanced token-aware selectivity, enabling the model to organically filter relevant information and discard noise with far greater precision than traditional attention-based mechanisms68.

## **Synthesis and Architectural Recommendations**

The successful deployment of a static, offline Wikipedia resource for an autonomous agentic framework requires a deliberate architectural shift away from the brute-force application of dense vector databases and unstructured generative routing. The analysis of current retrieval mechanisms indicates that an optimal architecture must be modular, deterministic, and highly specialized for local hardware constraints.

To resolve the systemic failures outlined in the baseline infrastructure, the following architectural synthesis is recommended:

> 1. **Storage and Extraction:** Migrate raw markdown storage to a highly compressed ZIM archive, accessed via the openzim-mcp interface for zero-overhead, zero-network offline reading. Maintain the SQLite "Title DNS" for instant transactional exact-matching and alias resolution utilizing native page\_props metadata, but integrate DuckDB to process analytical queries over the 188 million-edge link web.  
> 2. **Lexical Dominance and Intent Routing:** Acknowledge the scaling superiority of BM25 for precise encyclopedic entity discovery. Completely replace brittle regex patching with a CPU-bound, ONNX INT8-quantized SetFit classifier. This enables sub-10ms conversational intent routing and temporal disambiguation without invoking the primary generative LLM.  
> 3. **Graph Traversal:** Implement CatRAG principles over the Wikipedia link web. Utilize Symbolic Anchoring and Query-Aware Dynamic Edge Weighting to proactively prune high-degree hub nodes. This eliminates semantic drift and guarantees complete, multi-hop reasoning paths without falling into the Static Graph Fallacy.  
> 4. **Deterministic Execution:** Enforce strict tool calling using XGrammar or llama.cpp's native GBNF. By generating precomputed bitmasks for tool JSON schemas, the agent is mathematically blocked from hallucinating API calls, resolving the issue of the agent ignoring injected context and falling into slow-fail loops.

By treating the offline encyclopedia not as unstructured memory fuel, but as a rigidly structured, highly navigable toolset governed by mathematical constraints, the agentic system can execute complex informational retrieval flawlessly, entirely offline, and well within the boundaries of consumer hardware.

#### **Works cited**

> 1. WIKIPEDIA\_RESEARCH\_BRIEF.md  
> 2. (PDF) AXIOM: Efficient Voice Agent System on Consumer Hardware, [https://www.researchgate.net/publication/400449198\_AXIOM\_Efficient\_Voice\_Agent\_System\_on\_Consumer\_Hardware\_Through\_Constraint-Driven\_Architecture](https://www.researchgate.net/publication/400449198_AXIOM_Efficient_Voice_Agent_System_on_Consumer_Hardware_Through_Constraint-Driven_Architecture)  
> 3. Manual:Database layout/diagram/1.38.0 \- MediaWiki, [https://www.mediawiki.org/wiki/Manual:Database\_layout/diagram/1.38.0](https://www.mediawiki.org/wiki/Manual:Database_layout/diagram/1.38.0)  
> 4. Manual:Database layout/diagram/1.34.0 \- MediaWiki, [https://www.mediawiki.org/wiki/Manual:Database\_layout/diagram/1.34.0](https://www.mediawiki.org/wiki/Manual:Database_layout/diagram/1.34.0)  
> 5. Manual:page\_props table \- MediaWiki, [https://www.mediawiki.org/wiki/Manual:Page\_props\_table](https://www.mediawiki.org/wiki/Manual:Page_props_table)  
> 6. Extension:Disambiguator \- MediaWiki, [https://www.mediawiki.org/wiki/Extension:Disambiguator](https://www.mediawiki.org/wiki/Extension:Disambiguator)  
> 7. Manual:Database layout/diagram/1.44.0 \- MediaWiki, [https://www.mediawiki.org/wiki/Manual:Database\_layout/diagram/1.44.0](https://www.mediawiki.org/wiki/Manual:Database_layout/diagram/1.44.0)  
> 8. MediaWiki: Maintenance, [https://doc.wikimedia.org/mediawiki-core/1.31.5/php/group\_\_Maintenance.html](https://doc.wikimedia.org/mediawiki-core/1.31.5/php/group__Maintenance.html)  
> 9. SFARL/wikrs \- Fast, honest wikitext extraction and parsing \- GitHub, [https://github.com/SFARL/wikrs](https://github.com/SFARL/wikrs)  
> 10. Alternative parsers \- MediaWiki, [https://www.mediawiki.org/wiki/Alternative\_parsers](https://www.mediawiki.org/wiki/Alternative_parsers)  
> 11. List of Community Extensions \- DuckDB, [https://duckdb.org/community\_extensions/list\_of\_extensions](https://duckdb.org/community_extensions/list_of_extensions)  
> 12. homebrew-core \- Homebrew Formulae, [https://formulae.brew.sh/formula/](https://formulae.brew.sh/formula/)  
> 13. Crosstalk-Solutions/project-nomad: Project NOMAD is an ... \- GitHub, [https://github.com/crosstalk-solutions/project-nomad](https://github.com/crosstalk-solutions/project-nomad)  
> 14. python-libzim \- Context7, [https://context7.com/openzim/python-libzim](https://context7.com/openzim/python-libzim)  
> 15. openzim-mcp · PyPI, [https://pypi.org/project/openzim-mcp/1.3.0/](https://pypi.org/project/openzim-mcp/1.3.0/)  
> 16. Projects | Cameron Rye, [https://rye.dev/projects/](https://rye.dev/projects/)  
> 17. MCP Vetted — MCP servers ranked by quality score, [https://mcp-vetted.com/](https://mcp-vetted.com/)  
> 18. In-depth: DuckDB vs SQLite \- PostHog, [https://posthog.com/blog/duckdb-vs-sqlite](https://posthog.com/blog/duckdb-vs-sqlite)  
> 19. DuckDB vs SQLite: A Complete Database Comparison \- DataCamp, [https://www.datacamp.com/blog/duckdb-vs-sqlite-complete-database-comparison](https://www.datacamp.com/blog/duckdb-vs-sqlite-complete-database-comparison)  
> 20. DuckDB vs SQLite on a server \- SSD Nodes, [https://www.ssdnodes.com/learn/duckdb-vs-sqlite-server](https://www.ssdnodes.com/learn/duckdb-vs-sqlite-server)  
> 21. DuckDB vs SQLite: Which one is better? \- DEV Community, [https://dev.to/ranaweerasupun/duckdb-vs-sqlite-two-tiny-databases-that-dont-actually-compete-39d1](https://dev.to/ranaweerasupun/duckdb-vs-sqlite-two-tiny-databases-that-dont-actually-compete-39d1)  
> 22. A Scaling Study of Retrieval-Augmented Generation Paradigms \- arXiv, [https://arxiv.org/html/2607.26497](https://arxiv.org/html/2607.26497)  
> 23. Which RAG Paradigm Wins at Scale? A Scaling Study of Retrieval, [https://arxiv.org/html/2607.26497v1](https://arxiv.org/html/2607.26497v1)  
> 24. Benfeng Xu \- CatalyzeX, [https://www.catalyzex.com/author/Benfeng%20Xu](https://www.catalyzex.com/author/Benfeng%20Xu)  
> 25. I built a \<400ms Latency Voice Agent \+ Hierarchical RAG that runs, [https://www.reddit.com/r/LocalLLaMA/comments/1qxu6l8/i\_built\_a\_400ms\_latency\_voice\_agent\_hierarchical/](https://www.reddit.com/r/LocalLLaMA/comments/1qxu6l8/i_built_a_400ms_latency_voice_agent_hierarchical/)  
> 26. Structured Intent Canonicalization with Few-Shot Learning \- arXiv, [https://arxiv.org/html/2602.18922v1](https://arxiv.org/html/2602.18922v1)  
> 27. Word Sense Disambiguation with Wikipedia Entities: A Survey of, [https://www.mdpi.com/1099-4300/28/2/236](https://www.mdpi.com/1099-4300/28/2/236)  
> 28. Entity Linking & Disambiguation \- AI Engineering from Scratch, [https://aiengineeringfromscratch.com/lesson?path=phases%2F05-nlp-foundations-to-advanced%2F25-entity-linking](https://aiengineeringfromscratch.com/lesson?path=phases/05-nlp-foundations-to-advanced/25-entity-linking)  
> 29. Neural Entity Linking: A Survey of Models Based on Deep Learning, [https://www.semantic-web-journal.net/system/files/swj2875.pdf](https://www.semantic-web-journal.net/system/files/swj2875.pdf)  
> 30. Unsupervised Named Entity Disambiguation for Low Resource, [https://www.researchgate.net/publication/387078843\_Unsupervised\_Named\_Entity\_Disambiguation\_for\_Low\_Resource\_Domains](https://www.researchgate.net/publication/387078843_Unsupervised_Named_Entity_Disambiguation_for_Low_Resource_Domains)  
> 31. Production Machine Learning — 545 Open-Source MLOps Tools, [https://ethical.institute/open-source/production-ml-list/](https://ethical.institute/open-source/production-ml-list/)  
> 32. Efficiently run SetFit Models with Optimum \- Hugging Face, [https://huggingface.co/docs/setfit/en/tutorials/onnx](https://huggingface.co/docs/setfit/en/tutorials/onnx)  
> 33. Efficiently run SetFit Models with Optimum \- Hugging Face, [https://huggingface.co/docs/setfit/tutorials/onnx](https://huggingface.co/docs/setfit/tutorials/onnx)  
> 34. e5\_onnx\_optimization \- Kaggle, [https://www.kaggle.com/code/amadevs/e5-onnx-optimization](https://www.kaggle.com/code/amadevs/e5-onnx-optimization)  
> 35. NLP Engineer Salary & Career Guide | MortalJobs, [https://mortaljobs.com/ai-job-roles/nlp-engineer/](https://mortaljobs.com/ai-job-roles/nlp-engineer/)  
> 36. An improved TF-IDF approach for text classification \- ResearchGate, [https://www.researchgate.net/publication/376540160\_An\_improved\_TF-IDF\_approach\_for\_text\_classification](https://www.researchgate.net/publication/376540160_An_improved_TF-IDF_approach_for_text_classification)  
> 37. A Survey of Data Augmentation Approaches for NLP \- ResearchGate, [https://www.researchgate.net/publication/353488271\_A\_Survey\_of\_Data\_Augmentation\_Approaches\_for\_NLP](https://www.researchgate.net/publication/353488271_A_Survey_of_Data_Augmentation_Approaches_for_NLP)  
> 38. Retrieving Minimal and Sufficient Reasoning Subgraphs with Graph, [https://arxiv.org/html/2603.07179v1](https://arxiv.org/html/2603.07179v1)  
> 39. Daily Papers \- Hugging Face, [https://huggingface.co/papers?q=Graph%20RAG](https://huggingface.co/papers?q=Graph+RAG)  
> 40. HippoRAG: Neurobiologically Inspired Long-Term Memory for Large, [https://www.alphaxiv.org/abs/2405.14831](https://www.alphaxiv.org/abs/2405.14831)  
> 41. From RAG to Memory: Non-Parametric Continual Learning for Large, [https://www.alphaxiv.org/abs/2502.14802](https://www.alphaxiv.org/abs/2502.14802)  
> 42. From RAG to Memory: Non-Parametric Continual Learning for Large, [https://icml.cc/virtual/2025/poster/45585](https://icml.cc/virtual/2025/poster/45585)  
> 43. Context-Aware Traversal for Robust Retrieval-Augmented Generation, [https://arxiv.org/html/2602.01965v1](https://arxiv.org/html/2602.01965v1)  
> 44. From RAG to Memory: Non-Parametric Continual Learning for Large, [https://openreview.net/forum?id=LWH8yn4HS2](https://openreview.net/forum?id=LWH8yn4HS2)  
> 45. Breaking the Static Graph: Context-Aware Traversal for Robust, [https://huggingface.co/papers/2602.01965](https://huggingface.co/papers/2602.01965)  
> 46. Hierarchical Abstract Tree for Cross-Document Retrieval ... \- alphaXiv, [https://www.alphaxiv.org/abs/2605.00529](https://www.alphaxiv.org/abs/2605.00529)  
> 47. PropRAG: Guiding Retrieval with Beam Search over Proposition Paths, [https://aclanthology.org/2025.emnlp-main.317.pdf](https://aclanthology.org/2025.emnlp-main.317.pdf)  
> 48. PropRAG: Guiding Retrieval with Beam Search over Proposition Paths, [https://www.alphaxiv.org/replicate/2504.18070](https://www.alphaxiv.org/replicate/2504.18070)  
> 49. CAGE: Coherence-Aware Graph Encoding for Retrieval-Augmented, [https://arxiv.org/html/2609.04647v1](https://arxiv.org/html/2609.04647v1)  
> 50. Bridging Facts for Cross-Document Reasoning at Index Time \- arXiv, [https://arxiv.org/html/2603.16415v1](https://arxiv.org/html/2603.16415v1)  
> 51. Self-Evolving Agent-Native Retrieval via LLM-Wiki \- arXiv, [https://arxiv.org/html/2605.25480](https://arxiv.org/html/2605.25480)  
> 52. Self-Evolving Agent-Native Retrieval via LLM-Wiki \- arXiv, [https://arxiv.org/html/2605.25480v1](https://arxiv.org/html/2605.25480v1)  
> 53. digital-archaeology/excavations/qwen.md at main \- GitHub, [https://github.com/t81dev/digital-archaeology/blob/main/excavations/qwen.md](https://github.com/t81dev/digital-archaeology/blob/main/excavations/qwen.md)  
> 54. CanIRunLLM — VRAM Calculator for 63 Local LLMs \- id8 Tools, [https://id8.co.in/tools/can-i-run-llm](https://id8.co.in/tools/can-i-run-llm)  
> 55. Deploying Open Weights Models: Gemma 2 vs Llama ... \- Shyank Dev, [https://www.shyankdev.us/blogs/deploying-open-weights-gemma-2-vs-llama-3-vs-qwen-2-5](https://www.shyankdev.us/blogs/deploying-open-weights-gemma-2-vs-llama-3-vs-qwen-2-5)  
> 56. JSON Mode & Grammars for Local LLMs: Full Guide (2026), [https://localaimaster.com/blog/json-mode-grammars-guide](https://localaimaster.com/blog/json-mode-grammars-guide)  
> 57. Your LLM Obeys 99% of the Time. That 1% Is Taking ... \- Towards AI, [https://pub.towardsai.net/your-llm-obeys-99-of-the-time-that-1-is-taking-down-production-a6ea1b6f00c1](https://pub.towardsai.net/your-llm-obeys-99-of-the-time-that-1-is-taking-down-production-a6ea1b6f00c1)  
> 58. Grammar-Constrained Generation: The Output Reliability Technique, [https://tianpan.co/blog/2026/04/16/grammar-constrained-generation-output-reliability](https://tianpan.co/blog/2026/04/16/grammar-constrained-generation-output-reliability)  
> 59. llama.cpp/grammars/README.md at master · ggml-org ... \- GitHub, [https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md)  
> 60. Constraining LLM Output with GBNF to JSON Schema \- Grasp, [https://paths.grasp.study/public-courses/7523f750-8de8-4c2c-adef-9c641ff40819/modules/0e0fcca1-ad0c-44ea-840b-49aefb81160b/lessons/af054e54-4d2a-440d-aba3-75753b5c77cf](https://paths.grasp.study/public-courses/7523f750-8de8-4c2c-adef-9c641ff40819/modules/0e0fcca1-ad0c-44ea-840b-49aefb81160b/lessons/af054e54-4d2a-440d-aba3-75753b5c77cf)  
> 61. \[RFC\] Deterministic Draft Filter: Pluggable Domain Validator, [https://github.com/ggml-org/llama.cpp/discussions/25219](https://github.com/ggml-org/llama.cpp/discussions/25219)  
> 62. Context Engineering \- LLM Memory and Retrieval for AI Agents, [https://weaviate.io/blog/context-engineering](https://weaviate.io/blog/context-engineering)  
> 63. Active Memory: Adaptive Data Systems \- Emergent Mind, [https://www.emergentmind.com/topics/active-memory](https://www.emergentmind.com/topics/active-memory)  
> 64. Scaling Managed Agents: Decoupling the brain from the hands, [https://www.anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents)  
> 65. Context Compression for Long-Horizon AI Agents: Lifecycle, [https://www.preprints.org/manuscript/202607.0924](https://www.preprints.org/manuscript/202607.0924)  
> 66. PBFT‑Backed Semantic Voting for Multi‑Agent Memory Pruning \- arXiv, [https://arxiv.org/html/2506.17338v2](https://arxiv.org/html/2506.17338v2)  
> 67. PBFT-Backed Semantic Voting for Multi-Agent Memory Pruning \- arXiv, [https://arxiv.org/pdf/2506.17338](https://arxiv.org/pdf/2506.17338)  
> 68. Mamba for Dummies: Efficient Linear-Time LLMs Explained \- Medium, [https://michielh.medium.com/mamba-for-dummies-linear-time-llms-explained-0d4b51efcf9f](https://michielh.medium.com/mamba-for-dummies-linear-time-llms-explained-0d4b51efcf9f)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAcCAYAAAC3f0UFAAAA6ElEQVR4Xu2RwQpBQRSGj1AKYekBKCtPodjIUikbG8lKKXtZeQXlBexsLZSltWeQZKOsJP7/npmaO6495auve2fOac6ZMyK/TQqWYAs2vNgbC/g0brxYJAfR5KYfiOIGL7DiB6LgqTuY9QM+BdHkjrOXhmUYc/YCqvBqvqQr2tIJ1myShdNYwjgcw6ToCFlt5OQFLezhAE7g3OyzyhYWzTqAt2fJO5yKnvqRmWi5BKzDM+yHMhz4Yky2DM0ep5GHGScmR9EWLByfTV6L96I8deWs26Ktcb68Q2jOTO456xx8iPbO/z/fygt3bCmCkJXZNgAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAA7CAYAAADGgdZDAAAFR0lEQVR4Xu3dW6htUxgH8CEUuedyiFJCiVAuEQ8nt0guyYPiVSQvKOJBu+TJi6TEi0t5wYNCSsp5UBSPRC45REpJlAfkMr7mmud8a5y112Wvtdc+a/v96mvPMdba66y55qz1P2OMOXcpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADw//Bs2j6w1uGpvREvtx3QOL/WUam9I20H5xAAJFeX4S/OR2qdltqT3FDrh1oXpL5Da92S2pAdUGsttY+o9VpqB+cQACRfNu3vm3b2UNsxEP05sIWvmjb04nw5JLUjmF2V2j3nEAAMvNi0fy7diNujta5rHpslsMXrxkjKMvzYdixZ7OdJtW4dtJ8rw6OWq6rdr0X5tml/VLoA92qtD1L/Ms8hANhvxVq1HMJiKvS9WifWuqzWwYOKL+2ox9L2CYPfCaMCW/Qd0/RthndLN33WuqnWv23nJol1fzE1/Ffqy9uratR+LcJ3TfufWg+U7lyL867XnkPX1vqz1u2lC5G/1vpksB19cbxP2fNsANgm2sDWr1/7JfVls4ywRd+8Fy9MEqNYHzZ9B9W6udbFZXmBLTxe663UvrHWvam9ldpR1Fm0+7UIObD169cerrUz9Yf2HPo0bYc4vnkqNZ4fxx8Atp38Zbx78HNX6cJQO603LrBd1PQt4yq/52td3nYORIBcZmCLadkcHiI4/JHaW2mewNbu1yLk4BXBNo5hHK/4+WB6rD2H1tL2yaU7vnkt3KKDJQAszVmlG4WKqaMQV4XmIPN52s7TT6NGx9YLbKN81nZsgt/K6PcZlhHYYr3Vm6X7bNvwEOb592Oa96dar9f6u8y3lmvWwDZpv6YRF6/E9GUf+uN1Lh1s31b2nmv5tY9L22HcORTnYkylAsC28Erpvhz78BDrhHKQiDU/Z6f2Ipxe69S2c4SYGptUx+559r7GBaLNDmwxbdx/bjECNSo8xOjUjrZzCvHZxXvvQ1q8fgTvjZolsE2zX5M8Xbr3nkfnYq1hrIfrxQUG40w6h3YXI2oAbBPxpRkB7akyfJ+rj9N2uKJpzysWhy/DuEA2TWBbK90VnevVfXueOSxGiPJC/PXWecXVkHGBxijx3iLEjBKhKUJPBJwXyvrPG+Xcsu9+fDOi7/j+F5Jp9yvEc2MfDmsfKF3IjpGz/PnHlHkeQYvz8pLUbk06h+K1Fz1VCwBbKkZJ8ghNfBFvB+MC2TSBbaMiiOX1Veut8xoX2O6sdWbbORDve5abF08y7QjbtPsV+v8IrOeuMrxWrb0x7jxGrV8DgJWXg0uMjIy6DcZW6G8RMq7Grd0aF8g2O7Dl6b0+PMT9xLLfy/pr7MaJ12t/rz9mF9a6p9b76bFJZgls0+zXNHaV4TWPT6bteVm/BsC2FIvWY5rqyDJ8Fd6qixGcUffdir4nShc4dpbx6+A24o7SXaEavih7A1b7p5Q2GhifKV0oC/HeYwF/L0LVebWuTH2TTBvYpt2vadxduvWT4Z38wBxiPeA1pbv6Nj6HnbWOzk8AgFV3Rtl31GbVxWjhWtu5JDHy1N88OKYH21AY03a7mr5ZxLGKe8nFzWuzGGl7qdbXTf840wa2MGm/ZhH7cE7bCQD8/8To4f7ojTL81yAW4f7S/SWACHHxVyemtd2COgCwYmIUKqby9idx77G4EnMzxIhXjHwBAKyU68votWxb5e22AwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIB5/AcSWdp+quTo9AAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAbCAYAAACa9mScAAAA6ElEQVR4Xu2QMQtBYRSGj6KIsiirAZPBIBmUSSkpxeKX2O6PUBaL0WI1MbAoLAa/QPwL4j2dr8+9p3QvC8N96ql7z/nue8/5iEJCfkgMdmFFN4LQhmdYM+8cNodRe8KHHrzDqqovYFzV3vKAN1iCfbgmCeVpAsHjcgh/xOusYAem3Yf8SJGE8P5fkyQJGeoGyMGIeebVxiTrOjBh6hYOGakaf7Sh11otuCVZfwYzpm4pwj28kNzLFQ48J4iaJPfGP1yqnoXHrsOCbrjIwxNJ0Mdk4ZTkHsrw6G0Hg6c8wAncwYa3HfK/PAFijiOVZGlXVgAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAaCAYAAABozQZiAAAAt0lEQVR4XmNgGAVkgR1A/B+Iy4A4BIpXQcVakcSqoGIgGg7eAnElEp8FiNcwQBQqIYmDwG8gjoZxOIE4BiEHBjYMEEUgzejgKgOSgZpArIiQA4NyBojGf2jiIHAMiAXRBZHBAwaI5q1o4kQBmJNRAoYYwMEA0fgEiGXQ5AgCaQaEk0EGkQRAgQUKKBd0CUIAZBPIRrKcDLINZCtJASUJxDpAvIsB4t+pQBwAxKpAzIqkbhSMAtIAAKxUJHg501lGAAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAaCAYAAABhJqYYAAAAw0lEQVR4Xu2RPQ5BQRRGR5AQEhKFaG1BdEotEjYgGmugtwutTqHGDrRKCg2JnpZz38wkM9erFeIkp3jfN//PmN8ij3Xs4UB1HxSwgS9cqy6VnLGD57pIo4M3bOoijSnusaQL4YR33OAKz9iPRkAGx7jEosuuxp734whHV4TIRJ0lSCgXCTm4PMK/5ULlksmEiJYrhiqXTI4iP6fqwwo+se0DGAXZFrtBl6wywyxO8IIPY3fdGbtgRBlrxj6j/5b7/Pkybw2CJC8Sfy0wAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAaCAYAAAC3g3x9AAABPklEQVR4Xs2VvUoDURBGR4yVSAiKgqSxCgE7O1HfQAuxEHyANOkFKztrU4kIYmMh9jbiDzaiYOcDWKYINlpY6fc59+rNuJvdvS7igUMyM7sDs3eWFclmyiZ+wzO8g2ewamqFmYfbcATew4u+agTDGfHf0oBd+J7DFzipt6XTFr14F67DNbjlcnx2jOmly43pbek8wcUgHoKHsAebQZ4cmTiRE9HT9NRET5byv2cUngdxInwedZPbEB2NvyHj8NjkcsFx2dCOG82raMPS8CtSChOizW5sIZY50YYdW4hh0P6F8L1mnWsUrtsPOO6j6LiD3oZbuAOv4YOpfeIPIclWcF0FHsAZF2+KThMNx2QDNian8OqrGsGy9K/TG1wJ4sLMyveI/CRkHV5u+P5PS0mr5VmAqzYZyx7cdy6Z2j/nAzUiRJ2btgNWAAAAAElFTkSuQmCC>