# Deep Learning — Master Syllabus

**Target Role:** Deep Learning Engineer / AI Engineer  
**Difficulty Level:** Advanced  
**Estimated Duration:** 80 Hours  
**Prerequisites:** Machine Learning, Python, NumPy, Statistics  

---

## Study Flow

---

### Module 1 — Neural Network Foundations

#### 1.1. Biological to Artificial Neurons

1. **The Artificial Neuron and Perceptron**
    - **Course Coverage:** 🟢 Covered in Class
    1. Biological neuron analogy
    2. Perceptron algorithm and convergence
    3. XOR problem and multi-layer requirement
    4. Lab Exercise

2. **Feedforward Neural Networks (MLP)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Hidden layers and non-linearity
    2. Universal approximation theorem
    3. Forward pass computation
    4. Lab Exercise

3. **Activation Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Sigmoid and Tanh — saturation and vanishing gradient
    2. ReLU family — ReLU, Leaky ReLU, ELU, GELU
    3. Softmax for classification output
    4. Lab Exercise

4. **Backpropagation and Chain Rule**
    - **Course Coverage:** 🟢 Covered in Class
    1. Computational graph
    2. Gradient computation via chain rule
    3. Vanishing and exploding gradients
    4. Lab Exercise

5. **Optimization Algorithms**
    - **Course Coverage:** 🟢 Covered in Class
    1. SGD, Momentum, Nesterov
    2. Adam, AdaGrad, RMSProp
    3. Learning rate schedules
    4. Gradient clipping
    5. Lab Exercise

---

### Module 2 — Convolutional Neural Networks

#### 2.1. CNN Architecture

1. **Convolution Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. 2D convolution, stride, padding
    2. Feature maps and receptive field
    3. Depthwise and pointwise convolutions
    4. Lab Exercise

2. **Pooling and Normalization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Max pooling, average pooling
    2. Batch normalization, Layer normalization
    3. Dropout for regularization
    4. Lab Exercise

3. **Classic CNN Architectures**
    - **Course Coverage:** 🟢 Covered in Class
    1. LeNet, AlexNet, VGG
    2. ResNet and skip connections
    3. InceptionNet, EfficientNet
    4. Lab Exercise

4. **Transfer Learning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Feature extraction vs fine-tuning
    2. Pre-trained models — ImageNet weights
    3. Domain adaptation
    4. Lab Exercise

---

### Module 3 — Recurrent Neural Networks

#### 3.1. Sequence Modelling

1. **RNN Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Hidden state and temporal dependency
    2. BPTT — Backpropagation through time
    3. Vanishing gradient in RNNs
    4. Lab Exercise

2. **LSTM and GRU**
    - **Course Coverage:** 🟢 Covered in Class
    1. LSTM gates — input, forget, output
    2. GRU — simplified gating
    3. Bidirectional RNNs
    4. Lab Exercise

3. **Sequence-to-Sequence Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Encoder-decoder architecture
    2. Attention mechanism
    3. Applications — translation, summarization
    4. Lab Exercise

---

### Module 4 — Transformer Architecture

#### 4.1. Attention and Transformers

1. **Self-Attention Mechanism**
    - **Course Coverage:** 🟢 Covered in Class
    1. Query, Key, Value projections
    2. Scaled dot-product attention
    3. Multi-head attention
    4. Lab Exercise

2. **Transformer Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Positional encoding
    2. Encoder and decoder blocks
    3. Feed-forward sublayer and residual connections
    4. Lab Exercise

3. **Pre-trained Language Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. BERT — masked language modelling
    2. GPT family — autoregressive generation
    3. Fine-tuning strategies
    4. Lab Exercise

---

### Module 5 — Generative Models

#### 5.1. Generative Deep Learning

1. **Autoencoders and VAEs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Encoder-decoder bottleneck
    2. Variational autoencoder — latent space
    3. Reconstruction loss and KL divergence
    4. Lab Exercise

2. **Generative Adversarial Networks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Generator vs Discriminator
    2. GAN training dynamics and mode collapse
    3. DCGAN, StyleGAN, CycleGAN
    4. Lab Exercise

3. **Diffusion Models**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Forward diffusion (noise addition)
    2. Reverse denoising process
    3. DDPM and score-based models
    4. Stable Diffusion overview
    5. Lab Exercise

---

### Module 6 — DL Training & Deployment

#### 6.1. Production Deep Learning

1. **DL Training Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Batch size selection
    2. Mixed precision training (FP16)
    3. Gradient accumulation
    4. Experiment tracking
    5. Lab Exercise

2. **Model Compression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Pruning — structured and unstructured
    2. Quantization — INT8, FP16
    3. Knowledge distillation
    4. Lab Exercise

3. **DL Frameworks**
    - **Course Coverage:** 🟢 Covered in Class
    1. PyTorch — DataLoader, Dataset, nn.Module
    2. PyTorch Lightning
    3. ONNX export
    4. Lab Exercise

4. **Capstone — Image Classification & NLP System**
    - **Course Coverage:** 🟢 Covered in Class
    1. CNN-based image classifier
    2. BERT-based text classifier
    3. Deployment with FastAPI
    4. Lab Exercise
