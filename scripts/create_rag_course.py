import os
BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum\_15_rag_engineering'
LESSONS = [
    ("_15_01_rag_fundamentals","_15_01_01_what_is_rag_and_why.md",1,1,"What is RAG and Why It Matters","RAG Fundamentals",["rag-vs-fine-tuning","rag-taxonomy","naive-advanced-modular","use-cases","knowledge-cutoff"],"intermediate"),
    ("_15_01_rag_fundamentals","_15_01_02_naive_rag_architecture.md",1,2,"Naive RAG Architecture","RAG Fundamentals",["index-retrieve-generate","langchain-retrieval-qa","llama-index","failure-modes"],"intermediate"),
    ("_15_01_rag_fundamentals","_15_01_03_rag_frameworks_overview.md",1,3,"RAG Frameworks Overview","RAG Fundamentals",["langchain","llama-index","haystack","dspy","ragas","framework-comparison"],"intermediate"),
    ("_15_01_rag_fundamentals","_15_01_04_rag_data_flow_components.md",1,4,"RAG Data Flow and Components","RAG Fundamentals",["document-loader","splitter","embedding","vector-store","retriever","reranker","output-parser"],"intermediate"),
    ("_15_01_rag_fundamentals","_15_01_05_langchain_lcel_pipeline.md",1,5,"LangChain LCEL Pipeline","RAG Fundamentals",["lcel","runnable","chain","chat-prompt-template","str-output-parser","streaming"],"intermediate"),
    ("_15_01_rag_fundamentals","_15_01_06_llamaindex_core_concepts.md",1,6,"LlamaIndex Core Concepts","RAG Fundamentals",["document","node","vector-store-index","query-engine","node-postprocessor","response-synthesizer"],"intermediate"),
    ("_15_02_document_processing_and_chunking","_15_02_01_document_loaders.md",2,1,"Document Loaders","Document Processing",["pypdf","pdfplumber","pymupdf","unstructured","html-loader","csv-loader","metadata"],"intermediate"),
    ("_15_02_document_processing_and_chunking","_15_02_02_fixed_size_chunking.md",2,2,"Fixed-Size Chunking","Document Processing",["recursive-character-splitter","chunk-size","chunk-overlap","token-splitter","metadata-add"],"intermediate"),
    ("_15_02_document_processing_and_chunking","_15_02_03_semantic_sentence_chunking.md",2,3,"Semantic and Sentence Chunking","Document Processing",["sentence-splitter","semantic-chunker","propositions","late-chunking","chonkie","retrieval-recall"],"intermediate"),
    ("_15_02_document_processing_and_chunking","_15_02_04_structure_aware_chunking.md",2,4,"Structure-Aware Chunking","Document Processing",["markdown-splitter","html-splitter","code-splitter","table-aware","unstructured-elements"],"intermediate"),
    ("_15_02_document_processing_and_chunking","_15_02_05_hierarchical_multi_granularity_chunking.md",2,5,"Hierarchical Multi-Granularity Chunking","Document Processing",["parent-document-retriever","sentence-window","llama-index-hierarchical","multi-granularity","proposition-indexing"],"advanced"),
    ("_15_02_document_processing_and_chunking","_15_02_06_multimodal_document_processing.md",2,6,"Multimodal Document Processing","Document Processing",["pymupdf-images","table-extraction","ocr-surya","caption-generation","image-node","multimodal-index"],"advanced"),
    ("_15_02_document_processing_and_chunking","_15_02_07_chunking_evaluation_selection.md",2,7,"Chunking Evaluation and Selection","Document Processing",["retrieval-recall","context-precision","chunk-size-impact","ragas-chunking","decision-matrix"],"intermediate"),
    ("_15_03_embeddings_for_rag","_15_03_01_embedding_model_selection.md",3,1,"Embedding Model Selection","Embeddings for RAG",["mteb","bge-large","e5-mistral","nomic-embed","text-embedding-3","multilingual-e5"],"intermediate"),
    ("_15_03_embeddings_for_rag","_15_03_02_embedding_apis_local_models.md",3,2,"Embedding APIs and Local Models","Embeddings for RAG",["openai-embed","cohere-embed","sentence-transformers","fastembed","ollama-embed","cache-backed"],"intermediate"),
    ("_15_03_embeddings_for_rag","_15_03_03_late_interaction_colbert.md",3,3,"Late Interaction Models ColBERT","Embeddings for RAG",["colbert","maxsim","ragatouille","plaid","colbert-v2","bi-encoder-vs-colbert"],"advanced"),
    ("_15_03_embeddings_for_rag","_15_03_04_fine_tuning_embedding_models.md",3,4,"Fine-Tuning Embedding Models","Embeddings for RAG",["mnrl","triplet-loss","sft-embedding","hard-negative-mining","matryoshka","ndcg-recall"],"advanced"),
    ("_15_03_embeddings_for_rag","_15_03_05_sparse_hybrid_embeddings.md",3,5,"Sparse and Hybrid Embeddings","Embeddings for RAG",["bm25-sparse","splade","fastembed-sparse","hybrid-qdrant","weaviate-hybrid","alpha-weight"],"advanced"),
    ("_15_03_embeddings_for_rag","_15_03_06_embedding_storage_management.md",3,6,"Embedding Storage and Management","Embeddings for RAG",["dimension","float16","materialized","redis-cache","re-embedding","versioning","cost-estimation"],"intermediate"),
    ("_15_04_vector_databases","_15_04_01_vector_database_fundamentals.md",4,1,"Vector Database Fundamentals","Vector Databases",["hnsw","ivf","pq","lsh","ann","pre-filter","post-filter","cosine","l2"],"intermediate"),
    ("_15_04_vector_databases","_15_04_02_faiss_deep_dive.md",4,2,"FAISS Deep Dive","Vector Databases",["indexflatl2","indexivfpq","indexhnsw","gpu-faiss","write-read-index","langchain-faiss"],"intermediate"),
    ("_15_04_vector_databases","_15_04_03_chroma.md",4,3,"Chroma","Vector Databases",["chromadb","persistent-client","http-client","collections","metadata-filter","langchain-chroma"],"intermediate"),
    ("_15_04_vector_databases","_15_04_04_qdrant.md",4,4,"Qdrant","Vector Databases",["qdrant-client","collections","points","payloads","named-vectors","sparse-support","field-condition"],"intermediate"),
    ("_15_04_vector_databases","_15_04_05_pinecone.md",4,5,"Pinecone","Vector Databases",["pinecone-serverless","namespace","upsert-query","metadata-filter","langchain-pinecone","cost-model"],"intermediate"),
    ("_15_04_vector_databases","_15_04_06_weaviate.md",4,6,"Weaviate","Vector Databases",["weaviate-schema","text2vec","near-text","hybrid","generative-module","graphql","weaviate-v4"],"intermediate"),
    ("_15_04_vector_databases","_15_04_07_vector_db_selection_operations.md",4,7,"Vector DB Selection and Operations","Vector Databases",["selection-criteria","batch-upsert","hnsw-tuning","backup","monitoring","multi-tenancy"],"intermediate"),
    ("_15_05_advanced_retrieval","_15_05_01_hybrid_search.md",5,1,"Hybrid Search","Advanced Retrieval",["rrf","bm25-retriever","ensemble-retriever","qdrant-hybrid","weaviate-hybrid","alpha-tuning"],"intermediate"),
    ("_15_05_advanced_retrieval","_15_05_02_hyde_hypothetical_documents.md",5,2,"HyDE Hypothetical Document Embeddings","Advanced Retrieval",["hyde","hypothetical-answer","hyde-query-transform","query-gap","recall-comparison"],"advanced"),
    ("_15_05_advanced_retrieval","_15_05_03_query_transformation.md",5,3,"Query Transformation","Advanced Retrieval",["query-rewriting","multi-query","multiquery-retriever","step-back","query-decomposition","sub-question-engine"],"advanced"),
    ("_15_05_advanced_retrieval","_15_05_04_rag_fusion.md",5,4,"RAG-Fusion","Advanced Retrieval",["rag-fusion","n-queries","rrf-fusion","diversity","recall-improvement"],"advanced"),
    ("_15_05_advanced_retrieval","_15_05_05_multi_hop_iterative_retrieval.md",5,5,"Multi-Hop and Iterative Retrieval","Advanced Retrieval",["ircot","react-retrieval","multi-step","hotpotqa","2wiki","graph-traversal"],"advanced"),
    ("_15_05_advanced_retrieval","_15_05_06_metadata_filtering_routing.md",5,6,"Metadata Filtering and Routing","Advanced Retrieval",["self-query-retriever","attribute-info","time-filter","multi-source","router-query-engine"],"intermediate"),
    ("_15_05_advanced_retrieval","_15_05_07_contextual_retrieval.md",5,7,"Contextual Retrieval","Advanced Retrieval",["contextual-retrieval","chunk-context","contextual-compression","llm-chain-extractor","embeddings-filter"],"advanced"),
    ("_15_05_advanced_retrieval","_15_05_08_re_ranking.md",5,8,"Re-Ranking","Advanced Retrieval",["cross-encoder","ms-marco","flashrank","cohere-rerank","colbert-rerank","rankllm","compression-retriever"],"intermediate"),
    ("_15_06_generation_and_augmentation","_15_06_01_rag_prompt_templates.md",6,1,"RAG Prompt Templates","Generation and Augmentation",["system-prompt","context-format","citation-instruction","no-answer","few-shot-rag","multilingual"],"intermediate"),
    ("_15_06_generation_and_augmentation","_15_06_02_response_synthesis_strategies.md",6,2,"Response Synthesis Strategies","Generation and Augmentation",["stuff","map-reduce","refine","map-rerank","tree-summarize","compact","token-limit"],"intermediate"),
    ("_15_06_generation_and_augmentation","_15_06_03_streaming_rag.md",6,3,"Streaming RAG","Generation and Augmentation",["chain-stream","astream","fastapi-sse","websocket-stream","token-buffer","latency"],"intermediate"),
    ("_15_06_generation_and_augmentation","_15_06_04_citations_source_attribution.md",6,4,"Citations and Source Attribution","Generation and Augmentation",["inline-citations","citation-extraction","faithfulness-check","citation-query-engine","attributed-qa"],"intermediate"),
    ("_15_06_generation_and_augmentation","_15_06_05_conversational_rag_memory.md",6,5,"Conversational RAG with Memory","Generation and Augmentation",["conv-retrieval-chain","history-aware-retriever","runnable-with-history","condensation","redis-memory"],"intermediate"),
    ("_15_06_generation_and_augmentation","_15_06_06_corrective_rag_self_rag.md",6,6,"Corrective RAG and Self-RAG","Generation and Augmentation",["self-rag","isrel-issup-isuse","crag","tavily-fallback","langgraph-crag","answer-correctness"],"advanced"),
    ("_15_07_rag_evaluation","_15_07_01_rag_evaluation_dimensions.md",7,1,"RAG Evaluation Dimensions","RAG Evaluation",["context-precision","context-recall","faithfulness","answer-relevance","end-to-end","cost"],"intermediate"),
    ("_15_07_rag_evaluation","_15_07_02_ragas_framework.md",7,2,"RAGAS Framework","RAG Evaluation",["ragas-evaluate","faithfulness","answer-relevancy","context-precision","context-recall","ci-integration"],"intermediate"),
    ("_15_07_rag_evaluation","_15_07_03_trulens_evaluation.md",7,3,"TruLens Evaluation","RAG Evaluation",["trulens","truchain","trullama","feedback","rag-triad","dashboard","leaderboard"],"intermediate"),
    ("_15_07_rag_evaluation","_15_07_04_deepeval.md",7,4,"DeepEval","RAG Evaluation",["deepeval","geval","hallucination-metric","faithfulness-metric","pytest-plugin","github-actions"],"intermediate"),
    ("_15_07_rag_evaluation","_15_07_05_building_rag_test_dataset.md",7,5,"Building a RAG Test Dataset","RAG Evaluation",["synthetic-qa","testset-generator","giskard","question-types","human-annotation","dataset-format"],"intermediate"),
    ("_15_07_rag_evaluation","_15_07_06_rag_experimentation_ab_testing.md",7,6,"RAG Experimentation and A/B Testing","RAG Evaluation",["mlflow-rag","langsmith","langfuse","ab-design","statistical-significance","iterative-improvement"],"intermediate"),
    ("_15_08_production_rag_systems","_15_08_01_graph_rag.md",8,1,"Graph RAG","Production RAG",["graphrag","leiden","community-summary","neo4j","langchain-neo4j","knowledge-graph-index"],"advanced"),
    ("_15_08_production_rag_systems","_15_08_02_multimodal_rag.md",8,2,"Multimodal RAG","Production RAG",["clip-retrieval","table-rag","pdf-figures","multimodal-vector-index","gpt4o-vision","audio-rag"],"advanced"),
    ("_15_08_production_rag_systems","_15_08_03_long_context_rag.md",8,3,"Long Context RAG","Production RAG",["128k-context","gemini-1.5","lost-in-middle","hybrid-approach","longrag","position-effects"],"advanced"),
    ("_15_08_production_rag_systems","_15_08_04_agentic_rag.md",8,4,"Agentic RAG","Production RAG",["agentic-rag","react-loop","retriever-tool","react-agent","multi-retriever","self-correction"],"advanced"),
    ("_15_08_production_rag_systems","_15_08_05_rag_observability.md",8,5,"RAG Observability","Production RAG",["langfuse","langsmith","phoenix-arize","trace-components","token-usage","feedback","alerting"],"intermediate"),
    ("_15_08_production_rag_systems","_15_08_06_rag_security_guardrails.md",8,6,"RAG Security and Guardrails","Production RAG",["prompt-injection","input-sanitization","nemo-guardrails","guardrails-ai","pii-redact","rate-limiting"],"advanced"),
    ("_15_08_production_rag_systems","_15_08_07_scaling_optimizing_rag.md",8,7,"Scaling and Optimizing RAG","Production RAG",["async-retrieval","gptcache","semantic-cache","index-sharding","pre-filtering","cost-optimization"],"advanced"),
    ("_15_09_industry_projects","_15_09_01_enterprise_document_qa_system.md",9,1,"Enterprise Document Q&A System","Industry Projects",["langchain","qdrant","openai","hybrid-retrieval","conversational","fastapi","langfuse"],"advanced"),
    ("_15_09_industry_projects","_15_09_02_codebase_qa_assistant.md",9,2,"Codebase Q&A Assistant","Industry Projects",["git-loader","code-splitter","codellama","function-level","github-integration"],"advanced"),
    ("_15_09_industry_projects","_15_09_03_research_paper_assistant.md",9,3,"Research Paper Assistant","Industry Projects",["arxiv","semantic-scholar","multi-paper","graphrag","multi-hop","streaming-api"],"advanced"),
    ("_15_09_industry_projects","_15_09_04_customer_support_rag_bot.md",9,4,"Customer Support RAG Bot","Industry Projects",["weaviate","claude","multi-language","session-memory","escalation","ragas-csat"],"advanced"),
    ("_15_09_industry_projects","_15_09_05_financial_report_rag.md",9,5,"Financial Report RAG","Industry Projects",["edgar","haystack","table-transformer","numerical-qa","self-rag","citation-page"],"advanced"),
    ("_15_09_industry_projects","_15_09_06_graphrag_knowledge_platform_capstone.md",9,6,"GraphRAG Knowledge Platform Capstone","Industry Projects",["graphrag","neo4j","vllm","llama-index","entity-extraction","ragas","trulens"],"advanced"),
]
created = 0
skipped = 0
for folder, fname, mod, les, title, mod_title, tags, diff in LESSONS:
    dirpath = os.path.join(BASE, folder)
    os.makedirs(dirpath, exist_ok=True)
    fpath = os.path.join(dirpath, fname)
    if not os.path.exists(fpath):
        lid = f"15_{mod:02d}_{les:02d}"
        tag_str = ", ".join('"'+t+'"' for t in tags)
        content = f'---\nid: "{lid}"\ntitle: "{title}"\ncourse: "RAG Engineering"\nmodule: {mod}\nmodule_title: "{mod_title}"\nlesson: {les}\nversion: "2.0"\ndifficulty: "{diff}"\nduration_minutes: 60\ntags: [{tag_str}]\nprerequisites: []\nlab_required: true\n---\n\n# {title}\n\n> **Status**: Syllabus stub. Full lesson content to be authored.\n\n---\n\n## Topics Covered\n\n*(See Phase 6 RAG Syllabus for full topic and subtopic breakdown)*\n\n---\n\n## Learning Objectives\n\n- To be defined during content authoring.\n'
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[CREATE] {fname}")
        created += 1
    else:
        print(f"[SKIP]   {fname}")
        skipped += 1
print(f"\nDONE - Created: {created}  Skipped: {skipped}  Total: {created+skipped}")
