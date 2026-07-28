# Phase 2: Deep Learning — Enterprise Syllabus
## Learning OS Enterprise Standard | Curriculum Architecture v2.0

**Classification**: Chief Curriculum Architect — Syllabus Design Document  
**Phase**: 2 of 8  
**Domain**: Deep Learning  
**Required Previous Phases**: Phase 1 (Machine Learning `_10_machine_learning`)  
**Folder Root**: `docs/curriculum/_11_deep_learning/`  
**Last Updated**: 2026-07-28

---

## Dependency Graph

```
_08_ds_math
    └─> _09_python_data_science
            └─> _10_machine_learning   (Phase 1)
                    └─> _11_deep_learning  ◄── THIS PHASE
```

Cross-phase reuse nodes (zero duplication):
- `ML.10_01_04` Bias-Variance → reused in DL generalization
- `ML.10_02_02` Gradient Descent → reused; extended with Adam, AdaGrad, etc.
- `ML.10_02_03` Linear Algebra PCA/SVD → reused in attention math
- `ML.10_06_02_07` MLP Classifier → extended into full DL networks
- `Python.OOP` → PyTorch `nn.Module` subclassing
- `FastAPI.Endpoints` → model serving endpoints

---

## Skills Gained (This Phase)

- Design and train deep neural networks from scratch using PyTorch and TensorFlow/Keras
- Apply backpropagation, initialization, and regularization correctly
- Build CNNs for image classification, detection, and segmentation
- Architect RNNs, LSTMs, GRUs for sequential and time-series data
- Implement self-attention and Transformer architectures
- Train GANs and Diffusion Models for generative tasks
- Apply transfer learning and fine-tuning on pretrained vision models
- Implement self-supervised and contrastive learning
- Compress and quantize models for edge deployment
- Deploy deep learning models via TorchScript, ONNX, and TensorRT

---

## Industry Applications (This Phase)

- Image classification and recognition systems
- Object detection pipelines (autonomous vehicles, manufacturing QC)
- NLP preprocessing with sequence models (before full Transformer in Phase 4)
- Speech-to-text feature extraction
- Generative art and synthetic data augmentation
- Medical image analysis (X-ray, MRI segmentation)
- Video action recognition
- Fraud detection with sequence models

---

## Course Structure

```
_11_deep_learning/
├── _11_01_dl_foundations/
├── _11_02_pytorch_framework/
├── _11_03_tensorflow_keras/
├── _11_04_training_optimization/
├── _11_05_convolutional_neural_networks/
├── _11_06_recurrent_neural_networks/
├── _11_07_attention_and_transformers/
├── _11_08_generative_models/
├── _11_09_self_supervised_learning/
├── _11_10_transfer_learning_and_finetuning/
├── _11_11_model_compression_and_deployment/
└── _11_12_industry_projects/
```

---

## MODULE 01 — Deep Learning Foundations

**Folder**: `_11_01_dl_foundations/`  
**Lesson Count**: 8  
**Learning Order**: 1st

### Lessons

#### Lesson 01.01 — The Artificial Neuron and Perceptron
**File**: `_11_01_01_artificial_neuron_and_perceptron.md`

| Topics | Subtopics |
|---|---|
| Biological neuron analogy | Dendrites, soma, axon → inputs, weights, output |
| McCulloch-Pitts neuron | Binary threshold unit |
| Perceptron learning rule | Weight update, convergence theorem |
| Linearly separable limitations | XOR problem |
| `sklearn.linear_model.Perceptron` | Reuse from Phase 1 — extend to DL context |
| From Perceptron to MLP | Motivation for hidden layers |

---

#### Lesson 01.02 — Feedforward Neural Networks (MLP Architecture)
**File**: `_11_01_02_feedforward_neural_networks_mlp.md`

| Topics | Subtopics |
|---|---|
| Layer architecture | Input layer, hidden layers, output layer |
| Depth vs width | Parameter count, representational capacity |
| Universal approximation theorem | Statement, implications, limitations |
| Matrix formulation | Z = XW + b, layer-by-layer computation |
| Vectorized forward pass | Batch computation, design matrix |
| Parameter count calculation | Weights + biases per layer |

---

#### Lesson 01.03 — Activation Functions
**File**: `_11_01_03_activation_functions.md`

| Topics | Subtopics |
|---|---|
| Sigmoid | σ(z) = 1/(1+e⁻ᶻ), vanishing gradient problem |
| Tanh | Range [-1,1], zero-centred, gradient saturation |
| ReLU | max(0,z), dying ReLU, sparse activation |
| Leaky ReLU | αz for z<0, fixes dying ReLU |
| PReLU | Learnable α parameter |
| ELU | Smooth negative region, mean-zero activations |
| GELU | Gaussian Error Linear Unit, used in BERT/GPT |
| Swish / SiLU | Self-gated, smooth, non-monotonic |
| Mish | Smooth, non-monotonic, image models |
| Softmax | Multi-class output, numerical stability (log-sum-exp) |
| Choosing activations | ReLU/GELU for hidden, Sigmoid/Softmax for output |

---

#### Lesson 01.04 — Loss Functions for Deep Learning
**File**: `_11_01_04_loss_functions_deep_learning.md`

| Topics | Subtopics |
|---|---|
| Regression losses | MSE, MAE, Huber/SmoothL1, Log-Cosh |
| Binary classification | Binary Cross-Entropy (BCE), Focal Loss |
| Multi-class classification | Categorical Cross-Entropy, NLL Loss, Label Smoothing |
| Multi-label | Binary Cross-Entropy per label |
| Contrastive losses | Triplet Loss, Contrastive Loss, NT-Xent |
| Detection losses | Smooth L1 + BCE combination |
| Custom loss functions | `nn.Module`-based loss class in PyTorch |
| Loss landscape | Saddle points, sharp vs flat minima |

---

#### Lesson 01.05 — Backpropagation and Computational Graphs
**File**: `_11_01_05_backpropagation_computational_graphs.md`

| Topics | Subtopics |
|---|---|
| Chain rule review | Composite function differentiation |
| Computational graph | Nodes as operations, edges as tensors |
| Forward pass | Left-to-right computation |
| Backward pass | Right-to-left gradient accumulation |
| Local gradients | Gradient of each primitive operation |
| Vanishing / exploding gradients | Chain multiplication across layers |
| Gradient flow tricks | Residual connections, batch norm (preview) |
| Autograd engines | PyTorch `autograd`, TensorFlow `GradientTape` |

---

#### Lesson 01.06 — Weight Initialization
**File**: `_11_01_06_weight_initialization.md`

| Topics | Subtopics |
|---|---|
| Why initialization matters | Symmetry breaking, gradient flow |
| Zero initialization | Problem: all neurons learn same features |
| Random normal | Too large/small variance issues |
| Xavier / Glorot | Uniform and normal variants, tanh/sigmoid |
| He / Kaiming | Variance correction for ReLU, `fan_in` |
| LeCun initialization | For SELU activation |
| Orthogonal initialization | Preserves gradient norms in RNNs |
| `torch.nn.init` | `xavier_uniform_`, `kaiming_normal_`, `orthogonal_` |
| `tf.keras.initializers` | `GlorotUniform`, `HeNormal` |

---

#### Lesson 01.07 — Regularization Techniques
**File**: `_11_01_07_regularization_techniques.md`

| Topics | Subtopics |
|---|---|
| L2 Weight Decay | `weight_decay` in optimizer, AdamW |
| L1 Regularization | Sparsity in weights |
| Dropout | `nn.Dropout`, `rate`, training vs inference mode |
| DropConnect | Drop weights instead of activations |
| Spatial Dropout | For CNNs — drop entire feature maps |
| Batch Normalization | Normalizes activations per mini-batch |
| Layer Normalization | Normalizes across features, used in Transformers |
| Group Normalization | For small batch sizes |
| Instance Normalization | Style transfer |
| Data Augmentation | As implicit regularization (preview in CNN module) |
| Early Stopping | `patience`, `monitor` |
| Label Smoothing | Soft targets, overconfidence reduction |

---

#### Lesson 01.08 — Neural Network Capacity and Generalization
**File**: `_11_01_08_neural_network_capacity_generalization.md`

| Topics | Subtopics |
|---|---|
| VC dimension for NNs | Theoretical capacity |
| Double descent phenomenon | Modern large model generalization |
| Effective model capacity | Depth, width, activation nonlinearity |
| Memorization vs generalization | Memorization experiments (Zhang et al.) |
| Learning curves for DL | Train loss, val loss, overfitting signatures |
| PAC learning | Probably Approximately Correct framework |

---

## MODULE 02 — PyTorch Framework

**Folder**: `_11_02_pytorch_framework/`  
**Lesson Count**: 9  
**Learning Order**: 2nd

### Lessons

#### Lesson 02.01 — PyTorch Tensors and Autograd
**File**: `_11_02_01_pytorch_tensors_autograd.md`

| Topics | Subtopics |
|---|---|
| `torch.Tensor` | dtype, device, shape, strides |
| Tensor creation | `torch.zeros`, `torch.ones`, `torch.randn`, `torch.arange` |
| Tensor operations | Arithmetic, matmul (`@`), broadcasting |
| Device management | `.to(device)`, `.cuda()`, `torch.device` |
| `requires_grad` | Leaf tensors, gradient accumulation |
| `torch.autograd.grad` | Manual gradient computation |
| `.backward()` | Compute gradient of scalar w.r.t. leaves |
| `.grad` | Accessing gradients |
| Detach and no_grad | `detach()`, `torch.no_grad()` context |

---

#### Lesson 02.02 — Building Models with nn.Module
**File**: `_11_02_02_building_models_nn_module.md`

| Topics | Subtopics |
|---|---|
| `nn.Module` | `__init__`, `forward()`, submodule registration |
| Linear layers | `nn.Linear(in, out)`, weights and bias |
| Sequential containers | `nn.Sequential`, `nn.ModuleList`, `nn.ModuleDict` |
| Parameter registration | `nn.Parameter`, `register_buffer` |
| Model inspection | `.parameters()`, `.named_parameters()`, `model.eval()` |
| Custom layer | Subclassing `nn.Module` with learnable params |
| `torchinfo` | Model summary, parameter count |

---

#### Lesson 02.03 — PyTorch Optimizers
**File**: `_11_02_03_pytorch_optimizers.md`

| Topics | Subtopics |
|---|---|
| SGD | `torch.optim.SGD`, `lr`, `momentum`, `nesterov`, `weight_decay` |
| Adam | Adaptive moments, `lr`, `betas`, `eps`, `weight_decay` |
| AdamW | Decoupled weight decay, preferred for Transformers |
| RMSProp | Adaptive LR, `alpha`, `centered` |
| Adagrad | Accumulated gradient history, `lr_decay` |
| Adadelta | No manual LR, `rho`, `eps` |
| LBFGS | Quasi-Newton, for small problems |
| Optimizer step | `zero_grad()` → `loss.backward()` → `step()` |
| Gradient clipping | `clip_grad_norm_`, `clip_grad_value_` |

---

#### Lesson 02.04 — Learning Rate Scheduling
**File**: `_11_02_04_learning_rate_scheduling.md`

| Topics | Subtopics |
|---|---|
| Step LR | `StepLR`, `MultiStepLR` |
| Exponential decay | `ExponentialLR` |
| Cosine annealing | `CosineAnnealingLR`, `CosineAnnealingWarmRestarts` |
| Warm-up | Linear warm-up + cosine decay combination |
| Cyclic LR | `CyclicLR`, `OneCycleLR` |
| Reduce on plateau | `ReduceLROnPlateau`, `patience`, `factor` |
| LR Finder | Smith's method, `torch-lr-finder` |
| Scheduler chaining | `SequentialLR`, `ChainedScheduler` |

---

#### Lesson 02.05 — PyTorch Data Pipeline
**File**: `_11_02_05_pytorch_data_pipeline.md`

| Topics | Subtopics |
|---|---|
| `torch.utils.data.Dataset` | `__len__`, `__getitem__` |
| `DataLoader` | `batch_size`, `shuffle`, `num_workers`, `pin_memory`, `drop_last` |
| Custom Dataset | Image folders, CSV datasets, HDF5 files |
| `torchvision.datasets` | MNIST, CIFAR-10, ImageNet |
| Transforms | `transforms.Compose`, `Normalize`, `ToTensor`, `Resize` |
| `torchvision.transforms.v2` | Modern API, composable |
| Iterable Dataset | Streaming large datasets |
| Sampler | `WeightedRandomSampler`, class imbalance |
| Memory mapping | `np.memmap`, efficient large array access |

---

#### Lesson 02.06 — Training Loop Architecture
**File**: `_11_02_06_training_loop_architecture.md`

| Topics | Subtopics |
|---|---|
| Standard training loop | epoch → batch → forward → loss → backward → step |
| Model modes | `model.train()` vs `model.eval()` |
| Mixed precision | `torch.amp.autocast`, `GradScaler` |
| Gradient accumulation | Simulating large batch size |
| Epoch metrics | Tracking train/val loss, accuracy per epoch |
| Checkpointing | `torch.save`, `torch.load`, `state_dict` |
| Early stopping | Custom implementation |
| `tqdm` progress | Epoch and batch progress bars |

---

#### Lesson 02.07 — Debugging and Profiling PyTorch Models
**File**: `_11_02_07_debugging_profiling_pytorch.md`

| Topics | Subtopics |
|---|---|
| NaN/Inf detection | `torch.isnan`, `torch.isinf`, anomaly detection |
| `torch.autograd.set_detect_anomaly` | Trace gradient issues |
| Gradient flow visualization | Plot `grad.norm()` per layer |
| `torch.profiler` | CPU/GPU time profiling, memory profiling |
| TensorBoard with PyTorch | `SummaryWriter`, `add_scalar`, `add_histogram` |
| `torchviz` | Computational graph visualization |
| Memory management | `.detach()`, `del`, `torch.cuda.empty_cache()` |

---

#### Lesson 02.08 — Distributed Training with PyTorch
**File**: `_11_02_08_distributed_training_pytorch.md`

| Topics | Subtopics |
|---|---|
| `DataParallel` | Single node, multiple GPUs |
| `DistributedDataParallel` | Multi-node, NCCL backend |
| `torchrun` | Launch utility, `WORLD_SIZE`, `LOCAL_RANK` |
| `dist.init_process_group` | Backend initialization |
| `DistributedSampler` | Partition dataset per rank |
| Gradient synchronization | AllReduce, ring-allreduce |
| FSDP | Fully Sharded Data Parallel, large model training |
| DeepSpeed integration | ZeRO stages 1/2/3 concept |

---

#### Lesson 02.09 — TorchScript and Model Export
**File**: `_11_02_09_torchscript_model_export.md`

| Topics | Subtopics |
|---|---|
| TorchScript | `torch.jit.trace`, `torch.jit.script` |
| `torch.export` | Stable export API (PyTorch 2.x+) |
| `torch.compile` | `torch.compile(model)`, TorchDynamo, Inductor |
| ONNX export | `torch.onnx.export`, opset version |
| ONNX Runtime | `ort.InferenceSession`, CPU/GPU execution |
| Model optimization | `torch.quantization.quantize_dynamic` |
| Tracing limitations | Dynamic shapes, control flow |

---

## MODULE 03 — TensorFlow and Keras

**Folder**: `_11_03_tensorflow_keras/`  
**Lesson Count**: 7  
**Learning Order**: 3rd

### Lessons

#### Lesson 03.01 — TensorFlow 2.x Architecture
**File**: `_11_03_01_tensorflow_2x_architecture.md`

| Topics | Subtopics |
|---|---|
| TF 2.x vs TF 1.x | Eager execution by default, `tf.function` |
| `tf.Tensor` | dtype, shape, device, operations |
| `tf.Variable` | Mutable state, `assign`, `assign_add` |
| `tf.GradientTape` | Manual gradient computation |
| `tf.function` | Graph compilation, `@tf.function` decorator |
| XLA compilation | `jit_compile=True` |
| TF ecosystem | `tf.data`, `tf.keras`, `tf.lite`, `tf.js`, `tf.serving` |

---

#### Lesson 03.02 — Keras Sequential and Functional API
**File**: `_11_03_02_keras_sequential_functional_api.md`

| Topics | Subtopics |
|---|---|
| Sequential API | `model.add()`, `layers.*` |
| Functional API | Input/output tensor wiring, multi-input/output |
| Model subclassing | `tf.keras.Model` subclass, `call()` method |
| Layer types | `Dense`, `Conv2D`, `LSTM`, `GRU`, `Embedding`, `Dropout`, `BatchNorm` |
| `model.summary()` | Layer shapes, parameter counts |
| Layer sharing | Shared weights via reuse of layer instance |
| Custom layers | `tf.keras.layers.Layer`, `build()`, `call()` |

---

#### Lesson 03.03 — Keras Training and Callbacks
**File**: `_11_03_03_keras_training_callbacks.md`

| Topics | Subtopics |
|---|---|
| `model.compile` | `optimizer`, `loss`, `metrics` |
| `model.fit` | `epochs`, `batch_size`, `validation_data`, `callbacks` |
| `model.evaluate` | Test set evaluation |
| `model.predict` | Inference |
| Callbacks | `ModelCheckpoint`, `EarlyStopping`, `ReduceLROnPlateau`, `TensorBoard`, `CSVLogger` |
| Custom callbacks | `on_epoch_end`, `on_batch_end` |
| `class_weight` | Imbalanced dataset handling |
| Mixed precision | `tf.keras.mixed_precision.set_global_policy("mixed_float16")` |

---

#### Lesson 03.04 — tf.data Pipeline
**File**: `_11_03_04_tf_data_pipeline.md`

| Topics | Subtopics |
|---|---|
| `tf.data.Dataset` | `from_tensors`, `from_tensor_slices`, `from_generator` |
| Transformations | `map`, `filter`, `batch`, `shuffle`, `repeat`, `prefetch` |
| `AUTOTUNE` | `tf.data.AUTOTUNE`, prefetch buffer |
| `cache()` | In-memory and disk caching |
| `tf.data.TFRecordDataset` | Binary serialized data |
| `tf.io` | `parse_single_example`, `FixedLenFeature` |
| Performance patterns | Parallelized `map`, interleaving |

---

#### Lesson 03.05 — Keras Tuner and AutoKeras
**File**: `_11_03_05_keras_tuner_autokeras.md`

| Topics | Subtopics |
|---|---|
| `keras_tuner` | `HyperModel`, `RandomSearch`, `BayesianOptimization`, `Hyperband` |
| Defining hyperparameter space | `hp.Int`, `hp.Float`, `hp.Choice` |
| `tuner.search` | `epochs`, `validation_data` |
| `tuner.get_best_hyperparameters` | Best config retrieval |
| AutoKeras | `ak.ImageClassifier`, `ak.TextClassifier` |
| AutoKeras blocks | `ak.ResNetBlock`, `ak.BertBlock` |

---

#### Lesson 03.06 — TensorFlow SavedModel and Serving
**File**: `_11_03_06_tensorflow_savedmodel_serving.md`

| Topics | Subtopics |
|---|---|
| SavedModel format | `model.save()`, `tf.saved_model.save()` |
| TFLite conversion | `TFLiteConverter`, quantization |
| TF Serving | `tensorflow-model-server`, REST/gRPC API |
| `tf.saved_model.load` | Loading for inference |
| Signature definition | `serving_default`, input/output specs |
| Concrete functions | `model.get_concrete_function` |

---

#### Lesson 03.07 — TensorBoard and Experiment Tracking
**File**: `_11_03_07_tensorboard_experiment_tracking.md`

| Topics | Subtopics |
|---|---|
| `TensorBoard callback` | Loss/metric curves |
| `tf.summary` | Scalars, histograms, images, text |
| Embeddings projector | Visualizing high-dimensional vectors |
| HParams dashboard | Hyperparameter comparison |
| Profile dashboard | GPU/CPU op profiling |
| MLflow + TF | `mlflow.tensorflow.autolog()` |
| W&B integration | `wandb.keras.WandbCallback` |

---

## MODULE 04 — Training Optimization

**Folder**: `_11_04_training_optimization/`  
**Lesson Count**: 8  
**Learning Order**: 4th

### Lessons

#### Lesson 04.01 — Advanced Optimizers
**File**: `_11_04_01_advanced_optimizers.md`

| Topics | Subtopics |
|---|---|
| Adam variants | NAdam, RAdam, AdaBelief |
| AdamW | Decoupled weight decay, Transformers default |
| LAMB | Layer-wise adaptive rate for large batches |
| Lion | EvoLved Sign Momentum (Google), memory efficient |
| Shampoo | Second-order optimizer |
| Muon | MoMentum + Nesterov + orthogonalization |
| Optimizer comparison | Convergence speed, generalization |

---

#### Lesson 04.02 — Learning Rate Techniques
**File**: `_11_04_02_learning_rate_techniques.md`

| Topics | Subtopics |
|---|---|
| LR Warmup | Linear, cosine warmup schedules |
| 1-Cycle policy | Smith's super-convergence |
| Cosine decay with restarts | SGDR |
| LR Finder | Cyclical LR range test |
| Layer-wise LR | Different LR per layer group |
| Differential LR | Fine-tuning with discriminative LR |

---

#### Lesson 04.03 — Batch Size and Gradient Accumulation
**File**: `_11_04_03_batch_size_gradient_accumulation.md`

| Topics | Subtopics |
|---|---|
| Batch size effect | Large batch → sharp minima, LR scaling |
| Linear scaling rule | LR ∝ batch size (Goyal et al.) |
| Gradient accumulation | `accumulate_grad_batches`, effective batch |
| Ghost batch norm | Large batch BN fix |
| Micro-batch training | Multi-GPU efficiency |

---

#### Lesson 04.04 — Mixed Precision Training
**File**: `_11_04_04_mixed_precision_training.md`

| Topics | Subtopics |
|---|---|
| FP16 vs BF16 | Precision tradeoffs, Tensor Cores |
| Loss scaling | Dynamic loss scaler, `GradScaler` |
| PyTorch AMP | `torch.amp.autocast`, `GradScaler` |
| Keras mixed precision | `set_global_policy("mixed_float16")` |
| BF16 training | `torch.bfloat16`, NVIDIA Ampere/H100 |
| Memory savings | Activation recomputation, gradient checkpointing |

---

#### Lesson 04.05 — Gradient Clipping and Stability
**File**: `_11_04_05_gradient_clipping_stability.md`

| Topics | Subtopics |
|---|---|
| Gradient norm clipping | `clip_grad_norm_`, max_norm selection |
| Gradient value clipping | `clip_grad_value_` |
| Exploding gradients | RNN training instability |
| Vanishing gradients | Residual connections as solution |
| Gradient noise | Stochastic depth, dropout regularization |
| Loss spike detection | `torch.isnan` checks |

---

#### Lesson 04.06 — Normalization Layers (Deep Dive)
**File**: `_11_04_06_normalization_layers_deep_dive.md`

| Topics | Subtopics |
|---|---|
| Batch Normalization | Algorithm, `γ`, `β`, running mean/variance |
| Layer Normalization | Normalize across features, Transformer use |
| Group Normalization | Compromise for small batches |
| Instance Normalization | Per-sample, style transfer |
| RMS Normalization | Simplified LN used in LLaMA |
| Spectral Normalization | GAN stability |
| Comparing normalizations | When to use each |

---

#### Lesson 04.07 — Data Augmentation for Deep Learning
**File**: `_11_04_07_data_augmentation_deep_learning.md`

| Topics | Subtopics |
|---|---|
| Standard image augmentation | Flip, crop, rotation, colour jitter |
| `torchvision.transforms.v2` | `RandomResizedCrop`, `ColorJitter`, `AutoAugment` |
| `albumentations` | Faster augmentation library |
| Mixup | Convex combination of two samples |
| CutMix | Patch swapping augmentation |
| AugMix | Mixture of augmentation chains |
| RandAugment | Automated augmentation policy |
| Test-time augmentation (TTA) | Average predictions over augmented copies |
| Augmentation for tabular/NLP | Synonym replacement, noise injection |

---

#### Lesson 04.08 — Curriculum Learning and Training Strategies
**File**: `_11_04_08_curriculum_learning_strategies.md`

| Topics | Subtopics |
|---|---|
| Curriculum learning | Easy → hard sample ordering |
| Self-paced learning | Automatic difficulty estimation |
| Progressive resizing | Train on small images → fine-tune on large |
| Stochastic depth | Layer dropout during training |
| R-Drop | Regularization by Output Distributions |
| Knowledge distillation | Soft targets from teacher |
| Ensemble distillation | Born Again Networks |

---

## MODULE 05 — Convolutional Neural Networks

**Folder**: `_11_05_convolutional_neural_networks/`  
**Lesson Count**: 11  
**Learning Order**: 5th

### Lessons

#### Lesson 05.01 — Convolution Operation and Filters
**File**: `_11_05_01_convolution_operation_and_filters.md`

| Topics | Subtopics |
|---|---|
| 2D Convolution | Kernel, stride, padding, dilation |
| Feature maps | Output shape formula |
| Parameter sharing | Weight tying, translational equivariance |
| `nn.Conv2d` | `in_channels`, `out_channels`, `kernel_size`, `stride`, `padding` |
| Separable convolution | Depthwise + pointwise, MobileNet |
| Dilated convolution | Expanded receptive field without more params |
| Transposed convolution | Upsampling, `nn.ConvTranspose2d` |

---

#### Lesson 05.02 — Pooling and Spatial Reduction
**File**: `_11_05_02_pooling_and_spatial_reduction.md`

| Topics | Subtopics |
|---|---|
| Max pooling | `nn.MaxPool2d`, receptive field growth |
| Average pooling | `nn.AvgPool2d`, global average pooling |
| Global Average Pooling | Replace FC layers, `nn.AdaptiveAvgPool2d(1,1)` |
| Strided convolution | Replacing pooling, learnable downsampling |
| Spatial pyramid pooling | SPP, multi-scale features |

---

#### Lesson 05.03 — Classic CNN Architectures
**File**: `_11_05_03_classic_cnn_architectures.md`

| Topics | Subtopics |
|---|---|
| LeNet-5 | 1998, MNIST, convolution + FC |
| AlexNet | 2012 ImageNet winner, ReLU, dropout |
| VGGNet | 3×3 convolutions, depth |
| GoogLeNet / Inception v1 | Inception module, 1×1 bottleneck |
| Inception v3 / v4 | Factorized convolutions |
| `torchvision.models` | Loading pretrained architectures |

---

#### Lesson 05.04 — ResNet and Skip Connections
**File**: `_11_05_04_resnet_skip_connections.md`

| Topics | Subtopics |
|---|---|
| Degradation problem | Very deep networks train worse |
| Residual block | F(x) + x identity shortcut |
| Bottleneck block | 1×1 → 3×3 → 1×1, parameter reduction |
| ResNet variants | ResNet-18/34/50/101/152 |
| ResNeXt | Grouped convolutions |
| Wide ResNet | Wider channels, fewer layers |
| SE-Net | Squeeze-and-Excitation attention |
| `torchvision.models.resnet50` | Pretrained loading |

---

#### Lesson 05.05 — Efficient CNN Architectures
**File**: `_11_05_05_efficient_cnn_architectures.md`

| Topics | Subtopics |
|---|---|
| MobileNetV1 | Depthwise separable convolutions |
| MobileNetV2 | Inverted residuals, linear bottleneck |
| MobileNetV3 | SE blocks, hard swish |
| EfficientNet | Compound scaling (width, depth, resolution) |
| EfficientNetV2 | Progressive training, Fused-MBConv |
| ConvNeXt | Modernized ResNet with Transformer recipes |
| ShuffleNet | Channel shuffle, group convolutions |
| Latency vs accuracy | Mobile deployment considerations |

---

#### Lesson 05.06 — Image Classification Pipeline
**File**: `_11_05_06_image_classification_pipeline.md`

| Topics | Subtopics |
|---|---|
| Dataset preparation | ImageFolder, custom Dataset |
| Augmentation pipeline | Train vs validation transforms |
| Fine-tuning pretrained CNN | Freeze backbone → train head → unfreeze |
| Evaluation metrics | Top-1, Top-5 accuracy |
| Test-time augmentation | Average predictions |
| Class activation maps | CAM, Grad-CAM visualization |

---

#### Lesson 05.07 — Object Detection: YOLO
**File**: `_11_05_07_object_detection_yolo.md`

| Topics | Subtopics |
|---|---|
| Detection formulation | Bounding box regression + classification |
| Anchor boxes | Predefined aspect ratios, anchor-free concept |
| YOLOv5/v8 architecture | Backbone, FPN neck, detection head |
| `ultralytics` | `YOLO("yolov8n.pt")`, `model.train`, `model.predict` |
| IoU and NMS | Intersection over Union, Non-Maximum Suppression |
| mAP metric | Mean Average Precision, IoU thresholds |
| Custom dataset | YOLO label format, `data.yaml` |

---

#### Lesson 05.08 — Object Detection: Faster R-CNN and SSD
**File**: `_11_05_08_object_detection_faster_rcnn_ssd.md`

| Topics | Subtopics |
|---|---|
| R-CNN family | R-CNN → Fast R-CNN → Faster R-CNN |
| Region Proposal Network | RPN, anchor generation, objectness score |
| ROI Pooling / ROI Align | Fixed-size feature extraction |
| `torchvision.models.detection` | `fasterrcnn_resnet50_fpn`, `retinanet_resnet50_fpn` |
| SSD architecture | Multi-scale default boxes |
| RetinaNet | Focal Loss, class imbalance solution |
| Feature Pyramid Network (FPN) | Multi-scale feature map fusion |

---

#### Lesson 05.09 — Image Segmentation
**File**: `_11_05_09_image_segmentation.md`

| Topics | Subtopics |
|---|---|
| Semantic segmentation | Per-pixel class label |
| FCN | Fully Convolutional Network |
| U-Net | Encoder-decoder with skip connections, medical imaging |
| DeepLab v3+ | Atrous convolutions, ASPP module |
| Panoptic segmentation | Semantic + instance combined |
| Mask R-CNN | Instance segmentation head |
| `torchvision.models.segmentation` | `deeplabv3_resnet50`, `fcn_resnet50` |
| Segment Anything Model (SAM) | Prompt-based universal segmentation |

---

#### Lesson 05.10 — Pose Estimation and Face Recognition
**File**: `_11_05_10_pose_estimation_face_recognition.md`

| Topics | Subtopics |
|---|---|
| Human pose estimation | Keypoint detection, heatmap regression |
| HRNet / ViTPose | High-resolution networks |
| OpenPose | Multi-person, part affinity fields |
| Face detection | MTCNN, RetinaFace |
| Face recognition | FaceNet, ArcFace, CosFace, `facenet-pytorch` |
| Face verification | Siamese networks, threshold |

---

#### Lesson 05.11 — Video Understanding
**File**: `_11_05_11_video_understanding.md`

| Topics | Subtopics |
|---|---|
| Video classification | 3D CNN, two-stream networks |
| Temporal segment networks | Long-range temporal modelling |
| I3D | Inflated 3D convolutions |
| SlowFast | Dual-pathway architecture |
| Video Swin Transformer | Shifted window for video |
| Optical flow | PWC-Net, FlowNet |
| Action detection | Spatio-temporal proposals |

---

## MODULE 06 — Recurrent Neural Networks

**Folder**: `_11_06_recurrent_neural_networks/`  
**Lesson Count**: 8  
**Learning Order**: 6th

### Lessons

#### Lesson 06.01 — Vanilla RNN Architecture
**File**: `_11_06_01_vanilla_rnn_architecture.md`

| Topics | Subtopics |
|---|---|
| Sequence modelling | Why feedforward is insufficient |
| RNN cell | hₜ = f(Wxhxₜ + Whhh_{t-1} + b) |
| BPTT | Backpropagation Through Time |
| Vanishing/exploding gradient | In temporal direction |
| `nn.RNN` | `input_size`, `hidden_size`, `num_layers`, `batch_first` |
| Many-to-many / one-to-many | Sequence task types |

---

#### Lesson 06.02 — LSTM Architecture
**File**: `_11_06_02_lstm_architecture.md`

| Topics | Subtopics |
|---|---|
| LSTM cell | Forget gate, input gate, output gate, cell state |
| Gate equations | f, i, g, o gate math |
| Cell state highway | Long-term memory flow |
| `nn.LSTM` | `input_size`, `hidden_size`, `num_layers`, `dropout`, `bidirectional` |
| Stacked LSTM | Multi-layer hidden representations |
| Bidirectional LSTM | Forward + backward context |
| Packed sequences | `pad_sequence`, `pack_padded_sequence`, variable length |

---

#### Lesson 06.03 — GRU Architecture
**File**: `_11_06_03_gru_architecture.md`

| Topics | Subtopics |
|---|---|
| GRU cell | Reset gate, update gate, no cell state |
| GRU vs LSTM | Fewer parameters, comparable performance |
| `nn.GRU` | Same API as LSTM minus cell state |
| When to choose GRU | Shorter sequences, faster training |

---

#### Lesson 06.04 — Sequence-to-Sequence Models
**File**: `_11_06_04_sequence_to_sequence_models.md`

| Topics | Subtopics |
|---|---|
| Encoder-Decoder architecture | Fixed context vector bottleneck |
| Seq2Seq training | Teacher forcing, scheduled sampling |
| Inference | Greedy decoding, beam search |
| Beam search | Width B, score normalization |
| Applications | Machine translation, summarization, chatbots |

---

#### Lesson 06.05 — Attention Mechanism (RNN-Era)
**File**: `_11_06_05_attention_mechanism_rnn.md`

| Topics | Subtopics |
|---|---|
| Bahdanau attention | Additive attention, alignment scores |
| Luong attention | Multiplicative attention, global vs local |
| Context vector | Weighted sum of encoder hidden states |
| `nn.MultiheadAttention` | Intro (full detail in Transformer module) |
| Copy mechanism | Pointer networks |
| Coverage mechanism | Preventing repetition |

---

#### Lesson 06.06 — RNNs for Time Series
**File**: `_11_06_06_rnns_for_time_series.md`

| Topics | Subtopics |
|---|---|
| Univariate forecasting | Single-step, multi-step |
| Multivariate forecasting | Multiple feature input, multiple output |
| Sliding window Dataset | `TimeseriesDataset` implementation |
| Encoder-only LSTM | Direct many-to-one regression |
| Seq2Seq for multi-step | Encoder → decoder rollout |
| DeepAR | Probabilistic LSTM forecasting |
| Comparison | LSTM vs ARIMA vs LightGBM on M4 |

---

#### Lesson 06.07 — Temporal Convolutional Networks (TCN)
**File**: `_11_06_07_temporal_convolutional_networks.md`

| Topics | Subtopics |
|---|---|
| TCN advantages | Parallelism, stable gradients, long memory |
| Causal convolution | No future leakage |
| Dilated causal convolution | Exponential receptive field |
| Residual block in TCN | Skip connections within TCN |
| WaveNet | Original dilated causal CNN for audio |
| TCN vs LSTM | Speed, parallelism, long-range dependency |

---

#### Lesson 06.08 — Anomaly Detection with RNNs
**File**: `_11_06_08_anomaly_detection_rnns.md`

| Topics | Subtopics |
|---|---|
| LSTM Autoencoder | Encode → decode, reconstruction error |
| Threshold-based detection | Percentile of reconstruction error |
| DeepAnT | Convolutional anomaly detection |
| MSCRED | Multi-Scale Convolutional Recurrent |
| SPOT / DSPOT | POT-based extreme value thresholding |
| Real-time inference | Windowed streaming anomaly detection |

---

## MODULE 07 — Attention and Transformers

**Folder**: `_11_07_attention_and_transformers/`  
**Lesson Count**: 9  
**Learning Order**: 7th  
**Note**: Full NLP Transformers (BERT, GPT, T5) are in Phase 4 (NLP). This module covers architecture and vision applications.

### Lessons

#### Lesson 07.01 — Scaled Dot-Product Attention
**File**: `_11_07_01_scaled_dot_product_attention.md`

| Topics | Subtopics |
|---|---|
| Query, Key, Value | QKV formulation |
| Attention scores | A = softmax(QKᵀ / √dₖ) · V |
| Scaling factor √dₖ | Gradient stability rationale |
| Attention mask | Padding mask, causal mask |
| `torch.nn.functional.scaled_dot_product_attention` | Flash Attention kernel (PyTorch 2.0+) |
| Complexity | O(n²d) in full attention |

---

#### Lesson 07.02 — Multi-Head Attention
**File**: `_11_07_02_multi_head_attention.md`

| Topics | Subtopics |
|---|---|
| Multiple attention heads | Different representation subspaces |
| Linear projections | W_Q, W_K, W_V per head |
| Concatenation and projection | Head output fusion |
| `nn.MultiheadAttention` | `embed_dim`, `num_heads`, `dropout`, `batch_first` |
| Computational cost | h heads × dₖ per head |
| Head analysis | What different heads attend to |

---

#### Lesson 07.03 — Positional Encoding
**File**: `_11_07_03_positional_encoding.md`

| Topics | Subtopics |
|---|---|
| Why position matters | Attention is permutation-invariant |
| Sinusoidal encoding | Vaswani et al. formula |
| Learned positional embeddings | `nn.Embedding(max_len, d_model)` |
| Relative positional encoding | T5 bias, ALiBi, RoPE |
| RoPE (Rotary PE) | LLaMA-style, 2D rotation matrix |
| ALiBi | Extrapolation to longer sequences |

---

#### Lesson 07.04 — Transformer Encoder Architecture
**File**: `_11_07_04_transformer_encoder_architecture.md`

| Topics | Subtopics |
|---|---|
| Encoder block | MHA → Add+Norm → FFN → Add+Norm |
| Feed-Forward Network | 2-layer MLP with GELU/ReLU |
| Pre-LN vs Post-LN | Stability comparison |
| Stacking encoders | N identical layers |
| Encoder output | Contextualised token representations |
| Implementation | PyTorch `nn.TransformerEncoderLayer` |

---

#### Lesson 07.05 — Transformer Decoder Architecture
**File**: `_11_07_05_transformer_decoder_architecture.md`

| Topics | Subtopics |
|---|---|
| Decoder block | Masked MHA → Cross-Attention → FFN |
| Causal masking | Autoregressive left-to-right attention |
| Cross-attention | Q from decoder, K/V from encoder |
| Autoregressive generation | Token-by-token decoding |
| `nn.TransformerDecoderLayer` | PyTorch implementation |
| Encoder-Decoder vs Decoder-only | T5 vs GPT paradigm |

---

#### Lesson 07.06 — Vision Transformer (ViT)
**File**: `_11_07_06_vision_transformer_vit.md`

| Topics | Subtopics |
|---|---|
| Patch embedding | Split image into P×P patches |
| Linear patch projection | `nn.Conv2d(stride=P)` |
| CLS token | Prepended classification token |
| Positional embedding | Learnable 1D, 2D sinusoidal |
| ViT architecture | Standard Transformer Encoder on patches |
| ViT variants | ViT-B/16, ViT-L/32, ViT-H |
| `timm` library | `timm.create_model("vit_base_patch16_224")` |
| ViT vs CNN | When ViT wins (large data, pretraining) |

---

#### Lesson 07.07 — Hierarchical Vision Transformers
**File**: `_11_07_07_hierarchical_vision_transformers.md`

| Topics | Subtopics |
|---|---|
| Swin Transformer | Shifted window attention, hierarchical features |
| Window attention | W×W local attention, O(n) complexity |
| Shifted windows | Cross-window connections |
| Patch merging | Spatial downsampling |
| DeiT | Data-efficient ViT, distillation token |
| BEiT | BERT-style pretraining for ViT |
| MViT | Multiscale Vision Transformer for video |

---

#### Lesson 07.08 — Efficient Attention Mechanisms
**File**: `_11_07_08_efficient_attention_mechanisms.md`

| Topics | Subtopics |
|---|---|
| Linear attention | Kernel approximation, O(n) |
| Performer | FAVOR+ random feature maps |
| Longformer | Sliding window + global attention |
| BigBird | Random + window + global |
| Flash Attention | IO-aware exact attention, GPU memory savings |
| Flash Attention 2/3 | Further optimizations |
| Multi-Query Attention | Shared KV heads, faster inference |
| Grouped Query Attention | LLaMA 2/3 style |

---

#### Lesson 07.09 — DETR and Detection Transformers
**File**: `_11_07_09_detr_detection_transformers.md`

| Topics | Subtopics |
|---|---|
| DETR architecture | CNN backbone + Transformer encoder-decoder |
| Object queries | Learned query vectors for detections |
| Hungarian matching | Bipartite set loss |
| `transformers.DetrForObjectDetection` | HuggingFace DETR |
| Deformable DETR | Deformable attention, faster convergence |
| DINO (Self-supervised DETR) | Self-supervised pretraining for detection |

---

## MODULE 08 — Generative Models

**Folder**: `_11_08_generative_models/`  
**Lesson Count**: 9  
**Learning Order**: 8th

### Lessons

#### Lesson 08.01 — Autoencoders
**File**: `_11_08_01_autoencoders.md`

| Topics | Subtopics |
|---|---|
| Autoencoder architecture | Encoder → Bottleneck → Decoder |
| Reconstruction loss | MSE, BCE |
| Undercomplete AE | Dimensionality reduction via bottleneck |
| Denoising Autoencoder | Corrupted input → clean reconstruction |
| Sparse Autoencoder | L1 penalty on activations |
| Contractive Autoencoder | Frobenius norm of Jacobian |
| Applications | Anomaly detection, pre-training, representation |

---

#### Lesson 08.02 — Variational Autoencoders (VAE)
**File**: `_11_08_02_variational_autoencoders_vae.md`

| Topics | Subtopics |
|---|---|
| VAE objective | ELBO = Reconstruction - KL Divergence |
| Reparameterization trick | z = μ + σ · ε, gradient flow |
| Encoder outputs | μ and log σ² |
| KL divergence | KL(q(z|x) || p(z)), standard normal prior |
| Decoder | p(x|z), Bernoulli or Gaussian |
| Vector arithmetic | Latent space interpolation |
| β-VAE | Disentangled representations |
| VQ-VAE | Discrete latent space, codebook |

---

#### Lesson 08.03 — GAN Foundations
**File**: `_11_08_03_gan_foundations.md`

| Topics | Subtopics |
|---|---|
| GAN objective | Minimax game: min_G max_D V(D,G) |
| Generator | Random noise → realistic samples |
| Discriminator | Real vs fake classification |
| Training dynamics | Nash equilibrium, mode collapse |
| Training tricks | Label smoothing, instance noise, one-sided smoothing |
| DCGAN | Deep Convolutional GAN architecture |
| Loss variants | Non-saturating loss, Wasserstein loss |

---

#### Lesson 08.04 — Advanced GANs
**File**: `_11_08_04_advanced_gans.md`

| Topics | Subtopics |
|---|---|
| WGAN | Wasserstein distance, Lipschitz constraint |
| WGAN-GP | Gradient penalty, `gp_lambda` |
| Progressive GAN (ProGAN) | Growing resolution |
| StyleGAN / StyleGAN2/3 | Style modulation, W latent space, ADA |
| Conditional GAN (cGAN) | Class-conditioned generation |
| InfoGAN | Mutual information maximization |
| CycleGAN | Unpaired image-to-image translation |
| Pix2Pix | Paired image translation |

---

#### Lesson 08.05 — Score-Based and Flow Models
**File**: `_11_08_05_score_based_flow_models.md`

| Topics | Subtopics |
|---|---|
| Normalizing flows | Exact density, invertible transforms |
| RealNVP | Affine coupling layers |
| Glow | Generative flow, invertible 1×1 conv |
| Score matching | Estimating ∇_x log p(x) |
| Denoising score matching | NCSN, Langevin dynamics |
| Flow Matching | Probability flow ODE, rectified flow |

---

#### Lesson 08.06 — Diffusion Models
**File**: `_11_08_06_diffusion_models.md`

| Topics | Subtopics |
|---|---|
| DDPM | Forward noising, reverse denoising |
| Noise schedule | Linear, cosine, sigmoid |
| U-Net denoiser | Time embedding, skip connections |
| ELBO objective | Variational lower bound for diffusion |
| DDIM | Deterministic sampling, fewer steps |
| Latent Diffusion | Compress to latent space first (Stable Diffusion) |
| Stable Diffusion | `diffusers` library, CLIP text encoder |
| Classifier-free guidance | CFG, unconditional + conditional |
| ControlNet | Conditioning on edges, depth, pose |

---

#### Lesson 08.07 — Text-to-Image Systems
**File**: `_11_08_07_text_to_image_systems.md`

| Topics | Subtopics |
|---|---|
| DALL-E 2 architecture | CLIP + diffusion prior + decoder |
| Imagen | Cascaded diffusion, T5 text encoder |
| Stable Diffusion | Latent diffusion, VAE + CLIP + U-Net |
| `diffusers` pipeline | `StableDiffusionPipeline`, `from_pretrained` |
| Prompt engineering for images | Positive/negative prompts |
| Fine-tuning | Textual Inversion, DreamBooth, LoRA for diffusion |
| SDXL | Improved architecture, multiple text encoders |
| Flux | Rectified flow transformer architecture |

---

#### Lesson 08.08 — Evaluation of Generative Models
**File**: `_11_08_08_evaluation_generative_models.md`

| Topics | Subtopics |
|---|---|
| FID (Fréchet Inception Distance) | Feature distribution comparison |
| IS (Inception Score) | Diversity + quality combined |
| CLIP Score | Image-text alignment |
| LPIPS | Perceptual similarity |
| Precision and Recall | Coverage and fidelity |
| Human evaluation | MOS, preference studies |
| `torch-fidelity` | FID/IS computation library |

---

#### Lesson 08.09 — Generative Models for Tabular and Audio
**File**: `_11_08_09_generative_models_tabular_audio.md`

| Topics | Subtopics |
|---|---|
| CTGAN | Conditional tabular GAN |
| TVAE | Tabular VAE |
| `sdv` library | Synthetic Data Vault |
| WaveNet | Dilated causal CNN for audio |
| WaveGAN | GAN for raw audio |
| MelGAN | Spectrogram → waveform |
| Evaluation | Statistical similarity, downstream ML utility |

---

## MODULE 09 — Self-Supervised Learning

**Folder**: `_11_09_self_supervised_learning/`  
**Lesson Count**: 6  
**Learning Order**: 9th

### Lessons

#### Lesson 09.01 — Self-Supervised Learning Foundations
**File**: `_11_09_01_self_supervised_learning_foundations.md`

| Topics | Subtopics |
|---|---|
| Pretext tasks | Rotation prediction, jigsaw, colorization |
| Contrastive vs generative SSL | SimCLR vs MAE comparison |
| Data2Vec | Self-supervised across modalities |
| Label efficiency | How SSL enables few-shot learning |

---

#### Lesson 09.02 — Contrastive Learning
**File**: `_11_09_02_contrastive_learning.md`

| Topics | Subtopics |
|---|---|
| NT-Xent Loss | Normalized temperature-scaled cross-entropy |
| SimCLR | Augmentation pair, projection head, large batch |
| MoCo v1/v2/v3 | Momentum encoder, memory bank/queue |
| BYOL | No negative pairs, EMA teacher |
| SimSiam | Siamese networks, stop-gradient |
| `lightly` library | Contrastive learning framework |

---

#### Lesson 09.03 — Masked Autoencoders (MAE)
**File**: `_11_09_03_masked_autoencoders_mae.md`

| Topics | Subtopics |
|---|---|
| MAE concept | 75% masking, reconstruct pixels |
| Asymmetric encoder-decoder | Sparse encoder, lightweight decoder |
| MAE vs BEiT | Pixel targets vs token targets |
| Video MAE | Temporal tube masking |
| MAE for audio | Masked spectrogram prediction |
| Fine-tuning MAE | Linear probing vs full fine-tuning |

---

#### Lesson 09.04 — DINO and Self-Distillation
**File**: `_11_09_04_dino_self_distillation.md`

| Topics | Subtopics |
|---|---|
| DINO v1 | Self-distillation, no negatives, centering |
| Teacher-student EMA | Momentum-updated teacher |
| Local-global crop strategy | Multi-crop augmentation |
| DINOv2 | Curated data, registers, stronger features |
| DINO features | Semantic segmentation without labels |
| `dinov2` | Facebook Research model hub |

---

#### Lesson 09.05 — Clustering-Based SSL
**File**: `_11_09_05_clustering_based_ssl.md`

| Topics | Subtopics |
|---|---|
| DeepCluster | K-Means as pseudo-labels |
| SwAV | Online clustering, sinkhorn-knopp |
| PCL | Prototypical contrastive learning |
| SCAN | Semantic clustering by adopting nearest neighbours |

---

#### Lesson 09.06 — Multi-Modal Self-Supervised Learning
**File**: `_11_09_06_multimodal_ssl.md`

| Topics | Subtopics |
|---|---|
| CLIP | Contrastive Image-Language Pretraining |
| `clip` / `open_clip` | Model loading, embed images and text |
| Zero-shot classification | Using CLIP for classification without labels |
| ALIGN | Dual encoder, noisy pairs |
| FLAVA | Multi-modal BERT |
| ImageBind | Six modalities aligned |

---

## MODULE 10 — Transfer Learning and Fine-Tuning

**Folder**: `_11_10_transfer_learning_and_finetuning/`  
**Lesson Count**: 7  
**Learning Order**: 10th

### Lessons

#### Lesson 10.01 — Transfer Learning Fundamentals
**File**: `_11_10_01_transfer_learning_fundamentals.md`

| Topics | Subtopics |
|---|---|
| Domain adaptation | Source → Target domain shift |
| Feature extraction | Frozen backbone → new head |
| Fine-tuning | Unfreeze all layers, small LR |
| Discriminative fine-tuning | Different LR per layer group |
| When to freeze vs unfreeze | Dataset size, domain similarity |
| `timm` for vision models | Pretrained model zoo |

---

#### Lesson 10.02 — Fine-Tuning ImageNet Pretrained CNNs
**File**: `_11_10_02_finetuning_imagenet_pretrained_cnns.md`

| Topics | Subtopics |
|---|---|
| Loading pretrained model | `torchvision.models.resnet50(pretrained=True)` |
| Replacing classifier head | Custom `nn.Linear` for num_classes |
| Progressive unfreeze | Freeze → train head → gradually unfreeze |
| Layer-wise LR decay | `[{'params': layer.parameters(), 'lr': lr * factor}]` |
| Augmentation strategy | RandAugment + Mixup |
| Medical / satellite imaging | Domain-specific fine-tuning |

---

#### Lesson 10.03 — Few-Shot Learning
**File**: `_11_10_03_few_shot_learning.md`

| Topics | Subtopics |
|---|---|
| N-way K-shot setup | N classes, K examples each |
| Siamese networks | Similarity learning |
| Prototypical networks | Class prototype mean embeddings |
| MAML | Model-Agnostic Meta-Learning |
| Reptile | Simpler MAML variant |
| `learn2learn` | Few-shot PyTorch library |

---

#### Lesson 10.04 — Domain Adaptation
**File**: `_11_10_04_domain_adaptation.md`

| Topics | Subtopics |
|---|---|
| Covariate shift | Input distribution change |
| DANN | Domain-Adversarial Neural Network |
| MMD loss | Maximum Mean Discrepancy |
| CORAL | Correlation alignment |
| Test-time adaptation | Entropy minimization at test time |
| Source-free DA | No access to source data |

---

#### Lesson 10.05 — Knowledge Distillation
**File**: `_11_10_05_knowledge_distillation.md`

| Topics | Subtopics |
|---|---|
| Hinton distillation | Soft targets, temperature T |
| Feature distillation | Intermediate layer matching |
| Response distillation | Output logit matching |
| Data-free distillation | No original training data |
| Distillation in NLP | DistilBERT, TinyBERT |
| Self-distillation | Born Again Networks, DINO |
| `torch.nn.functional.kl_div` | Loss implementation |

---

#### Lesson 10.06 — Parameter-Efficient Fine-Tuning (PEFT) for Vision
**File**: `_11_10_06_peft_for_vision.md`

| Topics | Subtopics |
|---|---|
| Adapter layers | Bottleneck adapters per layer |
| LoRA for ViT | Low-rank weight updates |
| Prompt tuning | Visual prompt tokens prepended |
| VPT (Visual Prompt Tuning) | Learnable patch tokens |
| `peft` library | `LoraConfig`, `get_peft_model` for ViT |
| BitFit | Bias-term fine-tuning only |

---

#### Lesson 10.07 — Multi-Task Learning
**File**: `_11_10_07_multi_task_learning.md`

| Topics | Subtopics |
|---|---|
| Hard parameter sharing | Shared backbone, task-specific heads |
| Soft parameter sharing | Regularized weight sharing |
| Task weighting | Uncertainty weighting, gradient surgery |
| GradNorm | Gradient normalization for MTL |
| Multi-task loss | Weighted sum, `UncertaintyLoss` |
| MTL for vision | Detection + segmentation + classification |

---

## MODULE 11 — Model Compression and Deployment

**Folder**: `_11_11_model_compression_and_deployment/`  
**Lesson Count**: 7  
**Learning Order**: 11th

### Lessons

#### Lesson 11.01 — Quantization
**File**: `_11_11_01_quantization.md`

| Topics | Subtopics |
|---|---|
| Quantization basics | FP32 → INT8 / INT4 |
| Post-Training Quantization | `torch.quantization.quantize_dynamic` |
| Static quantization | Calibration dataset, `prepare`, `convert` |
| Quantization-Aware Training | Fake quantization nodes |
| ONNX quantization | `onnxruntime.quantization` |
| GPTQ | Weight quantization for LLMs |
| AWQ | Activation-aware weight quantization |
| BitsAndBytes | 4-bit / 8-bit loading |

---

#### Lesson 11.02 — Pruning
**File**: `_11_11_02_pruning.md`

| Topics | Subtopics |
|---|---|
| Unstructured pruning | Weight-level sparsity, `torch.nn.utils.prune` |
| Structured pruning | Filter/channel/layer removal |
| Magnitude pruning | Remove smallest-magnitude weights |
| Lottery Ticket Hypothesis | Sparse subnetworks that train effectively |
| Movement pruning | Gradient-guided pruning during fine-tuning |
| Iterative pruning | Prune → retrain → repeat |

---

#### Lesson 11.03 — Model Distillation (Applied)
**File**: `_11_11_03_model_distillation_applied.md`

| Topics | Subtopics |
|---|---|
| Teacher-student pipeline | Full training loop |
| `nn.KLDivLoss` | KL divergence loss |
| Temperature calibration | T=1 (hard) vs T=4 (soft) |
| Task-specific distillation | Classification, detection |
| Online distillation | DML: mutual learning |

---

#### Lesson 11.04 — ONNX and TensorRT Deployment
**File**: `_11_11_04_onnx_tensorrt_deployment.md`

| Topics | Subtopics |
|---|---|
| ONNX export | `torch.onnx.export`, opset version |
| ONNX Runtime | `InferenceSession`, EP selection (CPU, CUDA) |
| TensorRT | FP16/INT8 engine, `trtexec` |
| `torch2trt` | PyTorch to TensorRT in one call |
| Triton Inference Server | Model serving, batching, backend |
| Benchmark | Latency, throughput, memory |

---

#### Lesson 11.05 — TensorFlow Lite and Edge Deployment
**File**: `_11_11_05_tensorflow_lite_edge_deployment.md`

| Topics | Subtopics |
|---|---|
| TFLite conversion | `TFLiteConverter.from_saved_model` |
| Quantization in TFLite | INT8 with representative dataset |
| Delegate | GPU delegate, NNAPI delegate |
| Coral Edge TPU | `edgetpu_compiler`, USB and PCIe |
| Raspberry Pi deployment | `tflite-runtime` |
| Arduino / ESP32 | TensorFlow Lite Micro, TFLM |

---

#### Lesson 11.06 — Serving with Triton and FastAPI
**File**: `_11_11_06_serving_triton_fastapi.md`

| Topics | Subtopics |
|---|---|
| Triton Inference Server | `model_repository`, backends |
| gRPC vs REST | Triton client, protocol buffers |
| Dynamic batching | Throughput optimization |
| Model ensemble | Pipeline of models in Triton |
| FastAPI wrapper | REST layer over loaded model |
| Async inference | Non-blocking prediction |

---

#### Lesson 11.07 — Benchmarking and Profiling
**File**: `_11_11_07_benchmarking_profiling.md`

| Topics | Subtopics |
|---|---|
| `torch.profiler` | Chrome trace, FLOP count |
| `fvcore` | FLOPs and parameter counting |
| `torchmetrics` | Standardized metric computation |
| Latency benchmarking | Warmup runs, `torch.cuda.synchronize` |
| Memory profiling | `torch.cuda.memory_summary` |
| Power consumption | NVIDIA `nvidia-smi dmon`, energy metrics |
| Edge benchmarks | MLPerf Inference, MobileNet latency tables |

---

## MODULE 12 — Industry Projects

**Folder**: `_11_12_industry_projects/`  
**Lesson Count**: 6  
**Learning Order**: 12th (Capstone)

### Lessons

#### Lesson 12.01 — Image Classification System (Production)
**File**: `_11_12_01_image_classification_system_production.md`

| Topics | Subtopics |
|---|---|
| Dataset | Custom 10-class dataset |
| Model | EfficientNetV2-S fine-tuned |
| Training pipeline | AMP + RandAugment + Mixup |
| Evaluation | Top-1, Top-5, Grad-CAM visualization |
| Deployment | ONNX → FastAPI → Docker |
| Monitoring | Evidently image distribution drift |

---

#### Lesson 12.02 — Object Detection System
**File**: `_11_12_02_object_detection_system.md`

| Topics | Subtopics |
|---|---|
| Dataset | Custom labeled with Roboflow |
| Model | YOLOv8 + Faster R-CNN comparison |
| Training | `ultralytics` + `torchvision.detection` |
| Evaluation | mAP@0.5, mAP@0.5:0.95 |
| Deployment | TensorRT engine + Triton serving |
| Use case | Manufacturing defect detection |

---

#### Lesson 12.03 — Medical Image Segmentation
**File**: `_11_12_03_medical_image_segmentation.md`

| Topics | Subtopics |
|---|---|
| Dataset | BTCV / LiTS / ISIC skin lesion |
| Model | U-Net + Swin-UNETR |
| Loss | Dice loss + BCE combined |
| Augmentation | Elastic deformation, intensity shift |
| MONAI framework | Medical-specific transforms, sliding window inference |
| Evaluation | Dice score, Hausdorff distance |

---

#### Lesson 12.04 — Generative Image Pipeline
**File**: `_11_12_04_generative_image_pipeline.md`

| Topics | Subtopics |
|---|---|
| Task | Fine-tune Stable Diffusion on custom style |
| Technique | DreamBooth / LoRA fine-tuning |
| `diffusers` pipeline | Full training code |
| CFG | Guidance scale tuning |
| Evaluation | FID, CLIP score |
| Use case | Product image generation for e-commerce |

---

#### Lesson 12.05 — Time Series Forecasting with Deep Learning
**File**: `_11_12_05_time_series_forecasting_deep_learning.md`

| Topics | Subtopics |
|---|---|
| Dataset | ETTh1, M4 competition |
| Models | TCN, N-BEATS, PatchTST, TimesNet |
| `neuralforecast` library | Unified DL forecasting framework |
| Evaluation | SMAPE, MASE, CRPS (probabilistic) |
| Deployment | Scheduled batch inference pipeline |

---

#### Lesson 12.06 — Anomaly Detection System (Industrial IoT)
**File**: `_11_12_06_anomaly_detection_industrial_iot.md`

| Topics | Subtopics |
|---|---|
| Data | SMAP / MSL / SMD industrial sensor datasets |
| Models | LSTM-AE, TranAD, USAD |
| Evaluation | F1 (point-adjusted), precision, recall |
| Streaming inference | Windowed real-time detection |
| Edge deployment | ONNX → Raspberry Pi / Jetson Nano |
| Integration | MQTT → detection pipeline → alert |

---

## Full Folder Structure

```
docs/curriculum/_11_deep_learning/
│
├── _11_01_dl_foundations/
│   ├── _11_01_01_artificial_neuron_and_perceptron.md
│   ├── _11_01_02_feedforward_neural_networks_mlp.md
│   ├── _11_01_03_activation_functions.md
│   ├── _11_01_04_loss_functions_deep_learning.md
│   ├── _11_01_05_backpropagation_computational_graphs.md
│   ├── _11_01_06_weight_initialization.md
│   ├── _11_01_07_regularization_techniques.md
│   └── _11_01_08_neural_network_capacity_generalization.md
│
├── _11_02_pytorch_framework/
│   ├── _11_02_01_pytorch_tensors_autograd.md
│   ├── _11_02_02_building_models_nn_module.md
│   ├── _11_02_03_pytorch_optimizers.md
│   ├── _11_02_04_learning_rate_scheduling.md
│   ├── _11_02_05_pytorch_data_pipeline.md
│   ├── _11_02_06_training_loop_architecture.md
│   ├── _11_02_07_debugging_profiling_pytorch.md
│   ├── _11_02_08_distributed_training_pytorch.md
│   └── _11_02_09_torchscript_model_export.md
│
├── _11_03_tensorflow_keras/
│   ├── _11_03_01_tensorflow_2x_architecture.md
│   ├── _11_03_02_keras_sequential_functional_api.md
│   ├── _11_03_03_keras_training_callbacks.md
│   ├── _11_03_04_tf_data_pipeline.md
│   ├── _11_03_05_keras_tuner_autokeras.md
│   ├── _11_03_06_tensorflow_savedmodel_serving.md
│   └── _11_03_07_tensorboard_experiment_tracking.md
│
├── _11_04_training_optimization/
│   ├── _11_04_01_advanced_optimizers.md
│   ├── _11_04_02_learning_rate_techniques.md
│   ├── _11_04_03_batch_size_gradient_accumulation.md
│   ├── _11_04_04_mixed_precision_training.md
│   ├── _11_04_05_gradient_clipping_stability.md
│   ├── _11_04_06_normalization_layers_deep_dive.md
│   ├── _11_04_07_data_augmentation_deep_learning.md
│   └── _11_04_08_curriculum_learning_strategies.md
│
├── _11_05_convolutional_neural_networks/
│   ├── _11_05_01_convolution_operation_and_filters.md
│   ├── _11_05_02_pooling_and_spatial_reduction.md
│   ├── _11_05_03_classic_cnn_architectures.md
│   ├── _11_05_04_resnet_skip_connections.md
│   ├── _11_05_05_efficient_cnn_architectures.md
│   ├── _11_05_06_image_classification_pipeline.md
│   ├── _11_05_07_object_detection_yolo.md
│   ├── _11_05_08_object_detection_faster_rcnn_ssd.md
│   ├── _11_05_09_image_segmentation.md
│   ├── _11_05_10_pose_estimation_face_recognition.md
│   └── _11_05_11_video_understanding.md
│
├── _11_06_recurrent_neural_networks/
│   ├── _11_06_01_vanilla_rnn_architecture.md
│   ├── _11_06_02_lstm_architecture.md
│   ├── _11_06_03_gru_architecture.md
│   ├── _11_06_04_sequence_to_sequence_models.md
│   ├── _11_06_05_attention_mechanism_rnn.md
│   ├── _11_06_06_rnns_for_time_series.md
│   ├── _11_06_07_temporal_convolutional_networks.md
│   └── _11_06_08_anomaly_detection_rnns.md
│
├── _11_07_attention_and_transformers/
│   ├── _11_07_01_scaled_dot_product_attention.md
│   ├── _11_07_02_multi_head_attention.md
│   ├── _11_07_03_positional_encoding.md
│   ├── _11_07_04_transformer_encoder_architecture.md
│   ├── _11_07_05_transformer_decoder_architecture.md
│   ├── _11_07_06_vision_transformer_vit.md
│   ├── _11_07_07_hierarchical_vision_transformers.md
│   ├── _11_07_08_efficient_attention_mechanisms.md
│   └── _11_07_09_detr_detection_transformers.md
│
├── _11_08_generative_models/
│   ├── _11_08_01_autoencoders.md
│   ├── _11_08_02_variational_autoencoders_vae.md
│   ├── _11_08_03_gan_foundations.md
│   ├── _11_08_04_advanced_gans.md
│   ├── _11_08_05_score_based_flow_models.md
│   ├── _11_08_06_diffusion_models.md
│   ├── _11_08_07_text_to_image_systems.md
│   ├── _11_08_08_evaluation_generative_models.md
│   └── _11_08_09_generative_models_tabular_audio.md
│
├── _11_09_self_supervised_learning/
│   ├── _11_09_01_self_supervised_learning_foundations.md
│   ├── _11_09_02_contrastive_learning.md
│   ├── _11_09_03_masked_autoencoders_mae.md
│   ├── _11_09_04_dino_self_distillation.md
│   ├── _11_09_05_clustering_based_ssl.md
│   └── _11_09_06_multimodal_ssl.md
│
├── _11_10_transfer_learning_and_finetuning/
│   ├── _11_10_01_transfer_learning_fundamentals.md
│   ├── _11_10_02_finetuning_imagenet_pretrained_cnns.md
│   ├── _11_10_03_few_shot_learning.md
│   ├── _11_10_04_domain_adaptation.md
│   ├── _11_10_05_knowledge_distillation.md
│   ├── _11_10_06_peft_for_vision.md
│   └── _11_10_07_multi_task_learning.md
│
├── _11_11_model_compression_and_deployment/
│   ├── _11_11_01_quantization.md
│   ├── _11_11_02_pruning.md
│   ├── _11_11_03_model_distillation_applied.md
│   ├── _11_11_04_onnx_tensorrt_deployment.md
│   ├── _11_11_05_tensorflow_lite_edge_deployment.md
│   ├── _11_11_06_serving_triton_fastapi.md
│   └── _11_11_07_benchmarking_profiling.md
│
└── _11_12_industry_projects/
    ├── _11_12_01_image_classification_system_production.md
    ├── _11_12_02_object_detection_system.md
    ├── _11_12_03_medical_image_segmentation.md
    ├── _11_12_04_generative_image_pipeline.md
    ├── _11_12_05_time_series_forecasting_deep_learning.md
    └── _11_12_06_anomaly_detection_industrial_iot.md
```

---

## Learning Order

```
01 DL Foundations
    ↓
02 PyTorch Framework
    ↓
03 TensorFlow & Keras
    ↓
04 Training Optimization
    ↓
05 CNNs  (Image classification → Detection → Segmentation → Video)
    ↓
06 RNNs  (LSTM → GRU → Seq2Seq → TCN → Anomaly)
    ↓
07 Attention & Transformers  (Attention → ViT → DETR)
    ↓
08 Generative Models  (AE → VAE → GAN → Diffusion)
    ↓
09 Self-Supervised Learning
    ↓
10 Transfer Learning & Fine-Tuning
    ↓
11 Model Compression & Deployment
    ↓
12 Industry Projects (Capstone)
```

---

## Summary Statistics

| Module | Title | Lessons |
|---|---|---|
| 01 | DL Foundations | 8 |
| 02 | PyTorch Framework | 9 |
| 03 | TensorFlow & Keras | 7 |
| 04 | Training Optimization | 8 |
| 05 | CNNs | 11 |
| 06 | RNNs | 8 |
| 07 | Attention & Transformers | 9 |
| 08 | Generative Models | 9 |
| 09 | Self-Supervised Learning | 6 |
| 10 | Transfer Learning & Fine-Tuning | 7 |
| 11 | Model Compression & Deployment | 7 |
| 12 | Industry Projects | 6 |
| **TOTAL** | | **95 lessons** |

---

## Phase 3 Handoff (Computer Vision)

Nodes introduced in Phase 2 and fully extended in Phase 3:
- YOLO, Faster R-CNN, Mask R-CNN, SAM → full CV pipeline
- ViT, DETR → advanced vision architecture
- CLIP → zero-shot CV
- OCR, face recognition, medical imaging deep dives
