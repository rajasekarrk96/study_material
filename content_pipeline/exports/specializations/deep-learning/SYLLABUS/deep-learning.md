# Deep Learning & Neural Architectures — Master Syllabus

**Target Role:** Deep Learning Engineer / AI Researcher / Computer Vision & NLP Engineer  
**Difficulty Level:** Advanced  
**Estimated Duration:** 90 Hours  
**Prerequisites:** specializations/machine-learning, foundations/ds-math, foundations/core-python  
**Required Courses:** specializations/machine-learning, foundations/ds-math  
**Optional Courses:** technologies/docker, technologies/fastapi  

---

## Study Flow

### Module 1 — Deep Learning Foundations
1. **The Artificial Neuron & Perceptron** (Biological inspiration, mathematical formulation, linear separability, XOR limitation)
2. **Feedforward Neural Networks (MLP)** (Multi-layer perceptron architecture, hidden representations, universal approximation theorem)
3. **Activation Functions Deep Dive** (Sigmoid, Tanh, ReLU, Leaky ReLU, GeLU, Swish, dying ReLU problem)
4. **Loss Functions for Deep Learning** (Cross-Entropy, Binary Cross-Entropy, Focal Loss, MSE, Huber Loss, Contrastive Loss)
5. **Backpropagation & Computational Graphs** (Chain rule of calculus, reverse-mode automatic differentiation, gradient flow)
6. **Weight Initialization Strategies** (Xavier/Glorot initialization, He/Kaiming initialization, zero-bias initialization)
7. **Regularization Techniques** (L1/L2 weight decay, Dropout, DropConnect, Early Stopping, Label Smoothing)
8. **Neural Network Capacity & Generalization** (Underfitting, overfitting, double descent phenomenon, inductive biases)

### Module 2 — PyTorch Framework Deep Dive
1. **PyTorch Tensors & Autograd Mechanics** (Tensor memory layouts, stride, dynamic computational graph, `requires_grad`)
2. **Building Neural Networks with `nn.Module`** (Defining custom layers, parameter registration, sequential vs functional models)
3. **PyTorch Optimizers** (SGD with momentum, Adam, AdamW, RMSProp, Lion, weight decay decoupling)
4. **Learning Rate Schedulers** (StepLR, CosineAnnealing, OneCycleLR, warmup strategies)
5. **Data Pipelines & Custom Datasets** (`Dataset`, `DataLoader`, num_workers, pin_memory, custom collate functions)
6. **Production Training Loop Architecture** (Validation loops, gradient accumulation, model checkpointing)
7. **Debugging & Profiling PyTorch** (PyTorch Profiler, CUDA memory tracking, detecting CPU-GPU synchronization bottlenecks)
8. **Distributed Training Fundamentals** (DistributedDataParallel vs DataParallel, gradient all-reduce)
9. **Model Persistence & Export** (TorchScript tracing/scripting, ONNX model export)

### Module 3 — TensorFlow 2.x & Keras
1. **TensorFlow 2.x Architecture** (Eager execution vs `@tf.function` graph tracing, AutoGraph)
2. **Keras Sequential & Functional APIs** (Model building, multi-input and multi-output architectures)
3. **Keras Training & Custom Callbacks** (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, writing custom callbacks)
4. **`tf.data` High-Performance Pipelines** (Mapping, prefetching, parallel batching, interleaving)
5. **Hyperparameter Tuning** (KerasTuner, Bayesian optimization, random search)
6. **SavedModel & TensorFlow Serving** (Exporting production artifacts, REST/gRPC model serving)
7. **TensorBoard & Experiment Tracking** (Visualizing scalar metrics, histograms, graph graphs, and embedding projectors)

### Module 4 — Advanced Training Optimization & Stability
1. **Advanced Optimization Algorithms** (LAMB, Lookahead, Sophia, adaptive gradient mechanics)
2. **Learning Rate Scheduling Techniques** (Cyclical learning rates, warm restarts, learning rate range test)
3. **Batch Size Scaling & Gradient Accumulation** (Linear scaling rule, simulating large batch sizes with constrained VRAM)
4. **Mixed Precision Training (AMP)** (FP16/BF16 numerical precision, loss scaling, dynamic gradient scalers)
5. **Gradient Clipping & Training Stability** (Clip by norm, clip by value, preventing exploding gradients)
6. **Normalization Layers** (BatchNorm, LayerNorm, InstanceNorm, GroupNorm, RMSNorm, running statistics tracking)
7. **Data Augmentation Strategies** (MixUp, CutMix, RandAugment, Albumentations pipelines)

### Module 5 — Convolutional Neural Networks (CNNs)
1. **Convolution Operation & Filter Mathematics** (Kernels, stride, padding, receptive field calculation, dilation)
2. **Spatial Reduction & Pooling** (Max pooling, average pooling, global average pooling)
3. **Classic CNN Architectures** (LeNet, AlexNet, VGG, Inception/GoogLeNet)
4. **Residual Networks (ResNet)** (Residual connections, identity mappings, solving vanishing gradients in deep networks)
5. **Modern Efficient CNNs** (ResNeXt, MobileNet depthwise separable convolutions, EfficientNet compound scaling, ConvNeXt)
6. **End-to-End Image Classification Pipeline** (Transfer learning, fine-tuning pretrained backbones)

### Module 6 — Recurrent Neural Networks & Temporal Sequences
1. **Vanilla RNN Architecture** (Hidden state recurrence, Backpropagation Through Time (BPTT), exploding/vanishing gradients)
2. **Long Short-Term Memory (LSTM)** (Input gate, forget gate, cell state, output gate mathematics)
3. **Gated Recurrent Unit (GRU)** (Reset gate, update gate, computational efficiency vs LSTM)
4. **Sequence-to-Sequence (Seq2Seq)** (Encoder-decoder architectures, teacher forcing)
5. **Attention Mechanism for RNNs** (Bahdanau additive attention, Luong multiplicative attention)
6. **RNNs for Time Series & Anomaly Detection** (Multivariate sequence forecasting, sliding window inference)
7. **Temporal Convolutional Networks (TCN)** (Dilated causal convolutions, receptive fields)

### Module 7 — Transformers & Multi-Head Attention
1. **Scaled Dot-Product Attention** (Query, Key, Value mechanics, attention matrix scaling)
2. **Multi-Head Attention (MHA)** (Multi-representation subspace projection, computational complexity)
3. **Positional Encoding Systems** (Sinusoidal positional embeddings, learnable embeddings, RoPE, ALiBi)
4. **Transformer Encoder Architecture** (Pre-LN vs Post-LN, Feedforward Networks (FFN), residual connections)
5. **Transformer Decoder Architecture** (Causal masking, cross-attention mechanics)
6. **Vision Transformers (ViT)** (Patch projection, class token, transformer self-attention for vision)
7. **Efficient Attention Mechanisms** (FlashAttention memory-aware tiling, sliding window attention, sparse attention)

### Module 8 — Generative Models & Deep Generative Architectures
1. **Autoencoders (AE)** (Bottleneck representations, latent spaces, reconstruction loss)
2. **Variational Autoencoders (VAE)** (Probabilistic latent space, reparameterization trick, KL divergence loss)
3. **Generative Adversarial Networks (GAN)** (Minimax objective, generator vs discriminator dynamics, training instability)
4. **Advanced GAN Architectures** (DCGAN, WGAN-GP Wasserstein distance with gradient penalty, StyleGAN)
5. **Diffusion Models Fundamentals** (Forward noising process, reverse denoising diffusion, score matching)
6. **Denoising Diffusion Probabilistic Models (DDPM)** (U-Net backbones, noise prediction, classifier-free guidance)
7. **Generative Model Evaluation** (Inception Score (IS), Fréchet Inception Distance (FID))

### Module 9 — Self-Supervised Learning (SSL)
1. **Self-Supervised Learning Foundations** (Pretext tasks, representation learning without human labels)
2. **Contrastive Learning** (SimCLR, InfoNCE loss, negative sampling, data augmentation dependencies)
3. **Non-Contrastive SSL** (BYOL, SimSiam, collapse prevention mechanisms)
4. **Masked Autoencoders (MAE)** (Masked image modeling, asymmetric encoder-decoder architecture)
5. **Self-Distillation (DINO)** (Vision transformer self-distillation, centering and sharpening)

### Module 10 — Transfer Learning & Parameter-Efficient Fine-Tuning
1. **Transfer Learning Foundations** (Feature extraction vs full fine-tuning, catastrophic forgetting)
2. **Domain Adaptation** (Adversarial domain adaptation, maximum mean discrepancy)
3. **Knowledge Distillation** (Teacher-student networks, soft targets, temperature scaling)
4. **Parameter-Efficient Fine-Tuning (PEFT)** (Low-Rank Adaptation (LoRA), prompt tuning, adapter modules)
5. **Multi-Task Learning** (Hard vs soft parameter sharing, loss balancing strategies)

### Module 11 — Model Compression, Optimization & Edge Serving
1. **Model Quantization** (Post-Training Quantization (PTQ), Quantization-Aware Training (QAT), INT8 weight calibration)
2. **Neural Network Pruning** (Structured vs unstructured pruning, magnitude pruning, iterative pruning)
3. **Model Compilation & Acceleration** (ONNX Runtime, TensorRT execution graphs, OpenVINO)
4. **Production Model Serving** (Triton Inference Server dynamic batching, FastAPI async model worker pipelines)
5. **Benchmarking & Latency Profiling** (Throughput (QPS), p50/p95/p99 latency, GPU VRAM profiling)

### Module 12 — Industry Capstones
1. **Production Multi-Class Vision System** (ResNet/ViT backbone with Triton serving and Prometheus metrics)
2. **Industrial Time-Series Anomaly Detection Pipeline** (LSTM/TCN model for high-frequency sensor fault detection)
3. **End-to-End Generative Diffusion Pipeline** (Custom diffusion model for conditional image synthesis)