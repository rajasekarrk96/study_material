# Phase 4: Natural Language Processing — Enterprise Syllabus
## Learning OS Enterprise Standard | Curriculum Architecture v2.0

**Classification**: Chief Curriculum Architect — Syllabus Design Document  
**Phase**: 4 of 8  
**Domain**: Natural Language Processing  
**Required Previous Phases**: Phase 1 (ML), Phase 2 (DL), Phase 3 (CV)  
**Folder Root**: `docs/curriculum/_13_nlp/`  
**Last Updated**: 2026-07-28

---

## Dependency Graph

```
_11_deep_learning   (Phase 2)
    ├── _12_computer_vision  (Phase 3)
    └── _13_nlp  ◄── THIS PHASE
```

Cross-phase reuse nodes (zero duplication):
- `DL.11_07` Attention & Transformers → fully extended here (BERT, GPT, T5)
- `DL.11_06_04` Seq2Seq → extended for MT, summarization
- `DL.11_06_05` RNN Attention → predecessor to Transformer attention
- `DL.11_09_06` CLIP text encoder → extended in multimodal NLP
- `CV.12_05` OCR & Document → NLP downstream pipeline
- `ML.10_07_10` Topic Modeling → extended with neural methods
- `ML.10_03_04` Encoding → TF-IDF, vocabulary encoding reused

---

## Skills Gained (This Phase)

- Build complete NLP pipelines from text preprocessing to deployed models
- Implement and fine-tune BERT, RoBERTa, DeBERTa for classification/NER/QA
- Build and fine-tune GPT-style models for text generation
- Implement machine translation and summarization systems
- Apply PEFT techniques (LoRA, Adapters) for efficient NLP fine-tuning
- Build information extraction pipelines (NER, RE, event extraction)
- Engineer text retrieval systems with BM25 and dense retrieval
- Build and evaluate dialogue and conversational systems
- Deploy NLP models as scalable production APIs
- Evaluate language models with standard benchmarks

---

## Course Structure

```
_13_nlp/
├── _13_01_nlp_foundations/
├── _13_02_text_representation/
├── _13_03_pretrained_language_models/
├── _13_04_nlp_tasks_classification/
├── _13_05_sequence_labeling/
├── _13_06_text_generation/
├── _13_07_information_extraction/
├── _13_08_text_retrieval_and_search/
├── _13_09_conversational_ai/
└── _13_10_industry_projects/
```

---

## MODULE 01 — NLP Foundations

**Folder**: `_13_01_nlp_foundations/`  
**Lesson Count**: 7  
**Learning Order**: 1st

### Lessons

#### Lesson 01.01 — Text Preprocessing Pipeline
**File**: `_13_01_01_text_preprocessing_pipeline.md`

| Topics | Subtopics |
|---|---|
| Unicode and encoding | UTF-8, ASCII, encoding errors, `ftfy` |
| Sentence tokenization | `nltk.sent_tokenize`, `spacy`, regex |
| Word tokenization | Whitespace, regex, `nltk.word_tokenize` |
| Case normalization | Lowercasing, truecasing |
| Punctuation and noise | HTML tags, URLs, mentions removal |
| `spaCy` pipeline | `nlp(text)`, `doc.sents`, `doc.tokens` |
| Batch processing | `nlp.pipe`, multiprocessing |

---

#### Lesson 01.02 — Morphological Analysis
**File**: `_13_01_02_morphological_analysis.md`

| Topics | Subtopics |
|---|---|
| Stemming | Porter, Snowball, Lancaster — `nltk.stem` |
| Lemmatization | `spaCy`, `nltk.WordNetLemmatizer` |
| POS tagging | `spaCy.pos_`, Penn Treebank tagset |
| Dependency parsing | `spaCy.dep_`, head, children |
| Morphological features | Number, tense, case, gender |
| When to stem vs lemmatize | Information retrieval vs NLU |

---

#### Lesson 01.03 — Statistical NLP Fundamentals
**File**: `_13_01_03_statistical_nlp_fundamentals.md`

| Topics | Subtopics |
|---|---|
| Language model definition | P(w₁, w₂, ..., wₙ) |
| N-gram language models | Unigram, bigram, trigram, MLE |
| Perplexity | Evaluation metric for LMs |
| Smoothing | Laplace, Kneser-Ney, Good-Turing |
| Zipf's law | Power-law word frequency |
| Pointwise Mutual Information | PMI, collocations |
| `nltk.collocations` | Bigram/trigram association measures |

---

#### Lesson 01.04 — Regular Expressions for NLP
**File**: `_13_01_04_regular_expressions_nlp.md`

| Topics | Subtopics |
|---|---|
| Regex syntax | Anchors, quantifiers, groups, lookahead |
| `re` module | `re.findall`, `re.sub`, `re.compile` |
| Named groups | `(?P<name>...)` |
| Information extraction patterns | Date, phone, email, currency |
| Regex for tokenization | Custom tokenizer patterns |
| `regex` library | Unicode-aware, possessive quantifiers |

---

#### Lesson 01.05 — Stopwords, Vocabulary, and Corpus Statistics
**File**: `_13_01_05_stopwords_vocabulary_corpus_statistics.md`

| Topics | Subtopics |
|---|---|
| Stopword removal | `nltk.corpus.stopwords`, custom lists |
| Vocabulary | `Counter`, `FreqDist`, type-token ratio |
| Corpus statistics | Document frequency, term frequency |
| TF-IDF | `sklearn.TfidfVectorizer`, `TfidfTransformer` |
| BM25 | `rank_bm25`, Okapi BM25 formula |
| N-gram features | `ngram_range=(1,2)`, character n-grams |
| Vocabulary truncation | `max_features`, `min_df`, `max_df` |

---

#### Lesson 01.06 — Evaluation Metrics for NLP
**File**: `_13_01_06_evaluation_metrics_nlp.md`

| Topics | Subtopics |
|---|---|
| Classification metrics | Accuracy, F1, precision, recall (reuse from ML) |
| BLEU | Machine translation evaluation |
| ROUGE | Summarization evaluation (R-1, R-2, R-L) |
| METEOR | Better word alignment than BLEU |
| BERTScore | Semantic similarity via BERT embeddings |
| Perplexity | Language model evaluation |
| MCC for NLP | Imbalanced text classification |
| Human evaluation | Likert scales, pairwise preference |

---

#### Lesson 01.07 — NLP Libraries Overview
**File**: `_13_01_07_nlp_libraries_overview.md`

| Topics | Subtopics |
|---|---|
| `spaCy` | Industrial-strength NLP, pipelines |
| `NLTK` | Teaching + research, broad coverage |
| `HuggingFace Transformers` | Model hub, `pipeline()` API |
| `Gensim` | Topic modeling, Word2Vec |
| `TextBlob` | Simple API for beginners |
| `stanza` | Stanford NLP, multilingual |
| `flair` | Sequence labeling, contextual embeddings |
| Comparison | Use case selection guide |

---

## MODULE 02 — Text Representation

**Folder**: `_13_02_text_representation/`  
**Lesson Count**: 8  
**Learning Order**: 2nd

### Lessons

#### Lesson 02.01 — Bag of Words and TF-IDF (Applied)
**File**: `_13_02_01_bow_tfidf_applied.md`

| Topics | Subtopics |
|---|---|
| `CountVectorizer` | `fit_transform`, vocabulary mapping |
| `TfidfVectorizer` | `sublinear_tf`, `use_idf`, `norm` |
| Sparse matrices | CSR format, memory efficiency |
| Feature selection from BoW | Chi2, mutual info, variance threshold |
| BoW for classification | Naive Bayes, Logistic Regression on BoW |
| Limitations | No word order, no semantics |

---

#### Lesson 02.02 — Word2Vec and GloVe
**File**: `_13_02_02_word2vec_glove.md`

| Topics | Subtopics |
|---|---|
| Word embeddings | Dense vectors, semantic similarity |
| Word2Vec | CBOW, Skip-gram, negative sampling |
| GloVe | Global co-occurrence matrix factorization |
| `gensim.models.Word2Vec` | Training on custom corpus |
| Pretrained embeddings | `gensim-data`, Wikipedia+Gigaword |
| Analogy tasks | King - Man + Woman = Queen |
| Evaluation | Word similarity, analogy benchmark |
| OOV handling | Subword extensions preview |

---

#### Lesson 02.03 — FastText and Subword Embeddings
**File**: `_13_02_03_fasttext_subword_embeddings.md`

| Topics | Subtopics |
|---|---|
| FastText | Character n-gram subwords |
| OOV advantage | Compose any word from subwords |
| `fasttext` library | `train_unsupervised`, `get_word_vector` |
| FastText for classification | `train_supervised`, multilingual |
| Byte-Pair Encoding | BPE preview (used in GPT tokenizers) |
| Evaluation | Morphologically rich language tasks |

---

#### Lesson 02.04 — Sentence and Document Embeddings
**File**: `_13_02_04_sentence_document_embeddings.md`

| Topics | Subtopics |
|---|---|
| Averaging word vectors | Simple baseline |
| Doc2Vec | `gensim.models.Doc2Vec`, PV-DM, PV-DBOW |
| Universal Sentence Encoder | `tensorflow_hub` |
| Sentence-BERT (SBERT) | `sentence-transformers`, pooling strategies |
| `SentenceTransformer` | `encode()`, `semantic_search()` |
| Embedding pooling | CLS, mean, max pooling |
| Cosine similarity | `util.cos_sim`, semantic search |

---

#### Lesson 02.05 — Contextual Embeddings (ELMo, Pre-BERT)
**File**: `_13_02_05_contextual_embeddings_elmo.md`

| Topics | Subtopics |
|---|---|
| Why static embeddings fail | "bank" disambiguation |
| ELMo | Bidirectional LM, character CNN |
| CoVe | Context Vectors, MT encoder features |
| `allennlp` | ELMo integration |
| ULMFiT | Universal Language Model Fine-Tuning |
| Historical significance | Transition to Transformer era |

---

#### Lesson 02.06 — Subword Tokenization
**File**: `_13_02_06_subword_tokenization.md`

| Topics | Subtopics |
|---|---|
| Why subword | OOV, morphology, multilingual |
| BPE | Byte-Pair Encoding, merge rules |
| WordPiece | BERT tokenizer, likelihood-based |
| Unigram LM | SentencePiece, probabilistic |
| `tokenizers` library | Hugging Face tokenizers, Rust backend |
| `AutoTokenizer` | `encode`, `decode`, `batch_encode_plus` |
| Special tokens | [CLS], [SEP], [PAD], [MASK], <s>, </s> |
| Vocabulary size | Tradeoffs: 30K vs 50K vs 100K |

---

#### Lesson 02.07 — Knowledge Graph Embeddings
**File**: `_13_02_07_knowledge_graph_embeddings.md`

| Topics | Subtopics |
|---|---|
| Knowledge graphs | Entities, relations, triples (h, r, t) |
| TransE | Translational embeddings |
| RotatE | Rotation in complex space |
| KGBERT | BERT for KG completion |
| `pykeen` | KGE training framework |
| Downstream use | Entity linking, slot filling |

---

#### Lesson 02.08 — Multilingual and Cross-Lingual Embeddings
**File**: `_13_02_08_multilingual_cross_lingual_embeddings.md`

| Topics | Subtopics |
|---|---|
| mBERT | Multilingual BERT, 104 languages |
| XLM-R | Cross-lingual RoBERTa, Common Crawl |
| LaBSE | Language-agnostic BERT sentence embeddings |
| `sentence-transformers` multilingual | `paraphrase-multilingual-mpnet-base-v2` |
| Cross-lingual transfer | Zero-shot transfer to new languages |
| XTREME / XGLUE | Cross-lingual benchmark |

---

## MODULE 03 — Pretrained Language Models

**Folder**: `_13_03_pretrained_language_models/`  
**Lesson Count**: 9  
**Learning Order**: 3rd

### Lessons

#### Lesson 03.01 — BERT Architecture and Pretraining
**File**: `_13_03_01_bert_architecture_pretraining.md`

| Topics | Subtopics |
|---|---|
| BERT architecture | Encoder-only Transformer, 12/24 layers |
| Pretraining tasks | MLM (Masked Language Model), NSP |
| Input format | [CLS] + tokens + [SEP], token type IDs |
| Positional embeddings | Learned absolute, 512 max length |
| `BertModel` | `last_hidden_state`, `pooler_output` |
| BERT variants | BERT-base, BERT-large, cased/uncased |
| Pretraining data | BooksCorpus + English Wikipedia |

---

#### Lesson 03.02 — BERT Variants and Improvements
**File**: `_13_03_02_bert_variants_improvements.md`

| Topics | Subtopics |
|---|---|
| RoBERTa | Removes NSP, dynamic masking, more data |
| ALBERT | Parameter sharing, SOP task |
| DistilBERT | 6-layer distilled, 40% smaller, 60% faster |
| ELECTRA | Generator-Discriminator pretraining |
| DeBERTa / DeBERTa-v3 | Disentangled attention, SOTA on GLUE |
| BigBird | Sparse attention for long sequences |
| Longformer | Sliding window + global attention |
| XLNet | Permutation language model, autoregressive |

---

#### Lesson 03.03 — GPT-Style Decoder Models
**File**: `_13_03_03_gpt_style_decoder_models.md`

| Topics | Subtopics |
|---|---|
| GPT-1/2 architecture | Decoder-only, causal LM |
| GPT-2 | 1.5B params, zero-shot stories |
| GPT-3 / GPT-4 | Few-shot ICL, scale hypothesis |
| `GPT2LMHeadModel` | `generate()`, `past_key_values` |
| OPT | Meta open decoder |
| LLaMA 1/2/3 | Meta open-weight LLM |
| Mistral | Grouped query attention, sliding window |
| Phi-2/3 | Small, data-efficient models |

---

#### Lesson 03.04 — Encoder-Decoder Models (T5, BART)
**File**: `_13_03_04_encoder_decoder_models_t5_bart.md`

| Topics | Subtopics |
|---|---|
| T5 | Text-to-Text Transfer Transformer |
| T5 pretraining | Span corruption, sentinel tokens |
| BART | Denoising autoencoder pretraining |
| mT5 | Multilingual T5 |
| FLAN-T5 | Instruction-tuned T5 |
| `T5ForConditionalGeneration` | `generate()`, `encoder_outputs` |
| `BartForConditionalGeneration` | Same interface |
| Seq2seq tasks | Translation, summarization, QA |

---

#### Lesson 03.05 — Efficient Transformers
**File**: `_13_03_05_efficient_transformers.md`

| Topics | Subtopics |
|---|---|
| Attention complexity | O(n²) bottleneck |
| Longformer | Sliding window + global tokens |
| BigBird | Random + window + global attention |
| Reformer | LSH attention, reversible layers |
| Linformer | Low-rank attention approximation |
| MobileBERT | Bottleneck layers, inverted bottleneck |
| TinyBERT | 4-layer, layer mapping distillation |
| Efficient attention survey | Accuracy vs speed vs memory tradeoffs |

---

#### Lesson 03.06 — Tokenizer Deep Dive
**File**: `_13_03_06_tokenizer_deep_dive.md`

| Topics | Subtopics |
|---|---|
| `AutoTokenizer` | `from_pretrained`, `save_pretrained` |
| `encode` vs `encode_plus` vs `batch_encode_plus` | Return types |
| Padding strategies | `padding="longest"`, `padding="max_length"` |
| Truncation | `truncation=True`, `max_length` |
| `DataCollatorWithPadding` | Dynamic batching |
| Fast vs slow tokenizers | Rust backend, offset mapping |
| Custom tokenizer training | `BpeTrainer`, `WordPieceTrainer` |
| Token alignment | `word_ids()`, offset mapping for NER |

---

#### Lesson 03.07 — Fine-Tuning PLMs with HuggingFace
**File**: `_13_03_07_finetuning_plms_huggingface.md`

| Topics | Subtopics |
|---|---|
| `Trainer` API | `TrainingArguments`, `compute_metrics` |
| `AutoModelForSequenceClassification` | Head replacement |
| `AutoModelForTokenClassification` | NER fine-tuning |
| `AutoModelForQuestionAnswering` | Extractive QA |
| `AutoModelForSeq2SeqLM` | Summarization, translation |
| `evaluate` library | `load("metric")`, batch eval |
| Dataset preparation | `datasets` library, `map()`, `DatasetDict` |
| Hyperparameter search | `Trainer` + Optuna integration |

---

#### Lesson 03.08 — PEFT: LoRA, Adapters, Prompt Tuning
**File**: `_13_03_08_peft_lora_adapters_prompt_tuning.md`

| Topics | Subtopics |
|---|---|
| LoRA | Low-Rank Adaptation, frozen weights + AB matrices |
| `peft.LoraConfig` | `r`, `lora_alpha`, `target_modules`, `lora_dropout` |
| `get_peft_model` | Wrapping any PLM |
| QLoRA | 4-bit quantized LoRA, `bitsandbytes` |
| Adapters | Bottleneck layers, `AdapterHub` |
| Prefix Tuning | Learnable prefix tokens |
| Prompt Tuning | Learnable soft prompts |
| IA³ | Few-parameter rescaling |
| Comparison table | Params, memory, task performance |

---

#### Lesson 03.09 — Benchmarks and Model Evaluation
**File**: `_13_03_09_benchmarks_model_evaluation.md`

| Topics | Subtopics |
|---|---|
| GLUE | General Language Understanding Evaluation |
| SuperGLUE | Harder tasks: BoolQ, CB, MultiRC, WiC |
| SQuAD 1.1 / 2.0 | Extractive QA benchmark |
| RACE | Multi-choice reading comprehension |
| MMLU | 57-subject knowledge evaluation |
| HellaSwag | Commonsense completion |
| ARC | Grade-school reasoning |
| `lm-evaluation-harness` | Standard evaluation framework |
| LMSys Chatbot Arena | Human preference leaderboard |

---

## MODULE 04 — NLP Tasks: Classification

**Folder**: `_13_04_nlp_tasks_classification/`  
**Lesson Count**: 7  
**Learning Order**: 4th

### Lessons

#### Lesson 04.01 — Text Classification
**File**: `_13_04_01_text_classification.md`

| Topics | Subtopics |
|---|---|
| Task types | Binary, multi-class, multi-label |
| Feature-based | TF-IDF + Logistic Regression baseline |
| BERT fine-tuning | `AutoModelForSequenceClassification` |
| SetFit | Few-shot with sentence transformers |
| Zero-shot | `pipeline("zero-shot-classification")` |
| Datasets | AG News, SST-2, IMDb, 20 Newsgroups |
| Evaluation | Accuracy, macro F1, per-class breakdown |

---

#### Lesson 04.02 — Sentiment Analysis
**File**: `_13_04_02_sentiment_analysis.md`

| Topics | Subtopics |
|---|---|
| Lexicon-based | VADER, TextBlob, SentiWordNet |
| Fine-grained sentiment | Aspect-Based Sentiment Analysis (ABSA) |
| `VADER` | Rule-based, social media |
| BERT for sentiment | SST-2, Twitter fine-tuned |
| Aspect extraction | SemEval ABSA tasks |
| Opinion mining | Target, aspect, polarity triplet |
| `pyabsa` | ABSA toolkit |

---

#### Lesson 04.03 — Natural Language Inference
**File**: `_13_04_03_natural_language_inference.md`

| Topics | Subtopics |
|---|---|
| NLI task | Entailment / Contradiction / Neutral |
| SNLI / MultiNLI | Standard benchmarks |
| `cross-encoder/nli-deberta-v3` | State-of-the-art NLI model |
| NLI for zero-shot | Hypothesis template classification |
| Textual entailment applications | Fact checking, QA, summarization eval |

---

#### Lesson 04.04 — Topic Classification and Detection
**File**: `_13_04_04_topic_classification_detection.md`

| Topics | Subtopics |
|---|---|
| Multi-label topic | One document, multiple topics |
| BERTopic | Transformer + c-TF-IDF |
| Top2Vec | Jointly embed docs and words |
| Neural LDA | Combining VAE with LDA |
| Dynamic topic models | Tracking topics over time |
| `bertopic` | `fit_transform`, `get_topic_info`, visualization |

---

#### Lesson 04.05 — Document Classification at Scale
**File**: `_13_04_05_document_classification_scale.md`

| Topics | Subtopics |
|---|---|
| Long document challenge | BERT 512 token limit |
| Hierarchical model | Sentence → document aggregation |
| Longformer for classification | `LongformerForSequenceClassification` |
| Sliding window | Chunk + aggregate predictions |
| SetFit for few-shot | Sample efficiency |
| Production pipeline | Batch inference, async API |

---

#### Lesson 04.06 — Hate Speech and Content Moderation
**File**: `_13_04_06_hate_speech_content_moderation.md`

| Topics | Subtopics |
|---|---|
| Hate speech detection | HatEval, OffComEval datasets |
| Toxicity scoring | Perspective API, `detoxify` |
| Multi-label toxicity | Toxic, severe toxic, obscene, threat |
| Bias in classifiers | Lexical shortcuts, dialect bias |
| Adversarial robustness | HateCheck evaluation suite |
| Production considerations | Confidence thresholds, human review |

---

#### Lesson 04.07 — Language Identification and Detection
**File**: `_13_04_07_language_identification_detection.md`

| Topics | Subtopics |
|---|---|
| Language ID task | 100+ language identification |
| `langdetect` | Port of Google's langdetect |
| `fasttext` LID | 176 languages, high speed |
| `lingua-py` | High accuracy, low false positives |
| Code-switching | Mixed-language text handling |
| `cld3` | Google Compact Language Detector |
| Script detection | Latin, Cyrillic, CJK, Arabic |

---

## MODULE 05 — Sequence Labeling

**Folder**: `_13_05_sequence_labeling/`  
**Lesson Count**: 7  
**Learning Order**: 5th

### Lessons

#### Lesson 05.01 — Named Entity Recognition (NER)
**File**: `_13_05_01_named_entity_recognition.md`

| Topics | Subtopics |
|---|---|
| NER task | PER, ORG, LOC, DATE, MISC labels |
| IOB/BIO tagging | Inside, Outside, Beginning |
| `spaCy` NER | `doc.ents`, `ent.label_`, `ent.text` |
| BERT + CRF | `BertForTokenClassification` + CRF head |
| `flair` NER | `SequenceTagger`, Flair embeddings |
| CoNLL-2003 | Standard NER benchmark |
| Span-based NER | SpanBERT, non-BIO approach |
| Nested NER | Overlapping span handling |

---

#### Lesson 05.02 — Relation Extraction
**File**: `_13_05_02_relation_extraction.md`

| Topics | Subtopics |
|---|---|
| RE task | Given (entity1, entity2) → relation |
| Supervised RE | SemEval 2010 Task 8 dataset |
| BERT for RE | Entity markers, typed entity markers |
| `TACRED` / `DocRED` | Large-scale RE datasets |
| Zero-shot RE | Template-based, NLI approach |
| `OpenRE` | Open information extraction |

---

#### Lesson 05.03 — Part-of-Speech Tagging
**File**: `_13_05_03_pos_tagging.md`

| Topics | Subtopics |
|---|---|
| POS tagsets | Penn Treebank, Universal Dependencies |
| `spaCy` POS | `token.pos_`, `token.tag_` |
| HMM tagger | Forward-backward, Viterbi |
| CRF tagger | `sklearn-crfsuite` |
| BERT fine-tuned | Universal POS tagging |
| Dependency parsing | `spaCy` dep, head, children |
| Universal Dependencies | UD project, 100+ languages |

---

#### Lesson 05.04 — Chunking and Shallow Parsing
**File**: `_13_05_04_chunking_shallow_parsing.md`

| Topics | Subtopics |
|---|---|
| Chunking | NP, VP, PP chunk extraction |
| `nltk.RegexpParser` | Grammar-based chunker |
| IOB for chunks | Same scheme as NER |
| Semantic role labeling | Predicate, argument structure |
| `AllenNLP` SRL | `allennlp.predictors.SemanticRoleLabeler` |
| Frame semantic parsing | FrameNet, PropBank |

---

#### Lesson 05.05 — Coreference Resolution
**File**: `_13_05_05_coreference_resolution.md`

| Topics | Subtopics |
|---|---|
| Coreference task | "He said he was tired" → who is "he"? |
| `spaCy-experimental` | Neural coref |
| `AllenNLP` coref | `CoreferenceResolver` predictor |
| OntoNotes | Standard coref benchmark |
| Applications | Document summarization, QA, RE |

---

#### Lesson 05.06 — Event Extraction
**File**: `_13_05_06_event_extraction.md`

| Topics | Subtopics |
|---|---|
| Event types | Trigger, argument, role |
| ACE 2005 | Standard event extraction dataset |
| Joint event extraction | BERT for trigger + argument jointly |
| `DEGREE` | Generative event extraction |
| Document-level event | Long document event chains |
| Applications | News monitoring, incident reports |

---

#### Lesson 05.07 — Biomedical NLP
**File**: `_13_05_07_biomedical_nlp.md`

| Topics | Subtopics |
|---|---|
| BioBERT | BERT pretrained on PubMed + PMC |
| PubMedBERT | In-domain only pretraining |
| Clinical NLP | `scispaCy`, MIMIC-III, i2b2 |
| Drug/disease NER | BC5CDR, NCBI-disease datasets |
| Medical relation extraction | ChemProt, DDI extraction |
| `medcat` | Medical concept annotation toolkit |
| De-identification | PHI removal, HIPAA compliance |

---

## MODULE 06 — Text Generation

**Folder**: `_13_06_text_generation/`  
**Lesson Count**: 8  
**Learning Order**: 6th

### Lessons

#### Lesson 06.01 — Decoding Strategies
**File**: `_13_06_01_decoding_strategies.md`

| Topics | Subtopics |
|---|---|
| Greedy decoding | Argmax at each step |
| Beam search | Width B, score normalization, length penalty |
| Top-k sampling | `top_k=50`, diverse outputs |
| Top-p (nucleus) sampling | `top_p=0.9`, dynamic vocab |
| Temperature | `temperature`, sharpen/flatten distribution |
| Repetition penalty | `repetition_penalty` parameter |
| Contrastive search | Coherence + diversity balance |
| `model.generate()` | All parameters unified |

---

#### Lesson 06.02 — Machine Translation
**File**: `_13_06_02_machine_translation.md`

| Topics | Subtopics |
|---|---|
| NMT overview | Attention-based Seq2Seq evolution |
| mBART | Multilingual denoising pretraining |
| NLLB | No Language Left Behind, 200 languages |
| MarianMT | `Helsinki-NLP/opus-mt-*` models |
| `transformers` translation | `pipeline("translation")` |
| BLEU evaluation | `sacrebleu`, `evaluate.load("bleu")` |
| Domain adaptation | Fine-tuning on domain-specific bitext |
| Back-translation | Data augmentation for low-resource |

---

#### Lesson 06.03 — Text Summarization
**File**: `_13_06_03_text_summarization.md`

| Topics | Subtopics |
|---|---|
| Extractive | Select sentences, TextRank, BERTSum |
| Abstractive | Generate new text, BART, PEGASUS |
| PEGASUS | Gap sentence generation pretraining |
| BART for summarization | `BartForConditionalGeneration` |
| FLAN-T5 summarization | Instruction-tuned |
| Datasets | CNN/DailyMail, XSum, SAMSum |
| ROUGE evaluation | R-1, R-2, R-L |
| Long document | Hierarchical, sliding window |

---

#### Lesson 06.04 — Question Generation
**File**: `_13_06_04_question_generation.md`

| Topics | Subtopics |
|---|---|
| QG task | Passage + answer → question |
| `t5-base-e2e-qg` | End-to-end question generation |
| `KPEW` pipeline | Key phrase extraction + QG |
| SQuAD for QG | Training data format |
| Difficulty control | Easy/medium/hard question generation |
| Applications | Exam generation, study assistants |

---

#### Lesson 06.05 — Controlled Text Generation
**File**: `_13_06_05_controlled_text_generation.md`

| Topics | Subtopics |
|---|---|
| Style transfer | Sentiment, formality, toxicity |
| CTRL | Condition codes for controllable generation |
| Plug-and-Play LM | External discriminator guidance |
| Prefix conditioning | Task prefix, persona prefix |
| Constrained decoding | Lexically constrained beam search |
| `outlines` library | Structured output generation |
| Grammar-constrained | JSON/regex-constrained LLM output |

---

#### Lesson 06.06 — Text Data Augmentation
**File**: `_13_06_06_text_data_augmentation.md`

| Topics | Subtopics |
|---|---|
| Easy Data Augmentation (EDA) | Synonym replace, random insert/swap/delete |
| Back-translation augmentation | Translate → back-translate |
| LLM augmentation | GPT paraphrasing, restatement |
| `nlpaug` | `SynonymAug`, `ContextualWordEmbsAug` |
| Conditional generation | Class-conditional BART/T5 |
| `TextAttack` | Augmentation + adversarial examples |
| Low-resource benefits | When augmentation helps most |

---

#### Lesson 06.07 — Code Generation
**File**: `_13_06_07_code_generation.md`

| Topics | Subtopics |
|---|---|
| Code LMs | Codex, CodeLLaMA, StarCoder2, DeepSeek-Coder |
| HumanEval | Pass@k evaluation metric |
| `transformers` CodeLLaMA | `pipeline("text-generation")` |
| Fill-in-the-middle | `<fim_prefix>`, `<fim_suffix>` |
| Unit test generation | TDD with LLM |
| MBPP / APPS | Additional code benchmarks |
| Fine-tuning on code | Domain-specific code datasets |

---

#### Lesson 06.08 — Grammatical Error Correction
**File**: `_13_06_08_grammatical_error_correction.md`

| Topics | Subtopics |
|---|---|
| GEC task | Detect and correct grammatical errors |
| GECToR | Sequence labeling approach |
| BART/T5 for GEC | Generative correction |
| BEA-2019 | Standard GEC benchmark |
| Metrics | ERRANT, M² scorer |
| `language-tool-python` | Rule-based GEC |
| Applications | Writing assistants, essay grading |

---

## MODULE 07 — Information Extraction

**Folder**: `_13_07_information_extraction/`  
**Lesson Count**: 6  
**Learning Order**: 7th

### Lessons

#### Lesson 07.01 — Extractive Question Answering
**File**: `_13_07_01_extractive_question_answering.md`

| Topics | Subtopics |
|---|---|
| Extractive QA | Find span in context |
| `AutoModelForQuestionAnswering` | `start_logits`, `end_logits` |
| SQuAD format | `context`, `question`, `answers` |
| Data preparation | Tokenizer offset mapping for spans |
| Impossible questions | SQuAD 2.0, no-answer detection |
| Evaluation | Exact Match, F1 |
| `pipeline("question-answering")` | Simple inference |

---

#### Lesson 07.02 — Open-Domain Question Answering
**File**: `_13_07_02_open_domain_question_answering.md`

| Topics | Subtopics |
|---|---|
| Retriever-Reader | DPR retriever + BERT reader |
| DPR | Dense Passage Retrieval |
| RAG overview | Retrieval-Augmented Generation (full in Phase 6) |
| `haystack` | `DocumentStore`, `Retriever`, `Reader` pipeline |
| TriviaQA / Natural Questions | Open-domain QA benchmarks |
| Multi-hop QA | HotpotQA, 2WikiMultiHopQA |

---

#### Lesson 07.03 — Open Information Extraction
**File**: `_13_07_03_open_information_extraction.md`

| Topics | Subtopics |
|---|---|
| OIE task | (Subject, Predicate, Object) triples |
| OpenIE 5 | Stanford OIE |
| `openie` | Python wrapper |
| Graphene | Discourse-based OIE |
| Neural OIE | Seq2seq triple generation |
| KG construction | Triple → knowledge graph |

---

#### Lesson 07.04 — Document-Level Information Extraction
**File**: `_13_07_04_document_level_information_extraction.md`

| Topics | Subtopics |
|---|---|
| DocRED | Document-level RE dataset |
| Cross-sentence RE | Inter-sentence relation extraction |
| ATLOP | Adaptive threshold + localized context |
| Document NER | Long document chunking strategies |
| Financial IE | EDGAR filings, FinNLP |
| Contract understanding | CUAD dataset |

---

#### Lesson 07.05 — Knowledge Base Population
**File**: `_13_07_05_knowledge_base_population.md`

| Topics | Subtopics |
|---|---|
| Entity linking | Wikidata, DBpedia, `spaCy-entity-linker` |
| Entity disambiguation | Context-sensitive linking |
| Slot filling | TAC KBP tasks |
| KBQA | Knowledge Base Question Answering |
| Wikidata SPARQL | `wikidata-query-service` |
| `falcon2.0` | Entity + relation linker |

---

#### Lesson 07.06 — Fact Verification and Claim Detection
**File**: `_13_07_06_fact_verification_claim_detection.md`

| Topics | Subtopics |
|---|---|
| FEVER dataset | Fact Extraction and VERification |
| Pipeline | Claim → evidence retrieval → NLI |
| `transformers` for fact check | Fine-tuned on FEVER |
| Claim detection | Worthy-of-check, claim/non-claim |
| Multi-hop fact checking | HoVer dataset |
| Hallucination detection | LLM output verification |

---

## MODULE 08 — Text Retrieval and Search

**Folder**: `_13_08_text_retrieval_and_search/`  
**Lesson Count**: 7  
**Learning Order**: 8th

### Lessons

#### Lesson 08.01 — Sparse Retrieval (BM25 and TF-IDF)
**File**: `_13_08_01_sparse_retrieval_bm25_tfidf.md`

| Topics | Subtopics |
|---|---|
| Boolean retrieval | Inverted index, posting lists |
| TF-IDF retrieval | `sklearn`, `rank_bm25` |
| BM25 | Okapi BM25, `k1`, `b` parameters |
| Elasticsearch | `elasticsearch-py`, full-text index |
| Whoosh | Pure Python search engine |
| Query expansion | Pseudo-relevance feedback, synonyms |
| Evaluation | MAP, NDCG, Recall@K |

---

#### Lesson 08.02 — Dense Retrieval
**File**: `_13_08_02_dense_retrieval.md`

| Topics | Subtopics |
|---|---|
| Bi-encoder | Query encoder + document encoder |
| DPR | Dense Passage Retrieval, dot-product similarity |
| `sentence-transformers` | `SentenceTransformer`, `encode()` |
| FAISS indexing | `IndexFlatIP`, `IndexHNSW`, `IndexIVFPQ` |
| `beir` | Benchmark of information retrieval |
| Training dense retrievers | In-batch negatives, hard negatives |
| ANCE | Asynchronous hard negative mining |

---

#### Lesson 08.03 — Hybrid Retrieval
**File**: `_13_08_03_hybrid_retrieval.md`

| Topics | Subtopics |
|---|---|
| BM25 + dense fusion | RRF (Reciprocal Rank Fusion) |
| SPLADE | Sparse + dense unified model |
| ColBERT | Late interaction, MaxSim |
| `colbert-ir` | ColBERT v2 implementation |
| Re-ranking pipeline | Retriever → Cross-encoder re-ranker |
| `cross-encoder/ms-marco-*` | Re-ranking with cross-encoders |

---

#### Lesson 08.04 — Neural Re-Ranking
**File**: `_13_08_04_neural_re_ranking.md`

| Topics | Subtopics |
|---|---|
| Cross-encoder | Full attention over (query, doc) pair |
| MonoT5 | T5-based pointwise re-ranker |
| DuoT5 | Pairwise re-ranker |
| `sentence-transformers` re-rank | `CrossEncoder.rank()` |
| MS MARCO | Re-ranking benchmark |
| Efficiency | Retrieval → short-list → re-rank |

---

#### Lesson 08.05 — Semantic Search Systems
**File**: `_13_08_05_semantic_search_systems.md`

| Topics | Subtopics |
|---|---|
| End-to-end pipeline | Encode → index → query → rank |
| `sentence-transformers` semantic search | `util.semantic_search()` |
| Vector databases | Pinecone, Weaviate, Qdrant, Chroma |
| `chromadb` | Local vector store |
| `qdrant-client` | Production vector DB |
| Metadata filtering | Hybrid search with attributes |
| Scaling | Sharding, replication, ANN algorithms |

---

#### Lesson 08.06 — Question Answering over Documents
**File**: `_13_08_06_question_answering_over_documents.md`

| Topics | Subtopics |
|---|---|
| QA pipeline | Retriever → Reader |
| `haystack` | DocumentStore, pipelines |
| Extractive QA over retrieved docs | Multiple passages |
| Generative QA | Generate from retrieved context |
| `FARMReader` / `TransformersReader` | Haystack readers |
| Evaluation | Exact Match, F1, retrieval accuracy |
| Production deployment | FastAPI + Haystack pipeline |

---

#### Lesson 08.07 — Passage and Paragraph Retrieval
**File**: `_13_08_07_passage_paragraph_retrieval.md`

| Topics | Subtopics |
|---|---|
| Passage chunking | Fixed length, sentence-based, semantic |
| `langchain.text_splitter` | `RecursiveCharacterTextSplitter` |
| Sliding window chunks | Overlap strategy |
| Hierarchical retrieval | Retrieve paragraph → re-rank sentences |
| Late chunking | Embed full doc → chunk embeddings |
| Parent document retriever | Retrieve small → return large |

---

## MODULE 09 — Conversational AI

**Folder**: `_13_09_conversational_ai/`  
**Lesson Count**: 7  
**Learning Order**: 9th

### Lessons

#### Lesson 09.01 — Dialogue Systems Architecture
**File**: `_13_09_01_dialogue_systems_architecture.md`

| Topics | Subtopics |
|---|---|
| Task-oriented dialogue | Intent + slot filling + policy |
| Open-domain dialogue | Chit-chat, social bots |
| Components | NLU → Dialogue Manager → NLG |
| Pipeline vs end-to-end | Trade-offs |
| Dialogue state tracking | DST, belief state |
| MultiWOZ dataset | Multi-domain task-oriented benchmark |

---

#### Lesson 09.02 — Intent Classification and Slot Filling
**File**: `_13_09_02_intent_classification_slot_filling.md`

| Topics | Subtopics |
|---|---|
| Intent recognition | BERT for multi-class intent |
| Slot filling | NER-style slot tagging |
| Joint models | JointBERT, IC + SF simultaneously |
| `rasa` | Open-source dialogue framework |
| `SNIPS` / ATIS | NLU benchmark datasets |
| Zero-shot intent | Using NLI for unseen intents |

---

#### Lesson 09.03 — Dialogue State Tracking
**File**: `_13_09_03_dialogue_state_tracking.md`

| Topics | Subtopics |
|---|---|
| DST formulation | Track slot-value pairs per turn |
| TRADE | Transferable dialogue state generator |
| SimpleTOD | Causal LM for TOD |
| In-context DST | GPT-4 with demonstrations |
| MultiWOZ evaluation | Joint goal accuracy |
| `ConvLab-3` | Multi-domain dialogue research framework |

---

#### Lesson 09.04 — Response Generation
**File**: `_13_09_04_response_generation.md`

| Topics | Subtopics |
|---|---|
| Retrieval-based | Select from candidates, bi-encoder |
| Generative | GPT-2, DialoGPT, BlenderBot |
| DialoGPT | Reddit-trained conversational GPT |
| BlenderBot | Multi-skill social conversation |
| GODEL | Goal-oriented dialogue |
| Persona conditioning | ConvAI2, persona-consistent responses |
| Diversity | Top-p + temperature for non-repetitive |

---

#### Lesson 09.05 — Task-Oriented Bot with Rasa
**File**: `_13_09_05_task_oriented_bot_rasa.md`

| Topics | Subtopics |
|---|---|
| Rasa architecture | NLU + Core + Action Server |
| `domain.yml` | Intents, slots, responses, actions |
| `nlu.yml` | Training examples |
| `stories.yml` | Conversation paths |
| Custom actions | `Action.run()`, `SlotSet` |
| `rasa train` / `rasa run` | Training and serving |
| Rasa X / Pro | Conversation review, CI/CD |

---

#### Lesson 09.06 — Evaluation of Conversational Systems
**File**: `_13_09_06_evaluation_conversational_systems.md`

| Topics | Subtopics |
|---|---|
| Automatic metrics | BLEU, ROUGE, BERTScore for dialogue |
| USR | Unreferenced + referenced metric |
| FED | Fine-grained evaluation |
| Human evaluation | Engagingness, coherence, informative |
| Safety evaluation | Toxicity, bias, harmful output |
| Task success rate | For task-oriented bots |

---

#### Lesson 09.07 — Conversational AI with LLMs
**File**: `_13_09_07_conversational_ai_with_llms.md`

| Topics | Subtopics |
|---|---|
| System prompts | Role definition, constraints |
| Few-shot examples | In-context conversation examples |
| `openai` Python SDK | `client.chat.completions.create()` |
| `litellm` | Unified LLM API |
| Memory management | Sliding window, summarization |
| Tool use / function calling | `tools`, `tool_choice` |
| Guardrails | `nemo-guardrails`, `guardrails-ai` |

---

## MODULE 10 — Industry Projects

**Folder**: `_13_10_industry_projects/`  
**Lesson Count**: 6  
**Learning Order**: 10th (Capstone)

### Lessons

#### Lesson 10.01 — Multi-Class News Classification API
**File**: `_13_10_01_multiclass_news_classification_api.md`

| Topics | Subtopics |
|---|---|
| Dataset | AG News / BBC News |
| Model | DeBERTa-v3-small fine-tuned |
| Pipeline | Preprocess → Tokenize → Fine-tune → Evaluate |
| Deployment | FastAPI + `uvicorn` |
| MLflow tracking | Experiment logging |
| Batch inference | Async batch endpoint |

---

#### Lesson 10.02 — NER and RE Pipeline for Financial Documents
**File**: `_13_10_02_ner_re_pipeline_financial_documents.md`

| Topics | Subtopics |
|---|---|
| Domain | EDGAR 10-K filings |
| NER | Company, amount, date, product entities |
| RE | Investment, acquisition relations |
| Models | FinBERT NER + custom RE head |
| Pipeline | PDF → OCR → NER → RE → JSON output |
| Knowledge graph | Neo4j storage |

---

#### Lesson 10.03 — Multilingual Customer Support Bot
**File**: `_13_10_03_multilingual_customer_support_bot.md`

| Topics | Subtopics |
|---|---|
| Architecture | Language ID → XLM-R intent → MT → response |
| Languages | English, Spanish, French, Hindi |
| Intent model | mBERT fine-tuned on multilingual SNIPS |
| Response templates | Language-conditioned NLG |
| Rasa integration | Multilingual domain.yml |
| Deployment | Docker + FastAPI + Rasa |

---

#### Lesson 10.04 — Semantic Search Engine for Research Papers
**File**: `_13_10_04_semantic_search_engine_research_papers.md`

| Topics | Subtopics |
|---|---|
| Dataset | arXiv abstracts + full text |
| Embeddings | `all-mpnet-base-v2` via sentence-transformers |
| Vector DB | Qdrant |
| Query | Semantic + BM25 hybrid (RRF) |
| Re-ranking | `cross-encoder/ms-marco-MiniLM-L-12-v2` |
| UI | FastAPI + simple search frontend |
| Evaluation | Recall@10, MRR |

---

#### Lesson 10.05 — Abstractive Summarization Service
**File**: `_13_10_05_abstractive_summarization_service.md`

| Topics | Subtopics |
|---|---|
| Model | BART-large-CNN / PEGASUS |
| Input | News article / report / paper |
| Length control | `min_length`, `max_length`, `length_penalty` |
| Batch processing | `pipeline("summarization", batch_size=8)` |
| API | POST `/summarize` with JSON body |
| MLflow | ROUGE score tracking per experiment |

---

#### Lesson 10.06 — End-to-End Document Q&A System
**File**: `_13_10_06_end_to_end_document_qa_system.md`

| Topics | Subtopics |
|---|---|
| Architecture | PDF → OCR → Chunk → Embed → FAISS → QA |
| Tools | `surya` + `sentence-transformers` + `haystack` |
| Query | Semantic retrieval + extractive reader |
| Multi-doc | Multiple PDFs in one knowledge base |
| API | `/upload`, `/query` endpoints |
| Evaluation | End-to-end EM + F1 on curated Q&A pairs |

---

## Full Folder Structure

```
docs/curriculum/_13_nlp/
│
├── _13_01_nlp_foundations/
│   ├── _13_01_01_text_preprocessing_pipeline.md
│   ├── _13_01_02_morphological_analysis.md
│   ├── _13_01_03_statistical_nlp_fundamentals.md
│   ├── _13_01_04_regular_expressions_nlp.md
│   ├── _13_01_05_stopwords_vocabulary_corpus_statistics.md
│   ├── _13_01_06_evaluation_metrics_nlp.md
│   └── _13_01_07_nlp_libraries_overview.md
│
├── _13_02_text_representation/
│   ├── _13_02_01_bow_tfidf_applied.md
│   ├── _13_02_02_word2vec_glove.md
│   ├── _13_02_03_fasttext_subword_embeddings.md
│   ├── _13_02_04_sentence_document_embeddings.md
│   ├── _13_02_05_contextual_embeddings_elmo.md
│   ├── _13_02_06_subword_tokenization.md
│   ├── _13_02_07_knowledge_graph_embeddings.md
│   └── _13_02_08_multilingual_cross_lingual_embeddings.md
│
├── _13_03_pretrained_language_models/
│   ├── _13_03_01_bert_architecture_pretraining.md
│   ├── _13_03_02_bert_variants_improvements.md
│   ├── _13_03_03_gpt_style_decoder_models.md
│   ├── _13_03_04_encoder_decoder_models_t5_bart.md
│   ├── _13_03_05_efficient_transformers.md
│   ├── _13_03_06_tokenizer_deep_dive.md
│   ├── _13_03_07_finetuning_plms_huggingface.md
│   ├── _13_03_08_peft_lora_adapters_prompt_tuning.md
│   └── _13_03_09_benchmarks_model_evaluation.md
│
├── _13_04_nlp_tasks_classification/
│   ├── _13_04_01_text_classification.md
│   ├── _13_04_02_sentiment_analysis.md
│   ├── _13_04_03_natural_language_inference.md
│   ├── _13_04_04_topic_classification_detection.md
│   ├── _13_04_05_document_classification_scale.md
│   ├── _13_04_06_hate_speech_content_moderation.md
│   └── _13_04_07_language_identification_detection.md
│
├── _13_05_sequence_labeling/
│   ├── _13_05_01_named_entity_recognition.md
│   ├── _13_05_02_relation_extraction.md
│   ├── _13_05_03_pos_tagging.md
│   ├── _13_05_04_chunking_shallow_parsing.md
│   ├── _13_05_05_coreference_resolution.md
│   ├── _13_05_06_event_extraction.md
│   └── _13_05_07_biomedical_nlp.md
│
├── _13_06_text_generation/
│   ├── _13_06_01_decoding_strategies.md
│   ├── _13_06_02_machine_translation.md
│   ├── _13_06_03_text_summarization.md
│   ├── _13_06_04_question_generation.md
│   ├── _13_06_05_controlled_text_generation.md
│   ├── _13_06_06_text_data_augmentation.md
│   ├── _13_06_07_code_generation.md
│   └── _13_06_08_grammatical_error_correction.md
│
├── _13_07_information_extraction/
│   ├── _13_07_01_extractive_question_answering.md
│   ├── _13_07_02_open_domain_question_answering.md
│   ├── _13_07_03_open_information_extraction.md
│   ├── _13_07_04_document_level_information_extraction.md
│   ├── _13_07_05_knowledge_base_population.md
│   └── _13_07_06_fact_verification_claim_detection.md
│
├── _13_08_text_retrieval_and_search/
│   ├── _13_08_01_sparse_retrieval_bm25_tfidf.md
│   ├── _13_08_02_dense_retrieval.md
│   ├── _13_08_03_hybrid_retrieval.md
│   ├── _13_08_04_neural_re_ranking.md
│   ├── _13_08_05_semantic_search_systems.md
│   ├── _13_08_06_question_answering_over_documents.md
│   └── _13_08_07_passage_paragraph_retrieval.md
│
├── _13_09_conversational_ai/
│   ├── _13_09_01_dialogue_systems_architecture.md
│   ├── _13_09_02_intent_classification_slot_filling.md
│   ├── _13_09_03_dialogue_state_tracking.md
│   ├── _13_09_04_response_generation.md
│   ├── _13_09_05_task_oriented_bot_rasa.md
│   ├── _13_09_06_evaluation_conversational_systems.md
│   └── _13_09_07_conversational_ai_with_llms.md
│
└── _13_10_industry_projects/
    ├── _13_10_01_multiclass_news_classification_api.md
    ├── _13_10_02_ner_re_pipeline_financial_documents.md
    ├── _13_10_03_multilingual_customer_support_bot.md
    ├── _13_10_04_semantic_search_engine_research_papers.md
    ├── _13_10_05_abstractive_summarization_service.md
    └── _13_10_06_end_to_end_document_qa_system.md
```

---

## Learning Order

```
01 NLP Foundations  (Preprocessing, stats, regex, metrics)
    ↓
02 Text Representation  (BoW → Word2Vec → SBERT → Subword)
    ↓
03 Pretrained Language Models  (BERT → GPT → T5 → PEFT → Benchmarks)
    ↓
04 NLP Classification  (Text clf → Sentiment → NLI → Topics → Scale)
    ↓
05 Sequence Labeling  (NER → RE → POS → Coref → Events → BioNLP)
    ↓
06 Text Generation  (Decoding → MT → Summarization → Code → GEC)
    ↓
07 Information Extraction  (Extractive QA → OIE → Fact Verification)
    ↓
08 Text Retrieval & Search  (BM25 → Dense → Hybrid → Re-rank → Semantic)
    ↓
09 Conversational AI  (Intent → DST → Response → Rasa → LLM bots)
    ↓
10 Industry Projects (Capstone)
```

---

## Summary Statistics

| Module | Title | Lessons |
|---|---|---|
| 01 | NLP Foundations | 7 |
| 02 | Text Representation | 8 |
| 03 | Pretrained Language Models | 9 |
| 04 | NLP Classification | 7 |
| 05 | Sequence Labeling | 7 |
| 06 | Text Generation | 8 |
| 07 | Information Extraction | 6 |
| 08 | Text Retrieval & Search | 7 |
| 09 | Conversational AI | 7 |
| 10 | Industry Projects | 6 |
| **TOTAL** | | **72 lessons** |

---

## Phase 5 Handoff (Generative AI & LLMs)

Nodes introduced in Phase 4 and extended in Phase 5:
- GPT-style models → full LLM fine-tuning (SFT, RLHF, DPO)
- PEFT / LoRA → QLoRA for LLMs
- Conversational AI → Instruction-tuned chatbots
- Semantic search → RAG (Phase 6)
- Code generation → Code LLMs and Agents
