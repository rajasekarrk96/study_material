import os

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum\_13_nlp'

LESSONS = [
    ("_13_01_nlp_foundations","_13_01_01_text_preprocessing_pipeline.md",1,1,"Text Preprocessing Pipeline","NLP Foundations",["spacy","nltk","tokenization","unicode","ftfy","sentence-split"],"beginner"),
    ("_13_01_nlp_foundations","_13_01_02_morphological_analysis.md",1,2,"Morphological Analysis","NLP Foundations",["stemming","lemmatization","pos-tagging","dependency-parsing","spacy-morph"],"beginner"),
    ("_13_01_nlp_foundations","_13_01_03_statistical_nlp_fundamentals.md",1,3,"Statistical NLP Fundamentals","NLP Foundations",["language-model","ngram","perplexity","smoothing","zipf","pmi"],"intermediate"),
    ("_13_01_nlp_foundations","_13_01_04_regular_expressions_nlp.md",1,4,"Regular Expressions for NLP","NLP Foundations",["regex","named-groups","information-extraction","re-module","regex-tokenization"],"beginner"),
    ("_13_01_nlp_foundations","_13_01_05_stopwords_vocabulary_corpus_statistics.md",1,5,"Stopwords Vocabulary Corpus Statistics","NLP Foundations",["stopwords","tfidf","bm25","ngram-features","vocabulary-truncation","counter"],"intermediate"),
    ("_13_01_nlp_foundations","_13_01_06_evaluation_metrics_nlp.md",1,6,"Evaluation Metrics for NLP","NLP Foundations",["bleu","rouge","bertscore","meteor","perplexity","mcc"],"intermediate"),
    ("_13_01_nlp_foundations","_13_01_07_nlp_libraries_overview.md",1,7,"NLP Libraries Overview","NLP Foundations",["spacy","nltk","huggingface","gensim","flair","stanza","textblob"],"beginner"),
    ("_13_02_text_representation","_13_02_01_bow_tfidf_applied.md",2,1,"BoW and TF-IDF Applied","Text Representation",["countvectorizer","tfidfvectorizer","sparse-matrix","feature-selection","bow-classification"],"intermediate"),
    ("_13_02_text_representation","_13_02_02_word2vec_glove.md",2,2,"Word2Vec and GloVe","Text Representation",["word2vec","glove","cbow","skip-gram","gensim","analogy","word-embeddings"],"intermediate"),
    ("_13_02_text_representation","_13_02_03_fasttext_subword_embeddings.md",2,3,"FastText and Subword Embeddings","Text Representation",["fasttext","subword","oov","bpe","character-ngram","fasttext-classify"],"intermediate"),
    ("_13_02_text_representation","_13_02_04_sentence_document_embeddings.md",2,4,"Sentence and Document Embeddings","Text Representation",["doc2vec","sbert","sentence-transformers","use","cosine-similarity","semantic-search"],"intermediate"),
    ("_13_02_text_representation","_13_02_05_contextual_embeddings_elmo.md",2,5,"Contextual Embeddings ELMo","Text Representation",["elmo","cove","ulmfit","allennlp","biLM","contextual"],"intermediate"),
    ("_13_02_text_representation","_13_02_06_subword_tokenization.md",2,6,"Subword Tokenization","Text Representation",["bpe","wordpiece","unigram-lm","sentencepiece","autotokenizer","special-tokens","vocab-size"],"intermediate"),
    ("_13_02_text_representation","_13_02_07_knowledge_graph_embeddings.md",2,7,"Knowledge Graph Embeddings","Text Representation",["transe","rotate","kgbert","pykeen","entity-linking","triple"],"advanced"),
    ("_13_02_text_representation","_13_02_08_multilingual_cross_lingual_embeddings.md",2,8,"Multilingual Cross-Lingual Embeddings","Text Representation",["mbert","xlm-r","labse","cross-lingual-transfer","xtreme","xglue"],"advanced"),
    ("_13_03_pretrained_language_models","_13_03_01_bert_architecture_pretraining.md",3,1,"BERT Architecture and Pretraining","Pretrained Language Models",["bert","mlm","nsp","cls-token","sep-token","encoder-only","wordpiece"],"intermediate"),
    ("_13_03_pretrained_language_models","_13_03_02_bert_variants_improvements.md",3,2,"BERT Variants and Improvements","Pretrained Language Models",["roberta","albert","distilbert","electra","deberta","bigbird","longformer","xlnet"],"intermediate"),
    ("_13_03_pretrained_language_models","_13_03_03_gpt_style_decoder_models.md",3,3,"GPT-Style Decoder Models","Pretrained Language Models",["gpt2","gpt3","llama","mistral","phi","opt","causal-lm","decoder-only"],"intermediate"),
    ("_13_03_pretrained_language_models","_13_03_04_encoder_decoder_models_t5_bart.md",3,4,"Encoder-Decoder Models T5 BART","Pretrained Language Models",["t5","bart","mt5","flan-t5","seq2seq","span-corruption","denoising"],"intermediate"),
    ("_13_03_pretrained_language_models","_13_03_05_efficient_transformers.md",3,5,"Efficient Transformers","Pretrained Language Models",["longformer","bigbird","reformer","linformer","mobilebert","tinybert","lsh-attention"],"advanced"),
    ("_13_03_pretrained_language_models","_13_03_06_tokenizer_deep_dive.md",3,6,"Tokenizer Deep Dive","Pretrained Language Models",["autotokenizer","encode-plus","padding","truncation","offset-mapping","fast-tokenizer"],"intermediate"),
    ("_13_03_pretrained_language_models","_13_03_07_finetuning_plms_huggingface.md",3,7,"Fine-Tuning PLMs with HuggingFace","Pretrained Language Models",["trainer","training-arguments","compute-metrics","evaluate","datasets","hyperparameter-search"],"intermediate"),
    ("_13_03_pretrained_language_models","_13_03_08_peft_lora_adapters_prompt_tuning.md",3,8,"PEFT LoRA Adapters Prompt Tuning","Pretrained Language Models",["lora","qlora","adapters","prefix-tuning","prompt-tuning","ia3","peft-library"],"intermediate"),
    ("_13_03_pretrained_language_models","_13_03_09_benchmarks_model_evaluation.md",3,9,"Benchmarks and Model Evaluation","Pretrained Language Models",["glue","superglue","squad","mmlu","hellaswag","arc","lm-evaluation-harness"],"intermediate"),
    ("_13_04_nlp_tasks_classification","_13_04_01_text_classification.md",4,1,"Text Classification","NLP Classification",["sequence-classification","setfit","zero-shot-classification","tfidf-lr","ag-news","sst2"],"intermediate"),
    ("_13_04_nlp_tasks_classification","_13_04_02_sentiment_analysis.md",4,2,"Sentiment Analysis","NLP Classification",["vader","absa","sentiwordnet","pyabsa","semeval","opinion-mining","aspect-extraction"],"intermediate"),
    ("_13_04_nlp_tasks_classification","_13_04_03_natural_language_inference.md",4,3,"Natural Language Inference","NLP Classification",["nli","entailment","snli","multinli","deberta-nli","zero-shot-nli"],"intermediate"),
    ("_13_04_nlp_tasks_classification","_13_04_04_topic_classification_detection.md",4,4,"Topic Classification and Detection","NLP Classification",["bertopic","top2vec","dynamic-topics","c-tfidf","topic-modeling"],"intermediate"),
    ("_13_04_nlp_tasks_classification","_13_04_05_document_classification_scale.md",4,5,"Document Classification at Scale","NLP Classification",["longformer","hierarchical","sliding-window","setfit","batch-inference"],"advanced"),
    ("_13_04_nlp_tasks_classification","_13_04_06_hate_speech_content_moderation.md",4,6,"Hate Speech and Content Moderation","NLP Classification",["perspective-api","detoxify","hatecheck","bias","adversarial","confidence-threshold"],"advanced"),
    ("_13_04_nlp_tasks_classification","_13_04_07_language_identification_detection.md",4,7,"Language Identification and Detection","NLP Classification",["langdetect","fasttext-lid","lingua","cld3","code-switching","script-detection"],"intermediate"),
    ("_13_05_sequence_labeling","_13_05_01_named_entity_recognition.md",5,1,"Named Entity Recognition","Sequence Labeling",["ner","iob","spacy-ner","bert-crf","flair","conll2003","span-ner","nested-ner"],"intermediate"),
    ("_13_05_sequence_labeling","_13_05_02_relation_extraction.md",5,2,"Relation Extraction","Sequence Labeling",["re","tacred","docred","entity-markers","zero-shot-re","openre"],"intermediate"),
    ("_13_05_sequence_labeling","_13_05_03_pos_tagging.md",5,3,"Part-of-Speech Tagging","Sequence Labeling",["pos","penn-treebank","universal-dependencies","hmm","crf","spacy-tag"],"intermediate"),
    ("_13_05_sequence_labeling","_13_05_04_chunking_shallow_parsing.md",5,4,"Chunking and Shallow Parsing","Sequence Labeling",["np-chunking","vp-chunking","srl","framenet","allennlp-srl","propbank"],"intermediate"),
    ("_13_05_sequence_labeling","_13_05_05_coreference_resolution.md",5,5,"Coreference Resolution","Sequence Labeling",["coref","ontonotes","allennlp-coref","spacy-coref","pronoun-resolution"],"advanced"),
    ("_13_05_sequence_labeling","_13_05_06_event_extraction.md",5,6,"Event Extraction","Sequence Labeling",["ace2005","trigger","argument","degree","joint-event-extraction","document-level"],"advanced"),
    ("_13_05_sequence_labeling","_13_05_07_biomedical_nlp.md",5,7,"Biomedical NLP","Sequence Labeling",["biobert","pubmedbert","scispacy","mimic","bc5cdr","medcat","deidentification"],"advanced"),
    ("_13_06_text_generation","_13_06_01_decoding_strategies.md",6,1,"Decoding Strategies","Text Generation",["beam-search","top-k","top-p","temperature","repetition-penalty","contrastive-search","generate"],"intermediate"),
    ("_13_06_text_generation","_13_06_02_machine_translation.md",6,2,"Machine Translation","Text Generation",["nmt","mbart","nllb","marianmt","sacrebleu","back-translation","domain-adaptation"],"intermediate"),
    ("_13_06_text_generation","_13_06_03_text_summarization.md",6,3,"Text Summarization","Text Generation",["pegasus","bart-summarization","extractive","abstractive","cnn-dailymail","xsum","rouge"],"intermediate"),
    ("_13_06_text_generation","_13_06_04_question_generation.md",6,4,"Question Generation","Text Generation",["t5-qg","kpew","squad-qg","difficulty-control","exam-generation"],"intermediate"),
    ("_13_06_text_generation","_13_06_05_controlled_text_generation.md",6,5,"Controlled Text Generation","Text Generation",["ctrl","plug-and-play","prefix-conditioning","outlines","grammar-constrained","style-transfer"],"advanced"),
    ("_13_06_text_generation","_13_06_06_text_data_augmentation.md",6,6,"Text Data Augmentation","Text Generation",["eda","back-translation","nlpaug","textattack","llm-augmentation","conditional-gen"],"intermediate"),
    ("_13_06_text_generation","_13_06_07_code_generation.md",6,7,"Code Generation","Text Generation",["codellama","starcoder2","deepseek-coder","humaneval","pass-at-k","fim","mbpp"],"intermediate"),
    ("_13_06_text_generation","_13_06_08_grammatical_error_correction.md",6,8,"Grammatical Error Correction","Text Generation",["gector","bea2019","errant","m2-scorer","language-tool","gec"],"intermediate"),
    ("_13_07_information_extraction","_13_07_01_extractive_question_answering.md",7,1,"Extractive Question Answering","Information Extraction",["squad","start-logits","end-logits","offset-mapping","exact-match","f1"],"intermediate"),
    ("_13_07_information_extraction","_13_07_02_open_domain_question_answering.md",7,2,"Open-Domain Question Answering","Information Extraction",["dpr","retriever-reader","haystack","triviaqa","natural-questions","multi-hop"],"advanced"),
    ("_13_07_information_extraction","_13_07_03_open_information_extraction.md",7,3,"Open Information Extraction","Information Extraction",["oie","openie","graphene","neural-oie","subject-predicate-object","kg-construction"],"intermediate"),
    ("_13_07_information_extraction","_13_07_04_document_level_information_extraction.md",7,4,"Document-Level Information Extraction","Information Extraction",["docred","atlop","cross-sentence-re","financial-ie","cuad","contract"],"advanced"),
    ("_13_07_information_extraction","_13_07_05_knowledge_base_population.md",7,5,"Knowledge Base Population","Information Extraction",["entity-linking","wikidata","sparql","slot-filling","kbqa","falcon"],"advanced"),
    ("_13_07_information_extraction","_13_07_06_fact_verification_claim_detection.md",7,6,"Fact Verification and Claim Detection","Information Extraction",["fever","claim-detection","hover","hallucination-detection","nli-fact-check"],"advanced"),
    ("_13_08_text_retrieval_and_search","_13_08_01_sparse_retrieval_bm25_tfidf.md",8,1,"Sparse Retrieval BM25 TF-IDF","Text Retrieval",["bm25","elasticsearch","inverted-index","rank-bm25","query-expansion","map","ndcg"],"intermediate"),
    ("_13_08_text_retrieval_and_search","_13_08_02_dense_retrieval.md",8,2,"Dense Retrieval","Text Retrieval",["dpr","bi-encoder","sentence-transformers","faiss","beir","ance","hard-negatives"],"intermediate"),
    ("_13_08_text_retrieval_and_search","_13_08_03_hybrid_retrieval.md",8,3,"Hybrid Retrieval","Text Retrieval",["rrf","splade","colbert","colbert-v2","cross-encoder","re-ranking"],"advanced"),
    ("_13_08_text_retrieval_and_search","_13_08_04_neural_re_ranking.md",8,4,"Neural Re-Ranking","Text Retrieval",["monot5","duot5","cross-encoder-rank","ms-marco","pointwise","pairwise"],"advanced"),
    ("_13_08_text_retrieval_and_search","_13_08_05_semantic_search_systems.md",8,5,"Semantic Search Systems","Text Retrieval",["semantic-search","chromadb","qdrant","pinecone","weaviate","metadata-filter"],"intermediate"),
    ("_13_08_text_retrieval_and_search","_13_08_06_question_answering_over_documents.md",8,6,"Question Answering over Documents","Text Retrieval",["haystack","farmreader","extractive-qa","generative-qa","fastapi"],"intermediate"),
    ("_13_08_text_retrieval_and_search","_13_08_07_passage_paragraph_retrieval.md",8,7,"Passage and Paragraph Retrieval","Text Retrieval",["chunking","text-splitter","sliding-window","late-chunking","parent-document-retriever"],"intermediate"),
    ("_13_09_conversational_ai","_13_09_01_dialogue_systems_architecture.md",9,1,"Dialogue Systems Architecture","Conversational AI",["task-oriented","open-domain","nlu","dialogue-manager","nlg","multiwoz"],"intermediate"),
    ("_13_09_conversational_ai","_13_09_02_intent_classification_slot_filling.md",9,2,"Intent Classification and Slot Filling","Conversational AI",["intent","slot","jointbert","rasa","snips","atis","zero-shot-intent"],"intermediate"),
    ("_13_09_conversational_ai","_13_09_03_dialogue_state_tracking.md",9,3,"Dialogue State Tracking","Conversational AI",["dst","trade","simpletod","in-context-dst","convlab3","joint-goal-accuracy"],"advanced"),
    ("_13_09_conversational_ai","_13_09_04_response_generation.md",9,4,"Response Generation","Conversational AI",["dialogpt","blenderbot","godel","persona","retrieval-response","diversity"],"intermediate"),
    ("_13_09_conversational_ai","_13_09_05_task_oriented_bot_rasa.md",9,5,"Task-Oriented Bot with Rasa","Conversational AI",["rasa","domain-yml","stories","custom-actions","rasa-train","rasa-run"],"intermediate"),
    ("_13_09_conversational_ai","_13_09_06_evaluation_conversational_systems.md",9,6,"Evaluation of Conversational Systems","Conversational AI",["usr","fed","human-eval","task-success","safety","bertscore-dialogue"],"intermediate"),
    ("_13_09_conversational_ai","_13_09_07_conversational_ai_with_llms.md",9,7,"Conversational AI with LLMs","Conversational AI",["system-prompts","few-shot-conv","openai-sdk","litellm","tool-use","nemo-guardrails"],"intermediate"),
    ("_13_10_industry_projects","_13_10_01_multiclass_news_classification_api.md",10,1,"Multi-Class News Classification API","Industry Projects",["ag-news","deberta","fastapi","mlflow","batch-inference","fine-tuning"],"advanced"),
    ("_13_10_industry_projects","_13_10_02_ner_re_pipeline_financial_documents.md",10,2,"NER and RE Pipeline for Financial Docs","Industry Projects",["finbert","edgar","ner","re","neo4j","knowledge-graph","fastapi"],"advanced"),
    ("_13_10_industry_projects","_13_10_03_multilingual_customer_support_bot.md",10,3,"Multilingual Customer Support Bot","Industry Projects",["xlm-r","mbert","rasa","language-id","mt","multilingual"],"advanced"),
    ("_13_10_industry_projects","_13_10_04_semantic_search_engine_research_papers.md",10,4,"Semantic Search Engine for Research Papers","Industry Projects",["arxiv","mpnet","qdrant","hybrid-search","re-ranking","recall-at-k"],"advanced"),
    ("_13_10_industry_projects","_13_10_05_abstractive_summarization_service.md",10,5,"Abstractive Summarization Service","Industry Projects",["bart","pegasus","length-control","batch-pipeline","fastapi","rouge-tracking"],"advanced"),
    ("_13_10_industry_projects","_13_10_06_end_to_end_document_qa_system.md",10,6,"End-to-End Document QA System","Industry Projects",["surya","sentence-transformers","haystack","faiss","ocr-to-qa","multi-doc"],"advanced"),
]

created = 0
skipped = 0
for folder, fname, mod, les, title, mod_title, tags, diff in LESSONS:
    dirpath = os.path.join(BASE, folder)
    os.makedirs(dirpath, exist_ok=True)
    fpath = os.path.join(dirpath, fname)
    if not os.path.exists(fpath):
        lid = f"13_{mod:02d}_{les:02d}"
        tag_str = ", ".join('"' + t + '"' for t in tags)
        content = f'---\nid: "{lid}"\ntitle: "{title}"\ncourse: "Natural Language Processing"\nmodule: {mod}\nmodule_title: "{mod_title}"\nlesson: {les}\nversion: "2.0"\ndifficulty: "{diff}"\nduration_minutes: 60\ntags: [{tag_str}]\nprerequisites: []\nlab_required: true\n---\n\n# {title}\n\n> **Status**: Syllabus stub. Full lesson content to be authored.\n\n---\n\n## Topics Covered\n\n*(See Phase 4 NLP Syllabus for full topic and subtopic breakdown)*\n\n---\n\n## Learning Objectives\n\n- To be defined during content authoring.\n'
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[CREATE] {fname}")
        created += 1
    else:
        print(f"[SKIP]   {fname}")
        skipped += 1

print(f"\nDONE - Created: {created}  Skipped: {skipped}  Total: {created+skipped}")
