import os
BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum\_14_generative_ai_llms'
LESSONS = [
    ("_14_01_llm_architecture_internals","_14_01_01_transformer_scaling_laws.md",1,1,"Transformer Scaling Laws","LLM Architecture",["chinchilla","kaplan","emergent-abilities","mfu","compute-optimal"],"advanced"),
    ("_14_01_llm_architecture_internals","_14_01_02_advanced_positional_encodings.md",1,2,"Advanced Positional Encodings","LLM Architecture",["rope","alibi","yarn","longrope","context-extension","interpolation"],"advanced"),
    ("_14_01_llm_architecture_internals","_14_01_03_efficient_attention_llms.md",1,3,"Efficient Attention in LLMs","LLM Architecture",["mha","mqa","gqa","flash-attention","paged-attention","kv-cache","sliding-window"],"advanced"),
    ("_14_01_llm_architecture_internals","_14_01_04_mixture_of_experts_moe.md",1,4,"Mixture of Experts MoE","LLM Architecture",["moe","router","top-k","mixtral","deepseek-moe","expert-parallelism","sparse"],"advanced"),
    ("_14_01_llm_architecture_internals","_14_01_05_llm_normalization_ffn_variants.md",1,5,"LLM Normalization and FFN Variants","LLM Architecture",["pre-ln","rmsnorm","swiglu","geglu","ffn-expansion","parallel-attn"],"advanced"),
    ("_14_01_llm_architecture_internals","_14_01_06_tokenization_in_llms.md",1,6,"Tokenization in LLMs","LLM Architecture",["tiktoken","sentencepiece","chat-template","special-tokens","vocab-extension","token-efficiency"],"intermediate"),
    ("_14_01_llm_architecture_internals","_14_01_07_llm_model_families.md",1,7,"LLM Model Families","LLM Architecture",["llama","mistral","gemma","phi","qwen","deepseek","command-r"],"intermediate"),
    ("_14_01_llm_architecture_internals","_14_01_08_llm_training_infrastructure.md",1,8,"LLM Training Infrastructure","LLM Architecture",["3d-parallel","tensor-parallel","pipeline-parallel","deepspeed","fsdp","megatron","gradient-checkpointing"],"advanced"),
    ("_14_02_llm_pretraining","_14_02_01_pretraining_data_preparation.md",2,1,"Pretraining Data Preparation","LLM Pretraining",["common-crawl","minhash","deduplication","language-filter","datatrove","dolma","data-mixing"],"advanced"),
    ("_14_02_llm_pretraining","_14_02_02_causal_lm_pretraining.md",2,2,"Causal Language Model Pretraining","LLM Pretraining",["clm","sequence-packing","constant-length-dataset","warmup","olmo","nanogpt"],"advanced"),
    ("_14_02_llm_pretraining","_14_02_03_continued_pretraining_domain.md",2,3,"Continued Pretraining and Domain Adaptation","LLM Pretraining",["dapt","biomedlm","saulLM","code-llama","catastrophic-forgetting","replay"],"advanced"),
    ("_14_02_llm_pretraining","_14_02_04_training_small_llms_from_scratch.md",2,4,"Training Small LLMs from Scratch","LLM Pretraining",["nanogpt","litgpt","memmap","ddp","mixed-precision","perplexity-eval"],"advanced"),
    ("_14_02_llm_pretraining","_14_02_05_instruction_pretraining.md",2,5,"Instruction Pretraining","LLM Pretraining",["flan","self-instruct","metacl","instruction-upsampling","multitask-pretrain"],"advanced"),
    ("_14_02_llm_pretraining","_14_02_06_evaluation_during_pretraining.md",2,6,"Evaluation During Pretraining","LLM Pretraining",["perplexity","bpc","lm-eval-harness","loss-spike","wandb","checkpoint-comparison"],"intermediate"),
    ("_14_02_llm_pretraining","_14_02_07_open_pretraining_datasets.md",2,7,"Open Pretraining Datasets","LLM Pretraining",["the-pile","redpajama","dclm","fineweb","dolma","roots","the-stack"],"intermediate"),
    ("_14_03_supervised_fine_tuning","_14_03_01_instruction_tuning.md",3,1,"Instruction Tuning","Supervised Fine-Tuning",["flan","self-instruct","alpaca","wizardlm","openhermes","sft-trainer","chat-template"],"intermediate"),
    ("_14_03_supervised_fine_tuning","_14_03_02_sft_data_preparation.md",3,2,"SFT Data Preparation","Supervised Fine-Tuning",["sharegpt","openai-chat","deita","quality-filtering","ultrachat","openorca","synthetic-data"],"intermediate"),
    ("_14_03_supervised_fine_tuning","_14_03_03_full_fine_tuning_trl.md",3,3,"Full Fine-Tuning with TRL","Supervised Fine-Tuning",["trl","sft-trainer","sft-config","accelerate","multi-gpu","wandb","save-pretrained"],"intermediate"),
    ("_14_03_supervised_fine_tuning","_14_03_04_qlora_fine_tuning.md",3,4,"QLoRA Fine-Tuning","Supervised Fine-Tuning",["qlora","bitsandbytes","nf4","prepare-kbit","lora-config","merge-unload","vram"],"intermediate"),
    ("_14_03_supervised_fine_tuning","_14_03_05_chat_fine_tuning.md",3,5,"Chat Fine-Tuning","Supervised Fine-Tuning",["chat-format","loss-masking","completion-only-lm","multi-turn","sharegpt-format","domain-chat"],"intermediate"),
    ("_14_03_supervised_fine_tuning","_14_03_06_math_reasoning_fine_tuning.md",3,6,"Math and Reasoning Fine-Tuning","Supervised Fine-Tuning",["gsm8k","rejection-sampling","process-reward","metamath","deepseek-r1-distill"],"advanced"),
    ("_14_03_supervised_fine_tuning","_14_03_07_code_fine_tuning.md",3,7,"Code Fine-Tuning","Supervised Fine-Tuning",["code-alpaca","oss-instruct","fim","starcoder2-instruct","humaneval","evalplus"],"intermediate"),
    ("_14_03_supervised_fine_tuning","_14_03_08_continual_multitask_fine_tuning.md",3,8,"Continual and Multi-Task Fine-Tuning","Supervised Fine-Tuning",["catastrophic-forgetting","task-specific-lora","multi-adapter","ewc","molor","data-replay"],"advanced"),
    ("_14_04_alignment_rlhf_dpo","_14_04_01_rlhf_overview_instructgpt.md",4,1,"RLHF Overview and InstructGPT","Alignment",["3h","instructgpt","sft-rm-ppo","reward-hacking","kl-penalty","constitutional-ai"],"advanced"),
    ("_14_04_alignment_rlhf_dpo","_14_04_02_reward_model_training.md",4,2,"Reward Model Training","Alignment",["bradley-terry","reward-trainer","preference-dataset","anthropic-hh","rm-evaluation"],"advanced"),
    ("_14_04_alignment_rlhf_dpo","_14_04_03_ppo_fine_tuning.md",4,3,"PPO Fine-Tuning","Alignment",["ppo","ppo-trainer","reference-model","value-model","reward-normalization","kl-adaptive"],"advanced"),
    ("_14_04_alignment_rlhf_dpo","_14_04_04_direct_preference_optimization_dpo.md",4,4,"Direct Preference Optimization DPO","Alignment",["dpo","dpo-trainer","beta","chosen","rejected","ultrafeedback","win-rate"],"intermediate"),
    ("_14_04_alignment_rlhf_dpo","_14_04_05_orpo_simpo_dpo_variants.md",4,5,"ORPO SimPO and DPO Variants","Alignment",["orpo","simpo","ipo","kto","cpo","no-reference-model","length-normalization"],"advanced"),
    ("_14_04_alignment_rlhf_dpo","_14_04_06_constitutional_ai_rlaif.md",4,6,"Constitutional AI and RLAIF","Alignment",["constitutional-ai","rlaif","self-critique","llm-judge","scalable-oversight","debate"],"advanced"),
    ("_14_04_alignment_rlhf_dpo","_14_04_07_process_reward_models.md",4,7,"Process Reward Models","Alignment",["prm","outcome-rm","math-shepherd","best-of-n","mcts","step-level-feedback"],"advanced"),
    ("_14_04_alignment_rlhf_dpo","_14_04_08_evaluation_aligned_models.md",4,8,"Evaluation of Aligned Models","Alignment",["mt-bench","alpacaeval","arena-hard","ifeval","lmsys","safety-eval","toxigen"],"intermediate"),
    ("_14_05_prompt_engineering","_14_05_01_prompt_engineering_fundamentals.md",5,1,"Prompt Engineering Fundamentals","Prompt Engineering",["zero-shot","few-shot","system-prompt","prompt-sensitivity","temperature","openai-sdk"],"intermediate"),
    ("_14_05_prompt_engineering","_14_05_02_chain_of_thought_prompting.md",5,2,"Chain-of-Thought Prompting","Prompt Engineering",["cot","zero-shot-cot","self-consistency","least-to-most","tree-of-thought","plan-solve"],"intermediate"),
    ("_14_05_prompt_engineering","_14_05_03_structured_output_json_mode.md",5,3,"Structured Output and JSON Mode","Prompt Engineering",["json-mode","structured-outputs","instructor","outlines","function-calling","xml-output"],"intermediate"),
    ("_14_05_prompt_engineering","_14_05_04_advanced_prompting_techniques.md",5,4,"Advanced Prompting Techniques","Prompt Engineering",["react","reflexion","pal","generated-knowledge","maieutic","directional-stimulus"],"advanced"),
    ("_14_05_prompt_engineering","_14_05_05_prompt_optimization_autoprompt.md",5,5,"Prompt Optimization and AutoPrompt","Prompt Engineering",["dspy","miprov2","textgrad","meta-prompting","eval-driven","automatic-prompt"],"advanced"),
    ("_14_05_prompt_engineering","_14_05_06_context_window_management.md",5,6,"Context Window Management","Prompt Engineering",["context-limits","lost-in-middle","retrieval-augmentation","summarization-compression","chunking","tiktoken"],"intermediate"),
    ("_14_05_prompt_engineering","_14_05_07_prompt_security_robustness.md",5,7,"Prompt Security and Robustness","Prompt Engineering",["prompt-injection","jailbreaking","indirect-injection","promptfoo","garak","guardrails"],"advanced"),
    ("_14_06_multimodal_llms","_14_06_01_vision_language_pretraining.md",6,1,"Vision-Language Pretraining","Multimodal LLMs",["clip","align","flava","coca","flamingo","q-former","blip2-bridge"],"advanced"),
    ("_14_06_multimodal_llms","_14_06_02_llava_visual_instruction_tuning.md",6,2,"LLaVA and Visual Instruction Tuning","Multimodal LLMs",["llava","llava-1.5","llava-next","mlp-projector","sharegpt4v","stage-1-2"],"intermediate"),
    ("_14_06_multimodal_llms","_14_06_03_strong_open_multimodal_llms.md",6,3,"Strong Open Multimodal LLMs","Multimodal LLMs",["internvl","qwen2.5-vl","phi-4-vision","gemma3","minicpm-v","paligemma2"],"intermediate"),
    ("_14_06_multimodal_llms","_14_06_04_multimodal_fine_tuning.md",6,4,"Multimodal Fine-Tuning","Multimodal LLMs",["multimodal-sft","llama-factory","xtuner","lora-vision","mmbench","mmmu","docvqa"],"advanced"),
    ("_14_06_multimodal_llms","_14_06_05_video_llms.md",6,5,"Video LLMs","Multimodal LLMs",["video-llava","qwen2.5-vl-video","videochat2","frame-sampling","egoscehma","video-mme"],"advanced"),
    ("_14_06_multimodal_llms","_14_06_06_audio_speech_llms.md",6,6,"Audio and Speech LLMs","Multimodal LLMs",["whisper","qwen2-audio","wavllm","voicecraft","f5-tts","speechlm"],"intermediate"),
    ("_14_06_multimodal_llms","_14_06_07_omni_any_modality_models.md",6,7,"Omni and Any-Modality Models","Multimodal LLMs",["gpt-4o","gemini-2.0","internomni","miniomni","discrete-tokens","any-to-any"],"advanced"),
    ("_14_07_llm_evaluation_and_safety","_14_07_01_llm_benchmarks.md",7,1,"LLM Benchmarks","Evaluation and Safety",["mmlu","hellaswag","arc","winogrande","gsm8k","humaneval","big-bench","lm-eval-harness"],"intermediate"),
    ("_14_07_llm_evaluation_and_safety","_14_07_02_llm_as_judge_evaluation.md",7,2,"LLM-as-Judge Evaluation","Evaluation and Safety",["mt-bench","alpacaeval","arena-hard","pairwise","pointwise","position-bias","fastchat"],"intermediate"),
    ("_14_07_llm_evaluation_and_safety","_14_07_03_hallucination_detection_mitigation.md",7,3,"Hallucination Detection and Mitigation","Evaluation and Safety",["truthfulqa","selfcheckgpt","fava","factscore","rag-grounding","citation","hallusion"],"advanced"),
    ("_14_07_llm_evaluation_and_safety","_14_07_04_llm_safety_red_teaming.md",7,4,"LLM Safety and Red Teaming","Evaluation and Safety",["garak","promptfoo","jailbreak","pair","tap","gcg","beavertails","hh-rlhf"],"advanced"),
    ("_14_07_llm_evaluation_and_safety","_14_07_05_bias_fairness_llms.md",7,5,"Bias and Fairness in LLMs","Evaluation and Safety",["bbq","winobias","bold","counterfactual","debiasing","rlhf-debiasing","representation"],"advanced"),
    ("_14_07_llm_evaluation_and_safety","_14_07_06_responsible_ai_governance.md",7,6,"Responsible AI and Governance","Evaluation and Safety",["eu-ai-act","model-cards","datasheets","watermarking","synthid","c2pa","nist-ai-rmf"],"advanced"),
    ("_14_07_llm_evaluation_and_safety","_14_07_07_llm_memorization_privacy.md",7,7,"LLM Memorization and Privacy","Evaluation and Safety",["extraction-attack","membership-inference","dp-sgd","machine-unlearning","pii-filter","tofu"],"advanced"),
    ("_14_08_llm_inference_and_serving","_14_08_01_llm_inference_fundamentals.md",8,1,"LLM Inference Fundamentals","Inference and Serving",["autoregressive","kv-cache","prefill","decode","ttft","tpot","throughput-latency"],"intermediate"),
    ("_14_08_llm_inference_and_serving","_14_08_02_vllm.md",8,2,"vLLM","Inference and Serving",["paged-attention","continuous-batching","prefix-caching","tensor-parallel","speculative","gptq-awq"],"intermediate"),
    ("_14_08_llm_inference_and_serving","_14_08_03_text_generation_inference_tgi.md",8,3,"Text Generation Inference TGI","Inference and Serving",["tgi","flash-attention","streaming","lora-serving","dynamic-adapter","docker"],"intermediate"),
    ("_14_08_llm_inference_and_serving","_14_08_04_ollama_local_inference.md",8,4,"Ollama and Local Inference","Inference and Serving",["ollama","gguf","llama-cpp","modelfile","local-api","llama-cpp-python"],"intermediate"),
    ("_14_08_llm_inference_and_serving","_14_08_05_speculative_decoding.md",8,5,"Speculative Decoding","Inference and Serving",["draft-model","verify","acceptance-rate","medusa","eagle","2-3x-speedup"],"advanced"),
    ("_14_08_llm_inference_and_serving","_14_08_06_llm_batching_scheduling.md",8,6,"LLM Batching and Scheduling","Inference and Serving",["static-batching","continuous-batching","chunked-prefill","priority","litellm-proxy","load-balance"],"advanced"),
    ("_14_08_llm_inference_and_serving","_14_08_07_llm_api_gateway.md",8,7,"LLM API Gateway","Inference and Serving",["litellm","cost-tracking","rate-limiting","fallbacks","caching","langfuse","langsmith"],"intermediate"),
    ("_14_09_llm_compression_and_edge","_14_09_01_gptq_quantization.md",9,1,"GPTQ Quantization","LLM Compression",["gptq","auto-gptq","w4a16","calibration","obq","vllm-gptq"],"intermediate"),
    ("_14_09_llm_compression_and_edge","_14_09_02_awq_quantization.md",9,2,"AWQ Quantization","LLM Compression",["awq","autoawq","scale-search","salient-weights","exllamav2","vllm-awq"],"intermediate"),
    ("_14_09_llm_compression_and_edge","_14_09_03_gguf_llama_cpp.md",9,3,"GGUF and llama.cpp","LLM Compression",["gguf","llama-cpp","q4-k-m","q5-k-m","imatrix","metal","convert-hf-gguf"],"intermediate"),
    ("_14_09_llm_compression_and_edge","_14_09_04_knowledge_distillation_llms.md",9,4,"Knowledge Distillation for LLMs","LLM Compression",["black-box-distillation","white-box","distilgpt2","tinyllama","deepseek-r1-distill"],"intermediate"),
    ("_14_09_llm_compression_and_edge","_14_09_05_pruning_sparsity_llms.md",9,5,"Pruning and Sparsity in LLMs","LLM Compression",["sparsegpt","wanda","llm-pruner","2-4-sparsity","structured-pruning","quant-prune"],"advanced"),
    ("_14_09_llm_compression_and_edge","_14_09_06_edge_deployment_llms.md",9,6,"Edge Deployment of LLMs","LLM Compression",["executorch","phi-3-mini","mlx","jetson","web-llm","webgpu","mlc-llm","raspberry-pi"],"intermediate"),
    ("_14_10_industry_projects","_14_10_01_custom_chat_assistant_qlora.md",10,1,"Custom Chat Assistant QLoRA","Industry Projects",["qlora","sft-trainer","vllm","fastapi","domain-chat","win-rate"],"advanced"),
    ("_14_10_industry_projects","_14_10_02_dpo_aligned_model.md",10,2,"DPO Aligned Model","Industry Projects",["dpo","ultrafeedback","alpacaeval","toxigen","sft-dpo-pipeline"],"advanced"),
    ("_14_10_industry_projects","_14_10_03_code_generation_service.md",10,3,"Code Generation Service","Industry Projects",["codellama","humaneval","fim","vllm","fastapi","docker","pass-at-1"],"advanced"),
    ("_14_10_industry_projects","_14_10_04_multimodal_document_analyst.md",10,4,"Multimodal Document Analyst","Industry Projects",["internvl2","qwen2.5-vl","pdf-qa","multi-page","fastapi","invoice","contract"],"advanced"),
    ("_14_10_industry_projects","_14_10_05_on_device_llm_app.md",10,5,"On-Device LLM App","Industry Projects",["phi-3-mini","gguf","llama-cpp-python","gradio","offline","apple-m1","cpu-inference"],"intermediate"),
    ("_14_10_industry_projects","_14_10_06_llm_evaluation_pipeline_capstone.md",10,6,"LLM Evaluation Pipeline Capstone","Industry Projects",["lm-eval-harness","mt-bench","fastchat","llm-as-judge","wandb","leaderboard"],"advanced"),
]
created = 0
skipped = 0
for folder, fname, mod, les, title, mod_title, tags, diff in LESSONS:
    dirpath = os.path.join(BASE, folder)
    os.makedirs(dirpath, exist_ok=True)
    fpath = os.path.join(dirpath, fname)
    if not os.path.exists(fpath):
        lid = f"14_{mod:02d}_{les:02d}"
        tag_str = ", ".join('"'+t+'"' for t in tags)
        content = f'---\nid: "{lid}"\ntitle: "{title}"\ncourse: "Generative AI and LLMs"\nmodule: {mod}\nmodule_title: "{mod_title}"\nlesson: {les}\nversion: "2.0"\ndifficulty: "{diff}"\nduration_minutes: 60\ntags: [{tag_str}]\nprerequisites: []\nlab_required: true\n---\n\n# {title}\n\n> **Status**: Syllabus stub. Full lesson content to be authored.\n\n---\n\n## Topics Covered\n\n*(See Phase 5 Gen AI Syllabus for full topic and subtopic breakdown)*\n\n---\n\n## Learning Objectives\n\n- To be defined during content authoring.\n'
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[CREATE] {fname}")
        created += 1
    else:
        print(f"[SKIP]   {fname}")
        skipped += 1
print(f"\nDONE - Created: {created}  Skipped: {skipped}  Total: {created+skipped}")
