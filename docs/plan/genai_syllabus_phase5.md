# Phase 5: Generative AI & Large Language Models — Enterprise Syllabus
## Learning OS Enterprise Standard | Curriculum Architecture v2.0

**Classification**: Chief Curriculum Architect — Syllabus Design Document  
**Phase**: 5 of 8  
**Domain**: Generative AI & LLMs  
**Required Previous Phases**: Phase 1 (ML), Phase 2 (DL), Phase 3 (CV), Phase 4 (NLP)  
**Folder Root**: `docs/curriculum/_14_generative_ai_llms/`  
**Last Updated**: 2026-07-28

---

## Dependency Graph

```
_13_nlp  (Phase 4)
    └─> _14_generative_ai_llms  ◄── THIS PHASE
            └─> _15_rag_engineering  (Phase 6)
            └─> _16_ai_agents  (Phase 7)
```

Cross-phase reuse nodes (zero duplication):
- `NLP.13_03_03` GPT-style decoders → extended with full LLM training
- `NLP.13_03_08` PEFT/LoRA → extended with QLoRA, full SFT pipeline
- `NLP.13_06_01` Decoding strategies → extended with speculative decoding
- `DL.11_07` Attention → extended with Flash Attention, GQA, MoE
- `DL.11_04_04` Mixed precision → extended with BF16, quantization at scale
- `CV.12_08_05` LVLMs (LLaVA) → extended as multimodal LLMs

---

## Skills Gained (This Phase)

- Understand LLM architecture internals: tokenization, attention, positional encoding, MoE
- Pretrain small language models from scratch on custom corpora
- Apply Supervised Fine-Tuning (SFT) with HuggingFace Trainer + TRL
- Implement RLHF pipeline: reward model training, PPO fine-tuning
- Apply Direct Preference Optimization (DPO), ORPO, SimPO
- Engineer production-grade prompts for reasoning and structured output
- Build and evaluate multimodal LLMs (vision + language)
- Quantize and compress LLMs: GPTQ, AWQ, GGUF, llama.cpp
- Deploy LLMs for production inference: vLLM, TGI, Ollama
- Evaluate LLMs: automated benchmarks, human eval, safety testing

---

## Course Structure

```
_14_generative_ai_llms/
├── _14_01_llm_architecture_internals/
├── _14_02_llm_pretraining/
├── _14_03_supervised_fine_tuning/
├── _14_04_alignment_rlhf_dpo/
├── _14_05_prompt_engineering/
├── _14_06_multimodal_llms/
├── _14_07_llm_evaluation_and_safety/
├── _14_08_llm_inference_and_serving/
├── _14_09_llm_compression_and_edge/
└── _14_10_industry_projects/
```

---

## MODULE 01 — LLM Architecture Internals

**Folder**: `_14_01_llm_architecture_internals/`  
**Lesson Count**: 8  
**Learning Order**: 1st

### Lessons

#### Lesson 01.01 — Transformer Scaling Laws
**File**: `_14_01_01_transformer_scaling_laws.md`

| Topics | Subtopics |
|---|---|
| Chinchilla scaling laws | Compute-optimal: tokens ∝ params |
| Kaplan scaling laws | Power-law loss vs compute |
| Parameter vs data tradeoff | When to scale model vs data |
| Emergent abilities | Phase transitions at scale |
| Scaling beyond Chinchilla | LLaMA-style data-efficient training |
| MFU (Model FLOP Utilization) | GPU efficiency metric |

---

#### Lesson 01.02 — Advanced Positional Encodings
**File**: `_14_01_02_advanced_positional_encodings.md`

| Topics | Subtopics |
|---|---|
| RoPE | Rotary Position Embedding, LLaMA |
| ALiBi | Attention with Linear Biases, extrapolation |
| YaRN | Context extension via NTK-aware RoPE |
| LongRoPE | 2M token context extension |
| NoPE | Some layers without PE |
| Context length extrapolation | Interpolation strategies |

---

#### Lesson 01.03 — Efficient Attention in LLMs
**File**: `_14_01_03_efficient_attention_llms.md`

| Topics | Subtopics |
|---|---|
| Multi-Head Attention | Standard MHA, O(n²) |
| Multi-Query Attention | Single KV head, fast inference |
| Grouped-Query Attention | k KV heads, LLaMA-2/3 |
| Flash Attention 1/2/3 | IO-aware, tiled computation |
| Sliding Window Attention | Mistral, local context |
| KV Cache | Key-value cache during autoregressive gen |
| Paged Attention | vLLM memory management |

---

#### Lesson 01.04 — Mixture of Experts (MoE)
**File**: `_14_01_04_mixture_of_experts_moe.md`

| Topics | Subtopics |
|---|---|
| MoE architecture | Sparse activation, top-K routing |
| Router | `SwitchTransformerRouter`, load balancing |
| Expert capacity | Token routing, auxiliary loss |
| Mixtral 8×7B | MoE LLM architecture |
| Mixtral 8×22B / DeepSeek-MoE | Large-scale MoE |
| Expert parallelism | Distributed MoE training |
| Memory efficiency | Active params vs total params |

---

#### Lesson 01.05 — LLM Normalization and FFN Variants
**File**: `_14_01_05_llm_normalization_ffn_variants.md`

| Topics | Subtopics |
|---|---|
| Pre-LN vs Post-LN | Training stability tradeoffs |
| RMSNorm | `LlamaRMSNorm`, simplified LayerNorm |
| SwiGLU FFN | Gated linear unit, LLaMA FFN |
| GeGLU | GELU gated variant |
| FFN expansion ratio | 4× in BERT, 2.67× in SwiGLU |
| Parallel attention+FFN | PaLM architecture |

---

#### Lesson 01.06 — Tokenization in LLMs
**File**: `_14_01_06_tokenization_in_llms.md`

| Topics | Subtopics |
|---|---|
| Tiktoken | OpenAI's BPE tokenizer (`cl100k_base`) |
| LLaMA tokenizer | SentencePiece BPE, 32K vocab |
| GPT-4 tokenizer | 100K vocab, multilingual efficiency |
| Special tokens in LLMs | `<s>`, `</s>`, `[INST]`, `<|im_start|>` |
| Chat templates | `apply_chat_template()`, Jinja2 |
| Tokenizer vocab extension | Adding domain tokens |
| Token efficiency | Tokens per word by language |

---

#### Lesson 01.07 — LLM Model Families
**File**: `_14_01_07_llm_model_families.md`

| Topics | Subtopics |
|---|---|
| LLaMA 1/2/3/3.1/3.3 | Meta open-weight family |
| Mistral / Mixtral | European open models |
| Gemma 2/3 | Google open models |
| Phi-3/4 | Small data-efficient models |
| Qwen 2/2.5/3 | Alibaba multilingual |
| DeepSeek V2/V3/R1 | Chinese open-source SOTA |
| Command R+ | Cohere enterprise model |
| Model comparison | Params, context, license, benchmark |

---

#### Lesson 01.08 — LLM Training Infrastructure
**File**: `_14_01_08_llm_training_infrastructure.md`

| Topics | Subtopics |
|---|---|
| 3D parallelism | Data + Tensor + Pipeline parallel |
| Tensor parallelism | Megatron-LM column/row splitting |
| Pipeline parallelism | Micro-batches, bubble overhead |
| `DeepSpeed` | ZeRO-1/2/3, `ds_config.json` |
| `FSDP` | Fully Sharded Data Parallel, PyTorch native |
| Megatron-LM | NVIDIA LLM training framework |
| Gradient checkpointing | Memory vs compute tradeoff |
| Activation offloading | CPU offload during training |

---

## MODULE 02 — LLM Pretraining

**Folder**: `_14_02_llm_pretraining/`  
**Lesson Count**: 7  
**Learning Order**: 2nd

### Lessons

#### Lesson 02.01 — Pretraining Data Preparation
**File**: `_14_02_01_pretraining_data_preparation.md`

| Topics | Subtopics |
|---|---|
| Web crawl data | Common Crawl, C4, OSCAR |
| Data filtering | Quality filter, deduplication, toxicity |
| MinHash deduplication | LSH-based near-duplicate removal |
| Language filtering | FastText LID, ratio threshold |
| Data mixing | Domain weights, sampling strategy |
| `datatrove` | Scalable pretraining data pipeline |
| `dolma` | OLMo pretraining dataset |
| Data cards | Dataset transparency, model cards |

---

#### Lesson 02.02 — Causal Language Model Pretraining
**File**: `_14_02_02_causal_lm_pretraining.md`

| Topics | Subtopics |
|---|---|
| CLM objective | Predict next token, cross-entropy |
| Packing sequences | Efficient long-context batching |
| `DataCollatorForLanguageModeling` | Causal + MLM collators |
| Batch construction | Padding, packing, `ConstantLengthDataset` |
| Gradient accumulation | Effective batch size |
| Learning rate warmup | Cosine decay schedule |
| `GPTNeoXForCausalLM` | Small model pretraining |
| OLMo | Open Language Model, full transparency |

---

#### Lesson 02.03 — Continued Pretraining and Domain Adaptation
**File**: `_14_02_03_continued_pretraining_domain.md`

| Topics | Subtopics |
|---|---|
| Continued pretraining | Initialize from checkpoint → new domain |
| Domain-adaptive pretraining | DAPT (Gururangan et al.) |
| Medical domain | BioMedLM, MedPaLM 2 |
| Legal domain | SaulLM, LegalBERT |
| Code domain | Code Llama continued from LLaMA |
| Catastrophic forgetting | Regularization, replay |
| Learning rate selection | Lower LR for continued pretraining |

---

#### Lesson 02.04 — Training Small LLMs from Scratch
**File**: `_14_02_04_training_small_llms_from_scratch.md`

| Topics | Subtopics |
|---|---|
| Model design | Config: n_layers, d_model, n_heads, vocab |
| `nanoGPT` | Minimal GPT-2 reimplementation |
| `LitGPT` | Lightning-based clean LLM training |
| Data pipeline | Tokenize → memmap → ConstantLengthDataset |
| Training loop | DDP, mixed precision, gradient clip |
| Checkpointing | Save every N steps, resume |
| Evaluation during pretraining | Perplexity on held-out data |

---

#### Lesson 02.05 — Instruction Pretraining
**File**: `_14_02_05_instruction_pretraining.md`

| Topics | Subtopics |
|---|---|
| Instruction data at pretraining | FLAN-style mixture |
| FLAN-T5 pretraining | 1800+ NLP tasks as text-to-text |
| MetaICL | Meta-training for in-context learning |
| Instruction upsampling | Mix raw + instruction data |
| Multitask pretraining | Unifying many tasks |

---

#### Lesson 02.06 — Evaluation during Pretraining
**File**: `_14_02_06_evaluation_during_pretraining.md`

| Topics | Subtopics |
|---|---|
| Perplexity tracking | Bits-per-character, BPC |
| Downstream probes | Mid-training eval on benchmarks |
| `lm-evaluation-harness` | Zero-shot eval during training |
| Loss spike detection | Log-loss monitoring |
| Checkpoint comparison | Select best checkpoint |
| Wandb pretraining dashboard | Loss curves, gradient norms, LR |

---

#### Lesson 02.07 — Open Pretraining Datasets
**File**: `_14_02_07_open_pretraining_datasets.md`

| Topics | Subtopics |
|---|---|
| The Pile | 800GB diverse corpus |
| RedPajama | LLaMA training data recreation |
| DCLM | Data Curation Language Model |
| FineWeb / FineWeb-Edu | HF filtered web corpus |
| Dolma | OLMo dataset, CC + books + Wikipedia |
| ROOTS | Multilingual, BigScience |
| StarCoder data | The Stack for code |

---

## MODULE 03 — Supervised Fine-Tuning (SFT)

**Folder**: `_14_03_supervised_fine_tuning/`  
**Lesson Count**: 8  
**Learning Order**: 3rd

### Lessons

#### Lesson 03.01 — Instruction Tuning
**File**: `_14_03_01_instruction_tuning.md`

| Topics | Subtopics |
|---|---|
| Instruction tuning concept | (instruction, output) pairs |
| FLAN | 62 NLP datasets → instruction format |
| Self-Instruct | GPT-3 generating its own instructions |
| Alpaca | 52K instructions from GPT-3.5 |
| WizardLM | Evol-Instruct, complex instructions |
| OpenHermes | Synthetically generated instruct data |
| `trl.SFTTrainer` | Simple fine-tuning loop |
| Chat templates | `apply_chat_template()` during SFT |

---

#### Lesson 03.02 — SFT Data Preparation
**File**: `_14_03_02_sft_data_preparation.md`

| Topics | Subtopics |
|---|---|
| Instruction dataset formats | Alpaca, ShareGPT, OpenAI chat |
| `datasets` library | `load_dataset`, `map`, `filter` |
| Quality filtering | Length, perplexity, deduplication |
| `deita` | Data selection for instruction tuning |
| Synthetic data generation | GPT-4 as teacher |
| Data mixing | Code + math + general |
| `ultrachat`, `OpenOrca` | High-quality SFT datasets |

---

#### Lesson 03.03 — Full Fine-Tuning with TRL
**File**: `_14_03_03_full_fine_tuning_trl.md`

| Topics | Subtopics |
|---|---|
| `trl.SFTTrainer` | `model`, `dataset`, `peft_config` |
| `SFTConfig` | `max_seq_length`, `packing`, `dataset_text_field` |
| Gradient checkpointing | `use_reentrant=False` |
| Multi-GPU SFT | `accelerate launch`, `torchrun` |
| `accelerate` | `AcceleratorConfig`, `deepspeed_config` |
| Training loss monitoring | W&B, TensorBoard |
| Saving and merging | `model.save_pretrained`, `merge_and_unload` |

---

#### Lesson 03.04 — QLoRA Fine-Tuning
**File**: `_14_03_04_qlora_fine_tuning.md`

| Topics | Subtopics |
|---|---|
| QLoRA concept | 4-bit base model + LoRA adapters |
| `BitsAndBytesConfig` | `load_in_4bit`, `bnb_4bit_quant_type="nf4"` |
| `prepare_model_for_kbit_training` | Enable gradient computation |
| `LoraConfig` | `r`, `lora_alpha`, `target_modules` |
| `get_peft_model` | Wrap model |
| Memory requirements | 7B, 13B, 70B VRAM requirements |
| Merging adapters | `merge_and_unload()` |
| Inference after QLoRA | `AutoModelForCausalLM` + adapter |

---

#### Lesson 03.05 — Chat Fine-Tuning
**File**: `_14_03_05_chat_fine_tuning.md`

| Topics | Subtopics |
|---|---|
| Chat format | System + User + Assistant turns |
| `apply_chat_template` | Model-specific templates |
| Loss masking | Only compute loss on assistant tokens |
| `DataCollatorForCompletionOnlyLM` | TRL utility |
| Multi-turn conversation | Training on long dialogues |
| ShareGPT format | `conversations` key |
| OpenAI format | `messages` key |
| Domain chat fine-tuning | Customer support, medical, legal |

---

#### Lesson 03.06 — Math and Reasoning Fine-Tuning
**File**: `_14_03_06_math_reasoning_fine_tuning.md`

| Topics | Subtopics |
|---|---|
| Chain-of-Thought data | GSM8K, MATH dataset |
| Rejection sampling | Generate N → filter correct |
| Process reward models | Step-level feedback |
| STILL-3 / NovaSky | Open math reasoning SFT |
| `MetaMath` | Data augmentation for math |
| Tool-augmented reasoning | Code interpreter integration |
| DeepSeek-R1 distillation | Reasoning model fine-tuning |

---

#### Lesson 03.07 — Code Fine-Tuning
**File**: `_14_03_07_code_fine_tuning.md`

| Topics | Subtopics |
|---|---|
| Code SFT datasets | Code Alpaca, OSS-Instruct, Evol-Code |
| Fill-in-the-Middle training | FIM transformation |
| `StarCoder2-Instruct` | Instruction-tuned code model |
| `CodeLlama-Instruct` | Code instruction format |
| HumanEval evaluation | `pass@1`, `pass@10`, `pass@100` |
| Function calling SFT | JSON schema output training |
| EvalPlus | Enhanced HumanEval with more tests |

---

#### Lesson 03.08 — Continual and Multi-Task Fine-Tuning
**File**: `_14_03_08_continual_multitask_fine_tuning.md`

| Topics | Subtopics |
|---|---|
| Catastrophic forgetting in SFT | Regularization, replay |
| Task-specific LoRA | Separate adapters per task |
| Multi-adapter | `peft` multi-adapter switching |
| Continual learning | EWC, PackNet for LLMs |
| Data replay | Mix old + new training data |
| Mixture of LoRA experts | MoLoRA |

---

## MODULE 04 — Alignment: RLHF and DPO

**Folder**: `_14_04_alignment_rlhf_dpo/`  
**Lesson Count**: 8  
**Learning Order**: 4th

### Lessons

#### Lesson 04.01 — RLHF Overview and InstructGPT
**File**: `_14_04_01_rlhf_overview_instructgpt.md`

| Topics | Subtopics |
|---|---|
| Alignment problem | Helpful, Harmless, Honest (3H) |
| InstructGPT pipeline | SFT → RM → PPO |
| Human preference data | Pairwise comparisons |
| Constitutional AI | Anthropic RLHF variant |
| Reward hacking | Over-optimization of proxy reward |
| KL divergence penalty | `β` coefficient in PPO objective |

---

#### Lesson 04.02 — Reward Model Training
**File**: `_14_04_02_reward_model_training.md`

| Topics | Subtopics |
|---|---|
| Reward model formulation | `r(x, y)` scalar output |
| Bradley-Terry model | Pairwise preference loss |
| `AutoModelForSequenceClassification` | 1-class regression head |
| `trl.RewardTrainer` | TRL reward training |
| Preference datasets | Anthropic HH, OpenAI comparisons |
| Reward model evaluation | Accuracy on held-out pairs |
| Process vs outcome RM | Step-level vs final answer |

---

#### Lesson 04.03 — PPO Fine-Tuning
**File**: `_14_04_03_ppo_fine_tuning.md`

| Topics | Subtopics |
|---|---|
| PPO objective | Clipped surrogate objective |
| `trl.PPOTrainer` | `ppo_config`, `generate`, `compute_rewards` |
| Reference model | Frozen SFT model for KL |
| Value model | Critic network |
| Reward normalization | Running mean/std |
| KL penalty | Adaptive KL coefficient |
| Memory | 2 LLMs + value head in memory |

---

#### Lesson 04.04 — Direct Preference Optimization (DPO)
**File**: `_14_04_04_direct_preference_optimization_dpo.md`

| Topics | Subtopics |
|---|---|
| DPO derivation | Closed-form RL without RM |
| DPO objective | β log(σ(β log(π_θ/π_ref)_w - β log(π_θ/π_ref)_l)) |
| `trl.DPOTrainer` | `model`, `ref_model`, `beta` |
| Preference data format | `prompt`, `chosen`, `rejected` |
| DPO datasets | UltraFeedback, Anthropic HH |
| Evaluation | Win rate vs reference, MT-Bench |
| DPO vs PPO | Simpler, no RM, similar quality |

---

#### Lesson 04.05 — ORPO, SimPO, and DPO Variants
**File**: `_14_05_orpo_simpo_dpo_variants.md`

| Topics | Subtopics |
|---|---|
| ORPO | Odds Ratio Preference Optimization, no reference model |
| `trl.ORPOTrainer` | Single model, simpler setup |
| SimPO | Simple Preference Optimization, length normalization |
| IPO | Identity PO, exact solution |
| KTO | Kahneman-Tversky Optimization, unpaired |
| `trl.KTOTrainer` | Binary feedback, no pairs needed |
| CPO | Contrastive Preference Optimization |
| Comparison table | Memory, data, performance |

---

#### Lesson 04.06 — Constitutional AI and RLAIF
**File**: `_14_04_06_constitutional_ai_rlaif.md`

| Topics | Subtopics |
|---|---|
| Constitutional AI | Anthropic, self-critique + revision |
| RLAIF | LLM as judge, no human labels |
| Self-play alignment | Critique → revise → rank |
| Principle-driven | Define principles → auto-label |
| `llm-as-judge` | Using GPT-4 / Claude for eval |
| Scalable oversight | Debate, amplification |

---

#### Lesson 04.07 — Process Reward Models
**File**: `_14_04_07_process_reward_models.md`

| Topics | Subtopics |
|---|---|
| Outcome RM vs Process RM | Final vs step-level feedback |
| Let's Verify Step by Step | OpenAI PRM dataset |
| MATH-SHEPHERD | Process-supervised math RM |
| Best-of-N with PRM | Select best reasoning chain |
| MCTS with PRM | Monte Carlo Tree Search for reasoning |
| Training PRM | Step-level preference labeling |

---

#### Lesson 04.08 — Evaluation of Aligned Models
**File**: `_14_04_08_evaluation_aligned_models.md`

| Topics | Subtopics |
|---|---|
| MT-Bench | Multi-turn benchmark, GPT-4 judge |
| AlpacaEval 2 | Win rate vs GPT-4-Turbo |
| Arena-Hard | 500 hard prompts, judge |
| LMSys Chatbot Arena | Human preference leaderboard |
| IFEval | Instruction following evaluation |
| Safety evals | ToxiGen, BBQ, WinoBias |
| `mt-bench` + `FastChat` | Running evaluation locally |

---

## MODULE 05 — Prompt Engineering

**Folder**: `_14_05_prompt_engineering/`  
**Lesson Count**: 7  
**Learning Order**: 5th

### Lessons

#### Lesson 05.01 — Prompt Engineering Fundamentals
**File**: `_14_05_01_prompt_engineering_fundamentals.md`

| Topics | Subtopics |
|---|---|
| Prompt anatomy | Instruction, context, examples, output format |
| Zero-shot prompting | Direct instruction |
| One-shot / few-shot | In-context examples |
| Prompt sensitivity | Order, phrasing, whitespace effects |
| System prompts | Role definition, constraints |
| Temperature and top-p | Output variation control |
| `openai` Python SDK | `chat.completions.create()` |

---

#### Lesson 05.02 — Chain-of-Thought Prompting
**File**: `_14_05_02_chain_of_thought_prompting.md`

| Topics | Subtopics |
|---|---|
| CoT overview | "Let's think step by step" |
| Zero-shot CoT | Appending trigger phrase |
| Few-shot CoT | Exemplar reasoning chains |
| Self-consistency | Sample N → majority vote |
| Least-to-Most | Decompose → solve subproblems |
| Plan-and-Solve | Plan first, execute plan |
| Tree of Thought | Explore multiple reasoning branches |

---

#### Lesson 05.03 — Structured Output and JSON Mode
**File**: `_14_05_03_structured_output_json_mode.md`

| Topics | Subtopics |
|---|---|
| JSON mode | `response_format={"type":"json_object"}` |
| Structured outputs | `response_format={"type":"json_schema"}` |
| `instructor` library | Pydantic-validated LLM output |
| `outlines` library | Grammar-constrained generation |
| Function calling | `tools`, `tool_choice`, parallel calls |
| XML structured output | Anthropic Claude XML |
| Validation and retry | Auto-repair on parse failure |

---

#### Lesson 05.04 — Advanced Prompting Techniques
**File**: `_14_05_04_advanced_prompting_techniques.md`

| Topics | Subtopics |
|---|---|
| ReAct | Reason + Act, tool-use interleaving |
| Reflexion | Self-evaluation loop |
| PAL | Program-Aided Language Models |
| Generated Knowledge | Generate facts → answer |
| Maieutic prompting | Explain reasoning, check consistency |
| Directional Stimulus | Hint-based steering |
| Active Prompting | Uncertainty-based exemplar selection |

---

#### Lesson 05.05 — Prompt Optimization and AutoPrompt
**File**: `_14_05_05_prompt_optimization_autoprompt.md`

| Topics | Subtopics |
|---|---|
| Manual prompt iteration | A/B testing, eval loop |
| DSPy | Declarative prompt optimization |
| `dspy.Module` | Signature, Predict, ChainOfThought |
| `dspy.MIPROv2` | Automatic prompt optimizer |
| TextGrad | Gradient-based prompt tuning |
| LLM-based prompt refinement | Meta-prompting |
| Evaluation-driven optimization | Metric-guided iteration |

---

#### Lesson 05.06 — Context Window Management
**File**: `_14_05_06_context_window_management.md`

| Topics | Subtopics |
|---|---|
| Context limits | 4K → 8K → 32K → 128K → 1M |
| Lost in the middle | Performance degradation at mid-context |
| Retrieval augmentation | Only include relevant context |
| Summarization compression | Compress context to fit |
| Memory-augmented | External memory → context injection |
| Chunking strategies | Fixed, semantic, late chunking |
| Token counting | `tiktoken.encoding_for_model` |

---

#### Lesson 05.07 — Prompt Security and Robustness
**File**: `_14_05_07_prompt_security_robustness.md`

| Topics | Subtopics |
|---|---|
| Prompt injection | Malicious instructions in user input |
| Jailbreaking | DAN, roleplay, suffix attacks |
| Indirect prompt injection | Injections from retrieved content |
| Defense strategies | Input sanitization, system prompt hardening |
| `promptfoo` | Prompt testing and red-teaming |
| `garak` | LLM vulnerability scanner |
| Guardrails | Input/output filters |

---

## MODULE 06 — Multimodal LLMs

**Folder**: `_14_06_multimodal_llms/`  
**Lesson Count**: 7  
**Learning Order**: 6th

### Lessons

#### Lesson 06.01 — Vision-Language Pretraining
**File**: `_14_06_01_vision_language_pretraining.md`

| Topics | Subtopics |
|---|---|
| CLIP pretraining recap | Contrastive image-text |
| ALIGN | Dual-encoder, noisy pairs |
| FLAVA | Unified multimodal pretraining |
| CoCa | Contrastive Captioners |
| Flamingo | Visual conditioning with few-shot |
| Q-Former | BLIP-2 bridge between vision and LLM |
| Connection strategies | Projector, cross-attention, Q-Former |

---

#### Lesson 06.02 — LLaVA and Visual Instruction Tuning
**File**: `_14_06_02_llava_visual_instruction_tuning.md`

| Topics | Subtopics |
|---|---|
| LLaVA-1 | CLIP encoder + LLaMA, linear projector |
| LLaVA-1.5 | MLP projector, ShareGPT4V data |
| LLaVA-NeXT | AnyRes, multi-image, video |
| LLaVA-OneVision | Unified image/video/text |
| Training stages | Pretraining projector → SFT |
| `transformers.LlavaForConditionalGeneration` | HF interface |
| Data | LLaVA-Instruct-150K, ShareGPT4V |

---

#### Lesson 06.03 — Strong Open Multimodal LLMs
**File**: `_14_06_03_strong_open_multimodal_llms.md`

| Topics | Subtopics |
|---|---|
| InternVL 2.5/3 | Strong open-source LVLM |
| Qwen2.5-VL | Dynamic resolution, video |
| Phi-4-Vision | Small efficient multimodal |
| Gemma 3 | Google open multimodal |
| MiniCPM-V | Mobile-friendly multimodal |
| PaliGemma 2 | Google vision-language |
| `transformers.AutoModelForVision2Seq` | Universal interface |

---

#### Lesson 06.04 — Multimodal Fine-Tuning
**File**: `_14_06_04_multimodal_fine_tuning.md`

| Topics | Subtopics |
|---|---|
| Multimodal SFT data | Image + instruction + answer |
| `LLaVA-NeXT` training | Stage 1 + Stage 2 |
| LoRA for multimodal | Target vision encoder + LLM |
| `LLaMA-Factory` | Multimodal fine-tuning framework |
| `xtuner` | Efficient multimodal SFT |
| Evaluation | MMBench, MMMU, DocVQA |
| Custom vision SFT | Medical images, satellite |

---

#### Lesson 06.05 — Video LLMs
**File**: `_14_06_05_video_llms.md`

| Topics | Subtopics |
|---|---|
| Video understanding challenge | Temporal, long duration |
| Video-LLaVA | Unified image + video model |
| Qwen2.5-VL video | Dynamic FPS, long video |
| VideoChat2 | Instruction-tuned video model |
| LLaVA-NeXT-Video | Video extension of LLaVA |
| Frame sampling | Uniform, key-frame, dense |
| Video benchmarks | EgoSchema, MVBench, Video-MME |

---

#### Lesson 06.06 — Audio and Speech LLMs
**File**: `_14_06_06_audio_speech_llms.md`

| Topics | Subtopics |
|---|---|
| Whisper | OpenAI ASR, multilingual |
| `transformers.WhisperForConditionalGeneration` | Transcription |
| Qwen2-Audio | Native audio LLM |
| WavLLM | Wave-to-language model |
| Gemini Audio | Multimodal audio understanding |
| Speech synthesis | TTS: VoiceCraft, F5-TTS |
| SpeechLM | Joint speech + text model |

---

#### Lesson 06.07 — Omni and Any-Modality Models
**File**: `_14_06_07_omni_any_modality_models.md`

| Topics | Subtopics |
|---|---|
| GPT-4o | Native omni, no pipeline |
| Gemini 2.0 Flash | Real-time omni model |
| InternOmni | Open omni model |
| MiniOmni | Streaming real-time omni |
| Unified tokenization | Discrete visual/audio tokens |
| Any-to-Any generation | Text → image → audio → video |

---

## MODULE 07 — LLM Evaluation and Safety

**Folder**: `_14_07_llm_evaluation_and_safety/`  
**Lesson Count**: 7  
**Learning Order**: 7th

### Lessons

#### Lesson 07.01 — LLM Benchmarks
**File**: `_14_07_01_llm_benchmarks.md`

| Topics | Subtopics |
|---|---|
| MMLU | 57 subjects, 0-shot and 5-shot |
| HellaSwag | Commonsense completion |
| ARC-C/ARC-E | Grade-school science |
| WinoGrande | Winograd schema |
| GSM8K / MATH | Mathematical reasoning |
| HumanEval | Code generation pass@k |
| BIG-Bench Hard | 23 challenging tasks |
| `lm-evaluation-harness` | `lm_eval --model hf --tasks` |

---

#### Lesson 07.02 — LLM-as-Judge Evaluation
**File**: `_14_07_02_llm_as_judge_evaluation.md`

| Topics | Subtopics |
|---|---|
| MT-Bench | 80 multi-turn, GPT-4 judge |
| AlpacaEval | Win rate vs GPT-4 |
| Arena-Hard | 500 hard, judge |
| LLM judge prompts | Reference-free vs reference-based |
| Pairwise vs pointwise | Comparison vs scalar score |
| Position bias | Swap order, average |
| `fastchat.llm_judge` | MT-Bench evaluation toolkit |

---

#### Lesson 07.03 — Hallucination Detection and Mitigation
**File**: `_14_07_03_hallucination_detection_mitigation.md`

| Topics | Subtopics |
|---|---|
| Hallucination taxonomy | Factual, faithful, intrinsic, extrinsic |
| TruthfulQA | Measuring truthfulness |
| HALLUSION BENCH | Vision-language hallucination |
| SelfCheckGPT | Consistency-based detection |
| FAVA | Fine-grained attribution verification |
| Mitigation | RAG, citation, factuality fine-tuning |
| `FactScore` | Atomic fact verification |

---

#### Lesson 07.04 — LLM Safety and Red Teaming
**File**: `_14_07_04_llm_safety_red_teaming.md`

| Topics | Subtopics |
|---|---|
| Harm categories | Violence, CSAM, weapons, bias |
| Red teaming | Adversarial prompt generation |
| `garak` | Automated LLM vulnerability scanner |
| `promptfoo` | Prompt testing + red team |
| Jailbreak taxonomy | DAN, roleplay, suffix, multilingual |
| Automated red teaming | PAIR, TAP, GCG |
| Safety fine-tuning | HH-RLHF, BeaverTails |

---

#### Lesson 07.05 — Bias and Fairness in LLMs
**File**: `_14_07_05_bias_fairness_llms.md`

| Topics | Subtopics |
|---|---|
| Types of bias | Gender, racial, religious, occupational |
| BBQ | Bias Benchmark for QA |
| WinoBias | Gender bias in coreference |
| BOLD | Bias in open-ended language generation |
| Measurement | Counterfactual data, stereotype score |
| Debiasing strategies | Data filtering, RLHF debiasing |
| Representation evaluation | Token probability gaps |

---

#### Lesson 07.06 — Responsible AI and Governance
**File**: `_14_07_06_responsible_ai_governance.md`

| Topics | Subtopics |
|---|---|
| EU AI Act | Risk tiers, GPAI obligations |
| Model cards | `huggingface.co/models`, metadata |
| Datasheets for datasets | Gebru et al. framework |
| Transparency reports | Anthropic, OpenAI, Google |
| Watermarking | KGW watermark, SynthID |
| C2PA | Coalition for Content Provenance |
| NIST AI RMF | Risk management framework |

---

#### Lesson 07.07 — LLM Memorization and Privacy
**File**: `_14_07_07_llm_memorization_privacy.md`

| Topics | Subtopics |
|---|---|
| Memorization definition | Extractable training data |
| Extraction attacks | Carlini et al., verbatim extraction |
| Membership inference | Is this data in training set? |
| Differential privacy | DP-SGD for LLM training |
| Machine unlearning | TOFU dataset, forget-retain split |
| PII filtering | Scrub personal data from training |
| GDPR right to erasure | Technical implementation |

---

## MODULE 08 — LLM Inference and Serving

**Folder**: `_14_08_llm_inference_and_serving/`  
**Lesson Count**: 7  
**Learning Order**: 8th

### Lessons

#### Lesson 08.01 — LLM Inference Fundamentals
**File**: `_14_08_01_llm_inference_fundamentals.md`

| Topics | Subtopics |
|---|---|
| Autoregressive generation | Token-by-token, KV cache |
| Prefill vs decode | Batched prefill, sequential decode |
| KV cache memory | `n_layers × n_heads × seq_len × d_head × 2` |
| Throughput vs latency | Batch size tradeoff |
| TTFT / TPOT | Time to first token, time per output token |
| `transformers.pipeline` | Simple inference |
| `TextGenerationPipeline` | `max_new_tokens`, `do_sample` |

---

#### Lesson 08.02 — vLLM
**File**: `_14_08_02_vllm.md`

| Topics | Subtopics |
|---|---|
| PagedAttention | Non-contiguous KV cache pages |
| vLLM server | `python -m vllm.entrypoints.openai.api_server` |
| OpenAI-compatible API | Drop-in replacement |
| Continuous batching | Dynamic batching for high throughput |
| Prefix caching | KV prefix reuse |
| Multi-GPU | Tensor parallel inference |
| Speculative decoding | Draft + verify for speedup |
| Quantized models | GPTQ + AWQ in vLLM |

---

#### Lesson 08.03 — Text Generation Inference (TGI)
**File**: `_14_08_03_text_generation_inference_tgi.md`

| Topics | Subtopics |
|---|---|
| TGI by HuggingFace | Production inference server |
| Flash Attention 2 | Built-in |
| Continuous batching | Dynamic scheduling |
| `docker` deployment | `ghcr.io/huggingface/text-generation-inference` |
| Streaming | SSE streaming responses |
| LoRA serving | Dynamic LoRA adapter switching |
| Quantization | GPTQ, AWQ, FP8 in TGI |

---

#### Lesson 08.04 — Ollama and Local Inference
**File**: `_14_08_04_ollama_local_inference.md`

| Topics | Subtopics |
|---|---|
| `ollama` | Local LLM runner, GGUF backend |
| `ollama pull` | Download models from registry |
| `ollama run` | Interactive shell |
| Ollama OpenAI-compatible API | `localhost:11434/v1` |
| GGUF format | `llama.cpp` quantized models |
| `llama-cpp-python` | Python bindings |
| Modelfile | Custom system prompt, parameters |

---

#### Lesson 08.05 — Speculative Decoding
**File**: `_14_08_05_speculative_decoding.md`

| Topics | Subtopics |
|---|---|
| Speculative decoding concept | Draft model generates N tokens |
| Verification step | Target model checks in parallel |
| Acceptance rate | γ tokens accepted on average |
| Draft model selection | Small model same family |
| `vllm` speculative | `speculative_model` parameter |
| Medusa | Multi-head draft, no separate model |
| EAGLE | Extrapolation algorithm |
| Speedup | 2-3× with same quality |

---

#### Lesson 08.06 — LLM Batching and Scheduling
**File**: `_14_08_06_llm_batching_scheduling.md`

| Topics | Subtopics |
|---|---|
| Static batching | Wait → full batch → process |
| Continuous batching | Insert new requests mid-stream |
| Chunked prefill | Split long prefill into chunks |
| Priority scheduling | SLA-aware request routing |
| Multi-model serving | Model switching, routing |
| Load balancing | Round-robin, least-pending |
| `litellm` proxy | Multi-provider gateway |

---

#### Lesson 08.07 — LLM API Gateway
**File**: `_14_08_07_llm_api_gateway.md`

| Topics | Subtopics |
|---|---|
| `litellm` | 100+ LLM provider unification |
| `litellm` proxy | OpenAI-compatible gateway |
| Cost tracking | Per-request token cost |
| Rate limiting | Per-user, per-model limits |
| Fallbacks | `fallbacks` config, retry logic |
| Caching | `cache_responses=True`, Redis |
| Logging | Langfuse, Langsmith integration |

---

## MODULE 09 — LLM Compression and Edge

**Folder**: `_14_09_llm_compression_and_edge/`  
**Lesson Count**: 6  
**Learning Order**: 9th

### Lessons

#### Lesson 09.01 — GPTQ Quantization
**File**: `_14_09_01_gptq_quantization.md`

| Topics | Subtopics |
|---|---|
| GPTQ algorithm | Layer-wise quantization, OBQ |
| `auto-gptq` | `AutoGPTQForCausalLM.quantize()` |
| W4A16 | 4-bit weights, 16-bit activations |
| Calibration dataset | `c4`, `wikitext2` |
| GPTQ in vLLM | `--quantization gptq` |
| Accuracy vs memory | 4-bit GPTQ vs FP16 |

---

#### Lesson 09.02 — AWQ Quantization
**File**: `_14_09_02_awq_quantization.md`

| Topics | Subtopics |
|---|---|
| AWQ concept | Activation-aware weight quantization |
| `autoawq` | `AutoAWQForCausalLM.quantize()` |
| Scale search | Per-channel scale for salient weights |
| AWQ in vLLM | `--quantization awq` |
| AWQ vs GPTQ | Speed, accuracy comparison |
| ExLlamaV2 | Fast AWQ/GPTQ inference kernel |

---

#### Lesson 09.03 — GGUF and llama.cpp
**File**: `_14_09_03_gguf_llama_cpp.md`

| Topics | Subtopics |
|---|---|
| GGUF format | Unified quantized model format |
| `llama.cpp` | CPU/GPU inference, Metal, CUDA |
| `llama-cpp-python` | Python bindings, OpenAI-compatible |
| Quantization levels | Q4_K_M, Q5_K_M, Q8_0 |
| `convert_hf_to_gguf.py` | Convert HF models to GGUF |
| `imatrix` | Importance matrix for better quant |
| Metal/Apple Silicon | M1/M2/M3 GPU inference |

---

#### Lesson 09.04 — Knowledge Distillation for LLMs
**File**: `_14_09_04_knowledge_distillation_llms.md`

| Topics | Subtopics |
|---|---|
| Black-box distillation | Teacher generates data, student trains |
| White-box distillation | Token KL divergence |
| DistilGPT2 | 6-layer GPT-2 distilled |
| TinyLLaMA | 1.1B distilled from LLaMA |
| DeepSeek-R1 distillation | Reasoning distillation to Qwen/LLaMA |
| Speculative distillation | Draft model trained via distillation |

---

#### Lesson 09.05 — Pruning and Sparsity in LLMs
**File**: `_14_09_05_pruning_sparsity_llms.md`

| Topics | Subtopics |
|---|---|
| Unstructured pruning | SparseGPT, Wanda |
| Structured pruning | LLM-Pruner, layer/head pruning |
| SparseGPT | One-shot unstructured pruning |
| Wanda | Weights × activations magnitude |
| 2:4 sparsity | NVIDIA sparse tensor core format |
| Pruning + quantization | Combined compression |

---

#### Lesson 09.06 — Edge Deployment of LLMs
**File**: `_14_09_06_edge_deployment_llms.md`

| Topics | Subtopics |
|---|---|
| On-device LLMs | Phi-3-mini, Gemma-2-2B, SmolLM |
| `executorch` | Meta's mobile LLM deployment |
| `llama.cpp` on Android/iOS | Mobile inference |
| Apple MLX | Apple Silicon optimized framework |
| Jetson Orin | NVIDIA edge GPU inference |
| LLM in browser | WebGPU, `web-llm`, `mlc-llm` |
| Raspberry Pi | `llama.cpp` CPU inference |

---

## MODULE 10 — Industry Projects

**Folder**: `_14_10_industry_projects/`  
**Lesson Count**: 6  
**Learning Order**: 10th (Capstone)

### Lessons

#### Lesson 10.01 — Custom Chat Assistant (QLoRA Fine-Tuned)
**File**: `_14_10_01_custom_chat_assistant_qlora.md`

| Topics | Subtopics |
|---|---|
| Task | Domain-specific customer support assistant |
| Model | Llama-3.2-3B + QLoRA |
| Data | ShareGPT-style domain conversations |
| Training | `trl.SFTTrainer` + `BitsAndBytesConfig` |
| Deployment | vLLM + FastAPI |
| Evaluation | MT-Bench domain subset, win rate |

---

#### Lesson 10.02 — DPO-Aligned Model
**File**: `_14_10_02_dpo_aligned_model.md`

| Topics | Subtopics |
|---|---|
| Task | Align base model to be helpful + safe |
| Data | UltraFeedback preference dataset |
| Pipeline | SFT → DPO |
| `trl.DPOTrainer` | Full training code |
| Evaluation | AlpacaEval win rate before/after |
| Safety check | ToxiGen before/after |

---

#### Lesson 10.03 — Code Generation Service
**File**: `_14_10_03_code_generation_service.md`

| Topics | Subtopics |
|---|---|
| Task | Function generation + unit test |
| Model | CodeLlama-7B-Instruct |
| API | FastAPI `/generate` endpoint |
| Evaluation | HumanEval pass@1 |
| FIM support | Fill-in-the-middle endpoint |
| Deployment | vLLM + Docker |

---

#### Lesson 10.04 — Multimodal Document Analyst
**File**: `_14_10_04_multimodal_document_analyst.md`

| Topics | Subtopics |
|---|---|
| Task | Upload PDF/image → Q&A + summary |
| Vision model | InternVL2-8B or Qwen2.5-VL-7B |
| Pipeline | Image → LVLM → answer |
| Multi-page | Iterate pages, aggregate answers |
| API | FastAPI `/analyze` multipart upload |
| Use cases | Invoice, contract, medical report |

---

#### Lesson 10.05 — On-Device LLM App
**File**: `_14_10_05_on_device_llm_app.md`

| Topics | Subtopics |
|---|---|
| Task | Private local assistant, no cloud |
| Model | Phi-3-mini GGUF Q4_K_M |
| Runtime | `llama-cpp-python` |
| UI | Gradio chat interface |
| Performance | Tokens/s on CPU vs Apple M1 |
| Use case | Offline enterprise assistant |

---

#### Lesson 10.06 — LLM Evaluation Pipeline (Capstone)
**File**: `_14_10_06_llm_evaluation_pipeline_capstone.md`

| Topics | Subtopics |
|---|---|
| Task | Evaluate 3 models on 5 benchmarks |
| Benchmarks | MMLU, GSM8K, HumanEval, MT-Bench, TruthfulQA |
| Tools | `lm-evaluation-harness`, `fastchat` |
| LLM-as-judge | GPT-4o as evaluator |
| Dashboard | W&B comparison table |
| Report | Leaderboard, analysis, recommendations |

---

## Full Folder Structure

```
docs/curriculum/_14_generative_ai_llms/
│
├── _14_01_llm_architecture_internals/
│   ├── _14_01_01_transformer_scaling_laws.md
│   ├── _14_01_02_advanced_positional_encodings.md
│   ├── _14_01_03_efficient_attention_llms.md
│   ├── _14_01_04_mixture_of_experts_moe.md
│   ├── _14_01_05_llm_normalization_ffn_variants.md
│   ├── _14_01_06_tokenization_in_llms.md
│   ├── _14_01_07_llm_model_families.md
│   └── _14_01_08_llm_training_infrastructure.md
│
├── _14_02_llm_pretraining/
│   ├── _14_02_01_pretraining_data_preparation.md
│   ├── _14_02_02_causal_lm_pretraining.md
│   ├── _14_02_03_continued_pretraining_domain.md
│   ├── _14_02_04_training_small_llms_from_scratch.md
│   ├── _14_02_05_instruction_pretraining.md
│   ├── _14_02_06_evaluation_during_pretraining.md
│   └── _14_02_07_open_pretraining_datasets.md
│
├── _14_03_supervised_fine_tuning/
│   ├── _14_03_01_instruction_tuning.md
│   ├── _14_03_02_sft_data_preparation.md
│   ├── _14_03_03_full_fine_tuning_trl.md
│   ├── _14_03_04_qlora_fine_tuning.md
│   ├── _14_03_05_chat_fine_tuning.md
│   ├── _14_03_06_math_reasoning_fine_tuning.md
│   ├── _14_03_07_code_fine_tuning.md
│   └── _14_03_08_continual_multitask_fine_tuning.md
│
├── _14_04_alignment_rlhf_dpo/
│   ├── _14_04_01_rlhf_overview_instructgpt.md
│   ├── _14_04_02_reward_model_training.md
│   ├── _14_04_03_ppo_fine_tuning.md
│   ├── _14_04_04_direct_preference_optimization_dpo.md
│   ├── _14_04_05_orpo_simpo_dpo_variants.md
│   ├── _14_04_06_constitutional_ai_rlaif.md
│   ├── _14_04_07_process_reward_models.md
│   └── _14_04_08_evaluation_aligned_models.md
│
├── _14_05_prompt_engineering/
│   ├── _14_05_01_prompt_engineering_fundamentals.md
│   ├── _14_05_02_chain_of_thought_prompting.md
│   ├── _14_05_03_structured_output_json_mode.md
│   ├── _14_05_04_advanced_prompting_techniques.md
│   ├── _14_05_05_prompt_optimization_autoprompt.md
│   ├── _14_05_06_context_window_management.md
│   └── _14_05_07_prompt_security_robustness.md
│
├── _14_06_multimodal_llms/
│   ├── _14_06_01_vision_language_pretraining.md
│   ├── _14_06_02_llava_visual_instruction_tuning.md
│   ├── _14_06_03_strong_open_multimodal_llms.md
│   ├── _14_06_04_multimodal_fine_tuning.md
│   ├── _14_06_05_video_llms.md
│   ├── _14_06_06_audio_speech_llms.md
│   └── _14_06_07_omni_any_modality_models.md
│
├── _14_07_llm_evaluation_and_safety/
│   ├── _14_07_01_llm_benchmarks.md
│   ├── _14_07_02_llm_as_judge_evaluation.md
│   ├── _14_07_03_hallucination_detection_mitigation.md
│   ├── _14_07_04_llm_safety_red_teaming.md
│   ├── _14_07_05_bias_fairness_llms.md
│   ├── _14_07_06_responsible_ai_governance.md
│   └── _14_07_07_llm_memorization_privacy.md
│
├── _14_08_llm_inference_and_serving/
│   ├── _14_08_01_llm_inference_fundamentals.md
│   ├── _14_08_02_vllm.md
│   ├── _14_08_03_text_generation_inference_tgi.md
│   ├── _14_08_04_ollama_local_inference.md
│   ├── _14_08_05_speculative_decoding.md
│   ├── _14_08_06_llm_batching_scheduling.md
│   └── _14_08_07_llm_api_gateway.md
│
├── _14_09_llm_compression_and_edge/
│   ├── _14_09_01_gptq_quantization.md
│   ├── _14_09_02_awq_quantization.md
│   ├── _14_09_03_gguf_llama_cpp.md
│   ├── _14_09_04_knowledge_distillation_llms.md
│   ├── _14_09_05_pruning_sparsity_llms.md
│   └── _14_09_06_edge_deployment_llms.md
│
└── _14_10_industry_projects/
    ├── _14_10_01_custom_chat_assistant_qlora.md
    ├── _14_10_02_dpo_aligned_model.md
    ├── _14_10_03_code_generation_service.md
    ├── _14_10_04_multimodal_document_analyst.md
    ├── _14_10_05_on_device_llm_app.md
    └── _14_10_06_llm_evaluation_pipeline_capstone.md
```

---

## Learning Order

```
01 LLM Architecture Internals  (Scaling, RoPE, GQA, MoE, SwiGLU)
    ↓
02 LLM Pretraining  (Data → CLM → Domain → Small LLM from scratch)
    ↓
03 Supervised Fine-Tuning  (Instruction → QLoRA → Chat → Math → Code)
    ↓
04 Alignment: RLHF & DPO  (RM → PPO → DPO → ORPO → PRM)
    ↓
05 Prompt Engineering  (CoT → Structured → DSPy → Security)
    ↓
06 Multimodal LLMs  (VLP → LLaVA → Video → Audio → Omni)
    ↓
07 LLM Evaluation & Safety  (Benchmarks → Judge → Hallucination → Red Team)
    ↓
08 LLM Inference & Serving  (vLLM → TGI → Ollama → Speculative → Gateway)
    ↓
09 LLM Compression & Edge  (GPTQ → AWQ → GGUF → Edge Deploy)
    ↓
10 Industry Projects (Capstone)
```

---

## Summary Statistics

| Module | Title | Lessons |
|---|---|---|
| 01 | LLM Architecture Internals | 8 |
| 02 | LLM Pretraining | 7 |
| 03 | Supervised Fine-Tuning | 8 |
| 04 | Alignment: RLHF & DPO | 8 |
| 05 | Prompt Engineering | 7 |
| 06 | Multimodal LLMs | 7 |
| 07 | LLM Evaluation & Safety | 7 |
| 08 | LLM Inference & Serving | 7 |
| 09 | LLM Compression & Edge | 6 |
| 10 | Industry Projects | 6 |
| **TOTAL** | | **71 lessons** |

---

## Phase 6 Handoff (RAG Engineering)

Nodes introduced in Phase 5 and extended in Phase 6:
- LLM Inference (vLLM, TGI) → RAG backend LLM
- Prompt Engineering → RAG prompt templates
- Context window management → RAG context packing
- Semantic search (from Phase 4) → RAG retriever
- Hallucination mitigation → RAG factuality improvement
