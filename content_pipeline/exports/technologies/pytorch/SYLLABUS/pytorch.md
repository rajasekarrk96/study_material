# PyTorch — Master Syllabus

**Target Role:** Deep Learning Engineer / AI Researcher / ML Systems Engineer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 20 Hours  
**Prerequisites:** foundations/core-python, foundations/ds-math  
**Required Courses:** foundations/core-python, foundations/ds-math  
**Optional Courses:** technologies/docker  

---

## Study Flow

### Module 1 — Tensors & Memory Layout
1. **PyTorch Tensor Fundamentals** (Tensor creation, data types, CPU/GPU device allocation, tensor cloning vs views)
2. **Tensor Indexing, Slicing & Reshaping** (Advanced indexing, `view()`, `reshape()`, `squeeze()`, `unsqueeze()`, stride & contiguous memory)
3. **Mathematical & Matrix Operations** (Element-wise ops, matrix multiplication `matmul()`, `bmm()`, broadcasting semantics)

### Module 2 — Autograd & Computational Graphs
1. **Automatic Differentiation with Autograd** (Computational graph construction, `requires_grad`, backward pass, `.grad` accumulation)
2. **Controlling Gradient Tracking** (`torch.no_grad()`, `torch.inference_mode()`, `.detach()`, custom autograd functions)
3. **Hook Functions for Debugging** (Tensor hooks, module forward/backward hooks, inspecting intermediate activations & gradients)

### Module 3 — Neural Network Architecture with `nn.Module`
1. **Building Custom Layers and Models** (Subclassing `nn.Module`, parameter registration, buffer registration)
2. **Linear, Convolutional & Normalization Layers** (`nn.Linear`, `nn.Conv2d`, `nn.BatchNorm2d`, `nn.LayerNorm`, activations)
3. **Sequential & Functional Composition** (`nn.Sequential`, `nn.ModuleList`, `nn.ModuleDict`, branching architectures)

### Module 4 — Data Ingestion & Pipelines
1. **Custom Datasets & Ingestion** (Subclassing `torch.utils.data.Dataset`, indexing, memory-mapped data loading)
2. **DataLoaders & Performance Optimization** (`DataLoader`, `batch_size`, `shuffle`, `num_workers`, `pin_memory`, custom `collate_fn`)
3. **Data Transformations & Pipelines** (`torchvision.transforms.v2`, Albumentations integration)

### Module 5 — Training Loop Architecture & Optimization
1. **Standard Training & Validation Loop** (Zeroing gradients, forward pass, loss calculation, backward pass, optimizer step)
2. **Optimizers & Parameter Updates** (`torch.optim.SGD`, `Adam`, `AdamW`, weight decay, learning rate schedulers)
3. **Loss Functions & Metrics** (`nn.CrossEntropyLoss`, `nn.MSELoss`, `nn.BCEWithLogitsLoss`, torchmetrics integration)
4. **Mixed Precision Training (AMP)** (`torch.cuda.amp.autocast`, `GradScaler`, memory savings and compute acceleration)

### Module 6 — Model Persistence, Tracing & Export
1. **State Dictionaries & Checkpointing** (`model.state_dict()`, `torch.save()`, `torch.load()`, resuming training)
2. **TorchScript Tracing & Scripting** (`torch.jit.trace`, `torch.jit.script`, C++ runtime deployment)
3. **ONNX Export & Runtime Execution** (`torch.onnx.export`, verifying ONNX models with ONNX Runtime)
