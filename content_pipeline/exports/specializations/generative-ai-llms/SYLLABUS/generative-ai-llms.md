# Generative AI and LLMs — Master Syllabus

---

# Course Information

**Course Name:** Generative AI and LLMs

**Category:** Specialization Course

**Learning Path(s):**

- AI Engineer
- Generative AI Engineering
- ML Engineer

**Difficulty:** Beginner

**Estimated Duration:** 25 Hours

**Prerequisites:**

- Core Python
- Deep Learning
- Natural Language Processing

**Course Status:** COMING_SOON

---

# Module 1 — LLM Architecture

## Lesson 1.1 — Transformer Scaling Laws

**Course Coverage:** 🟢 Covered in Class

### Topics

- Chinchilla
- Kaplan
- Emergent Abilities
- Mfu
- Compute Optimal

## Lesson 1.2 — Advanced Positional Encodings

**Course Coverage:** 🟢 Covered in Class

### Topics

- Rope
- Alibi
- Yarn
- Longrope
- Context Extension
- Interpolation

## Lesson 1.3 — Efficient Attention in LLMs

**Course Coverage:** 🟢 Covered in Class

### Topics

- Mha
- Mqa
- Gqa
- Flash Attention
- Paged Attention
- Kv Cache
- Sliding Window

## Lesson 1.4 — Mixture of Experts MoE

**Course Coverage:** 🟢 Covered in Class

### Topics

- Moe
- Router
- Top K
- Mixtral
- Deepseek Moe
- Expert Parallelism
- Sparse

## Lesson 1.5 — LLM Normalization and FFN Variants

**Course Coverage:** 🟢 Covered in Class

### Topics

- Pre Ln
- Rmsnorm
- Swiglu
- Geglu
- Ffn Expansion
- Parallel Attn

## Lesson 1.6 — Tokenization in LLMs

**Course Coverage:** 🟢 Covered in Class

### Topics

- Tiktoken
- Sentencepiece
- Chat Template
- Special Tokens
- Vocab Extension
- Token Efficiency

## Lesson 1.7 — LLM Model Families

**Course Coverage:** 🟢 Covered in Class

### Topics

- Llama
- Mistral
- Gemma
- Phi
- Qwen
- Deepseek
- Command R

## Lesson 1.8 — LLM Training Infrastructure

**Course Coverage:** 🟢 Covered in Class

### Topics

- 3d Parallel
- Tensor Parallel
- Pipeline Parallel
- Deepspeed
- Fsdp
- Megatron
- Gradient Checkpointing

---

# Module 2 — LLM Pretraining

## Lesson 2.1 — Pretraining Data Preparation

**Course Coverage:** 🟢 Covered in Class

### Topics

- Common Crawl
- Minhash
- Deduplication
- Language Filter
- Datatrove
- Dolma
- Data Mixing

## Lesson 2.2 — Causal Language Model Pretraining

**Course Coverage:** 🟢 Covered in Class

### Topics

- Clm
- Sequence Packing
- Constant Length Dataset
- Warmup
- Olmo
- Nanogpt

## Lesson 2.3 — Continued Pretraining and Domain Adaptation

**Course Coverage:** 🟢 Covered in Class

### Topics

- Dapt
- Biomedlm
- Saullm
- Code Llama
- Catastrophic Forgetting
- Replay

## Lesson 2.4 — Training Small LLMs from Scratch

**Course Coverage:** 🟢 Covered in Class

### Topics

- Nanogpt
- Litgpt
- Memmap
- Ddp
- Mixed Precision
- Perplexity Eval

## Lesson 2.5 — Instruction Pretraining

**Course Coverage:** 🟢 Covered in Class

### Topics

- Flan
- Self Instruct
- Metacl
- Instruction Upsampling
- Multitask Pretrain

## Lesson 2.6 — Evaluation During Pretraining

**Course Coverage:** 🟢 Covered in Class

### Topics

- Perplexity
- Bpc
- Lm Eval Harness
- Loss Spike
- Wandb
- Checkpoint Comparison

## Lesson 2.7 — Open Pretraining Datasets

**Course Coverage:** 🟢 Covered in Class

### Topics

- The Pile
- Redpajama
- Dclm
- Fineweb
- Dolma
- Roots
- The Stack

---

# Module 3 — Supervised Fine-Tuning

## Lesson 3.1 — Instruction Tuning

**Course Coverage:** 🟢 Covered in Class

### Topics

- Flan
- Self Instruct
- Alpaca
- Wizardlm
- Openhermes
- SFT Trainer
- Chat Template

## Lesson 3.2 — SFT Data Preparation

**Course Coverage:** 🟢 Covered in Class

### Topics

- Sharegpt
- Openai Chat
- Deita
- Quality Filtering
- Ultrachat
- Openorca
- Synthetic Data

## Lesson 3.3 — Full Fine-Tuning with TRL

**Course Coverage:** 🟢 Covered in Class

### Topics

- Trl
- SFT Trainer
- SFT Config
- Accelerate
- Multi GPU
- Wandb
- Save Pretrained

## Lesson 3.4 — QLoRA Fine-Tuning

**Course Coverage:** 🟢 Covered in Class

### Topics

- Qlora
- Bitsandbytes
- Nf4
- Prepare Kbit
- Lora Config
- Merge Unload
- Vram

## Lesson 3.5 — Chat Fine-Tuning

**Course Coverage:** 🟢 Covered in Class

### Topics

- Chat Format
- Loss Masking
- Completion Only Lm
- Multi Turn
- Sharegpt Format
- Domain Chat

## Lesson 3.6 — Math and Reasoning Fine-Tuning

**Course Coverage:** 🟢 Covered in Class

### Topics

- Gsm8k
- Rejection Sampling
- Process Reward
- Metamath
- Deepseek R1 Distill

## Lesson 3.7 — Code Fine-Tuning

**Course Coverage:** 🟢 Covered in Class

### Topics

- Code Alpaca
- Oss Instruct
- Fim
- Starcoder2 Instruct
- Humaneval
- Evalplus

## Lesson 3.8 — Continual and Multi-Task Fine-Tuning

**Course Coverage:** 🟢 Covered in Class

### Topics

- Catastrophic Forgetting
- Task Specific Lora
- Multi Adapter
- Ewc
- Molor
- Data Replay

---

# Module 4 — Alignment

## Lesson 4.1 — RLHF Overview and InstructGPT

**Course Coverage:** 🟢 Covered in Class

### Topics

- 3h
- Instructgpt
- SFT Rm Ppo
- Reward Hacking
- Kl Penalty
- Constitutional AI

## Lesson 4.2 — Reward Model Training

**Course Coverage:** 🟢 Covered in Class

### Topics

- Bradley Terry
- Reward Trainer
- Preference Dataset
- Anthropic Hh
- Rm Evaluation

## Lesson 4.3 — PPO Fine-Tuning

**Course Coverage:** 🟢 Covered in Class

### Topics

- Ppo
- Ppo Trainer
- Reference Model
- Value Model
- Reward Normalization
- Kl Adaptive

## Lesson 4.4 — Direct Preference Optimization DPO

**Course Coverage:** 🟢 Covered in Class

### Topics

- DPO
- DPO Trainer
- Beta
- Chosen
- Rejected
- Ultrafeedback
- Win Rate

## Lesson 4.5 — ORPO SimPO and DPO Variants

**Course Coverage:** 🟢 Covered in Class

### Topics

- Orpo
- Simpo
- Ipo
- Kto
- Cpo
- No Reference Model
- Length Normalization

## Lesson 4.6 — Constitutional AI and RLAIF

**Course Coverage:** 🟢 Covered in Class

### Topics

- Constitutional AI
- Rlaif
- Self Critique
- LLM Judge
- Scalable Oversight
- Debate

## Lesson 4.7 — Process Reward Models

**Course Coverage:** 🟢 Covered in Class

### Topics

- Prm
- Outcome Rm
- Math Shepherd
- Best Of N
- Mcts
- Step Level Feedback

## Lesson 4.8 — Evaluation of Aligned Models

**Course Coverage:** 🟢 Covered in Class

### Topics

- Mt Bench
- Alpacaeval
- Arena Hard
- Ifeval
- Lmsys
- Safety Eval
- Toxigen

---

# Module 5 — Prompt Engineering

## Lesson 5.1 — Prompt Engineering Fundamentals

**Course Coverage:** 🟢 Covered in Class

### Topics

- Zero Shot
- Few Shot
- System Prompt
- Prompt Sensitivity
- Temperature
- Openai Sdk

## Lesson 5.2 — Chain-of-Thought Prompting

**Course Coverage:** 🟢 Covered in Class

### Topics

- Cot
- Zero Shot Cot
- Self Consistency
- Least To Most
- Tree Of Thought
- Plan Solve

## Lesson 5.3 — Structured Output and JSON Mode

**Course Coverage:** 🟢 Covered in Class

### Topics

- Json Mode
- Structured Outputs
- Instructor
- Outlines
- Function Calling
- Xml Output

## Lesson 5.4 — Advanced Prompting Techniques

**Course Coverage:** 🟢 Covered in Class

### Topics

- React
- Reflexion
- Pal
- Generated Knowledge
- Maieutic
- Directional Stimulus

## Lesson 5.5 — Prompt Optimization and AutoPrompt

**Course Coverage:** 🟢 Covered in Class

### Topics

- Dspy
- Miprov2
- Textgrad
- Meta Prompting
- Eval Driven
- Automatic Prompt

## Lesson 5.6 — Context Window Management

**Course Coverage:** 🟢 Covered in Class

### Topics

- Context Limits
- Lost In Middle
- Retrieval Augmentation
- Summarization Compression
- Chunking
- Tiktoken

## Lesson 5.7 — Prompt Security and Robustness

**Course Coverage:** 🟢 Covered in Class

### Topics

- Prompt Injection
- Jailbreaking
- Indirect Injection
- Promptfoo
- Garak
- Guardrails

---

# Module 6 — Multimodal LLMs

## Lesson 6.1 — Vision-Language Pretraining

**Course Coverage:** 🟢 Covered in Class

### Topics

- Clip
- Align
- Flava
- Coca
- Flamingo
- Q Former
- Blip2 Bridge

## Lesson 6.2 — LLaVA and Visual Instruction Tuning

**Course Coverage:** 🟢 Covered in Class

### Topics

- Llava
- Llava 1.5
- Llava Next
- Mlp Projector
- Sharegpt4v
- Stage 1 2

## Lesson 6.3 — Strong Open Multimodal LLMs

**Course Coverage:** 🟢 Covered in Class

### Topics

- Internvl
- Qwen2.5 Vl
- Phi 4 Vision
- Gemma3
- Minicpm V
- Paligemma2

## Lesson 6.4 — Multimodal Fine-Tuning

**Course Coverage:** 🟢 Covered in Class

### Topics

- Multimodal SFT
- Llama Factory
- Xtuner
- Lora Vision
- Mmbench
- Mmmu
- Docvqa

## Lesson 6.5 — Video LLMs

**Course Coverage:** 🟢 Covered in Class

### Topics

- Video Llava
- Qwen2.5 Vl Video
- Videochat2
- Frame Sampling
- Egoscehma
- Video Mme

## Lesson 6.6 — Audio and Speech LLMs

**Course Coverage:** 🟢 Covered in Class

### Topics

- Whisper
- Qwen2 Audio
- Wavllm
- Voicecraft
- F5 Tts
- Speechlm

## Lesson 6.7 — Omni and Any-Modality Models

**Course Coverage:** 🟢 Covered in Class

### Topics

- Gpt 4o
- Gemini 2.0
- Internomni
- Miniomni
- Discrete Tokens
- Any To Any

---

# Module 7 — Evaluation and Safety

## Lesson 7.1 — LLM Benchmarks

**Course Coverage:** 🟢 Covered in Class

### Topics

- Mmlu
- Hellaswag
- Arc
- Winogrande
- Gsm8k
- Humaneval
- Big Bench
- Lm Eval Harness

## Lesson 7.2 — LLM-as-Judge Evaluation

**Course Coverage:** 🟢 Covered in Class

### Topics

- Mt Bench
- Alpacaeval
- Arena Hard
- Pairwise
- Pointwise
- Position Bias
- Fastchat

## Lesson 7.3 — Hallucination Detection and Mitigation

**Course Coverage:** 🟢 Covered in Class

### Topics

- Truthfulqa
- Selfcheckgpt
- Fava
- Factscore
- RAG Grounding
- Citation
- Hallusion

## Lesson 7.4 — LLM Safety and Red Teaming

**Course Coverage:** 🟢 Covered in Class

### Topics

- Garak
- Promptfoo
- Jailbreak
- Pair
- Tap
- Gcg
- Beavertails
- Hh RLHF

## Lesson 7.5 — Bias and Fairness in LLMs

**Course Coverage:** 🟢 Covered in Class

### Topics

- Bbq
- Winobias
- Bold
- Counterfactual
- Debiasing
- RLHF Debiasing
- Representation

## Lesson 7.6 — Responsible AI and Governance

**Course Coverage:** 🟢 Covered in Class

### Topics

- Eu AI Act
- Model Cards
- Datasheets
- Watermarking
- Synthid
- C2pa
- Nist AI Rmf

## Lesson 7.7 — LLM Memorization and Privacy

**Course Coverage:** 🟢 Covered in Class

### Topics

- Extraction Attack
- Membership Inference
- Dp Sgd
- Machine Unlearning
- Pii Filter
- Tofu

---

# Module 8 — Inference and Serving

## Lesson 8.1 — LLM Inference Fundamentals

**Course Coverage:** 🟢 Covered in Class

### Topics

- Autoregressive
- Kv Cache
- Prefill
- Decode
- Ttft
- Tpot
- Throughput Latency

## Lesson 8.2 — vLLM

**Course Coverage:** 🟢 Covered in Class

### Topics

- Paged Attention
- Continuous Batching
- Prefix Caching
- Tensor Parallel
- Speculative
- Gptq Awq

## Lesson 8.3 — Text Generation Inference TGI

**Course Coverage:** 🟢 Covered in Class

### Topics

- Tgi
- Flash Attention
- Streaming
- Lora Serving
- Dynamic Adapter
- Docker

## Lesson 8.4 — Ollama and Local Inference

**Course Coverage:** 🟢 Covered in Class

### Topics

- Ollama
- Gguf
- Llama Cpp
- Modelfile
- Local API
- Llama Cpp Python

## Lesson 8.5 — Speculative Decoding

**Course Coverage:** 🟢 Covered in Class

### Topics

- Draft Model
- Verify
- Acceptance Rate
- Medusa
- Eagle
- 2 3x Speedup

## Lesson 8.6 — LLM Batching and Scheduling

**Course Coverage:** 🟢 Covered in Class

### Topics

- Static Batching
- Continuous Batching
- Chunked Prefill
- Priority
- Litellm Proxy
- Load Balance

## Lesson 8.7 — LLM API Gateway

**Course Coverage:** 🟢 Covered in Class

### Topics

- Litellm
- Cost Tracking
- Rate Limiting
- Fallbacks
- Caching
- Langfuse
- Langsmith

---

# Module 9 — LLM Compression

## Lesson 9.1 — GPTQ Quantization

**Course Coverage:** 🟢 Covered in Class

### Topics

- Gptq
- Auto Gptq
- W4a16
- Calibration
- Obq
- Vllm Gptq

## Lesson 9.2 — AWQ Quantization

**Course Coverage:** 🟢 Covered in Class

### Topics

- Awq
- Autoawq
- Scale Search
- Salient Weights
- Exllamav2
- Vllm Awq

## Lesson 9.3 — GGUF and llama.cpp

**Course Coverage:** 🟢 Covered in Class

### Topics

- Gguf
- Llama Cpp
- Q4 K M
- Q5 K M
- Imatrix
- Metal
- Convert Hf Gguf

## Lesson 9.4 — Knowledge Distillation for LLMs

**Course Coverage:** 🟢 Covered in Class

### Topics

- Black Box Distillation
- White Box
- Distilgpt2
- Tinyllama
- Deepseek R1 Distill

## Lesson 9.5 — Pruning and Sparsity in LLMs

**Course Coverage:** 🟢 Covered in Class

### Topics

- Sparsegpt
- Wanda
- LLM Pruner
- 2 4 Sparsity
- Structured Pruning
- Quant Prune

## Lesson 9.6 — Edge Deployment of LLMs

**Course Coverage:** 🟢 Covered in Class

### Topics

- Executorch
- Phi 3 Mini
- Mlx
- Jetson
- Web LLM
- Webgpu
- Mlc LLM
- Raspberry Pi

---

# Module 10 — Industry Projects

## Lesson 10.1 — Custom Chat Assistant QLoRA

**Course Coverage:** 🟢 Covered in Class

### Topics

- Qlora
- SFT Trainer
- Vllm
- Fastapi
- Domain Chat
- Win Rate

## Lesson 10.2 — DPO Aligned Model

**Course Coverage:** 🟢 Covered in Class

### Topics

- DPO
- Ultrafeedback
- Alpacaeval
- Toxigen
- SFT DPO Pipeline

## Lesson 10.3 — Code Generation Service

**Course Coverage:** 🟢 Covered in Class

### Topics

- Codellama
- Humaneval
- Fim
- Vllm
- Fastapi
- Docker
- Pass At 1

## Lesson 10.4 — Multimodal Document Analyst

**Course Coverage:** 🟢 Covered in Class

### Topics

- Internvl2
- Qwen2.5 Vl
- Pdf Qa
- Multi Page
- Fastapi
- Invoice
- Contract

## Lesson 10.5 — On-Device LLM App

**Course Coverage:** 🟢 Covered in Class

### Topics

- Phi 3 Mini
- Gguf
- Llama Cpp Python
- Gradio
- Offline
- Apple M1
- Cpu Inference

## Lesson 10.6 — LLM Evaluation Pipeline Capstone

**Course Coverage:** 🟢 Covered in Class

### Topics

- Lm Eval Harness
- Mt Bench
- Fastchat
- LLM As Judge
- Wandb
- Leaderboard

---

# Software & Tools

- Python 3.10+
- PyTorch
- Hugging Face Transformers
- PEFT/LoRA
- vLLM
- OpenAI API

---

# Hardware Requirements

- A computer with a CUDA-capable GPU (or cloud GPU access) recommended

---

# Course Completion Summary

**Estimated Hours:** 25 Hours

**Modules:** 10

**Lessons:** 71

**Difficulty:** Beginner

**Course Status:** COMING_SOON
