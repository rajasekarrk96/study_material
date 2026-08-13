# Missing Canonical Technologies Analysis (`exports/MISSING_CANONICAL_COURSES.md`)

_Learning OS v2 — Authoritative Missing Technology Justification_

---

## 1. Overview

In accordance with the **"Teach Once. Reuse Everywhere."** core axiom, technologies that are repeatedly referenced across multiple Specializations and Learning Paths must exist as authoritative standalone courses in `technologies/` rather than being partially re-taught across disparate curricula.

This report evaluates each candidate missing technology against three criteria:
1. **Reference Frequency:** Is it required by multiple downstream specializations or learning paths?
2. **Standalone Integrity:** Does it constitute a substantial, self-contained technical discipline?
3. **Absence Verification:** Does it not already exist under another slug in the repository?

---

## 2. Evaluation of Candidate Technologies

### 1. PyTorch (`technologies/pytorch`)
- **Category:** Technology
- **Referencing Courses:** `specializations/deep-learning`, `specializations/computer-vision`, `specializations/nlp`, `specializations/generative-ai-llms`, `specializations/mlops-ai-deployment`, `learning_paths/ai-engineer`, `learning_paths/ml-engineer` (7 references).
- **Justification:** PyTorch is the de facto standard research and production deep learning framework. Currently, courses assume PyTorch knowledge but have no canonical course teaching Tensors, Autograd, `nn.Module`, custom Datasets/DataLoaders, loss functions, GPU acceleration (`torch.cuda`), and `torch.distributed`.
- **Proposed Syllabus Scope (15 Hours):**
  - Module 1: Tensors, Tensor Operations, and Memory Layout
  - Module 2: Automatic Differentiation (`torch.autograd`) and Computational Graphs
  - Module 3: Building Neural Networks with `nn.Module` and `nn.Sequential`
  - Module 4: Data Pipelines (`Dataset`, `DataLoader`, Transforms)
  - Module 5: Training Loops, Optimizers (`torch.optim`), and Schedulers
  - Module 6: Model Persistence (`torch.save`, `torch.load`, TorchScript, ONNX Export)
  - Module 7: GPU Acceleration, Mixed Precision (`torch.cuda.amp`), and Multi-GPU Basics (`DDP`)

---

### 2. TensorFlow & Keras (`technologies/tensorflow`)
- **Category:** Technology
- **Referencing Courses:** `specializations/deep-learning`, `specializations/tinyml`, `specializations/computer-vision-iot`, `learning_paths/ml-engineer` (4 references).
- **Justification:** Essential for mobile, edge, and embedded AI deployments (TensorFlow Lite, TensorFlow Lite for Microcontrollers).
- **Proposed Syllabus Scope (12 Hours):**
  - Module 1: TensorFlow Core & Tensors
  - Module 2: Keras Sequential and Functional APIs
  - Module 3: `tf.data` ETL Pipelines
  - Module 4: Custom Layers, Models, and Loss Functions
  - Module 5: Callbacks, Checkpointing, and TensorBoard
  - Module 6: SavedModel, TensorFlow Serving, and TF Lite Model Quantization/Export

---

### 3. OpenCV (`technologies/opencv`)
- **Category:** Technology
- **Referencing Courses:** `specializations/computer-vision`, `specializations/computer-vision-iot`, `learning_paths/ai-engineer`, `learning_paths/iot-full-stack` (4 references).
- **Justification:** OpenCV is the foundational image processing library required by every visual intelligence course. Currently, basic image filtering and OpenCV API syntax is duplicated in Computer Vision syllabuses.
- **Proposed Syllabus Scope (15 Hours):**
  - Module 1: OpenCV Architecture, Image Matrix Representation, and Color Spaces (BGR, RGB, HSV, Grayscale)
  - Module 2: Image Geometric Transformations (Resizing, Affine, Perspective, Cropping)
  - Module 3: Image Filtering, Blurring, Thresholding, and Morphological Operations
  - Module 4: Edge Detection (Canny, Sobel) and Contour Analysis
  - Module 5: Drawing Primitives, Text, and Region of Interest (ROI) Manipulation
  - Module 6: Video Streams (`cv2.VideoCapture`), Camera Calibration, and FPS Benchmarking
  - Module 7: Feature Detection (ORB, SIFT) and Template Matching

---

### 4. Vector Databases (`technologies/vector-databases`)
- **Category:** Technology
- **Referencing Courses:** `specializations/rag-engineering`, `specializations/generative-ai-llms`, `specializations/ai-agents`, `learning_paths/ai-engineer` (4 references).
- **Justification:** Vector search engines are fundamental infrastructure for modern LLM applications. A dedicated course ensures RAG courses do not have to teach vector indexing algorithms from scratch.
- **Proposed Syllabus Scope (10 Hours):**
  - Module 1: Vector Embeddings & Vector Space Geometry (Cosine, Dot Product, Euclidean Distance)
  - Module 2: Approximate Nearest Neighbor (ANN) Indexing Algorithms (HNSW, IVF, Flat)
  - Module 3: ChromaDB (Local Embedded Vector DB)
  - Module 4: Pinecone & Qdrant (Cloud Vector Databases)
  - Module 5: Metadata Filtering, Hybrid Search (Dense + Sparse/BM25), and Namespace Partitioning
  - Module 6: Vector Database Benchmarking, Index Tuning, and Scale Strategies

---

### 5. PyTest (`technologies/pytest`)
- **Category:** Technology
- **Referencing Courses:** `technologies/advanced-python`, `technologies/fastapi`, `technologies/flask`, `technologies/selenium`, `learning_paths/python-full-stack`, `learning_paths/qa-automation` (6 references).
- **Justification:** Python testing is repeatedly referenced across web, backend, testing, and automation paths. A canonical PyTest course provides unified testing practices.
- **Proposed Syllabus Scope (8 Hours):**
  - Module 1: PyTest Test Discovery, Assertions, and CLI Options
  - Module 2: PyTest Fixtures (Setup/Teardown, Scopes, `autouse`, Fixture Factories)
  - Module 3: Parametrization (`@pytest.mark.parametrize`)
  - Module 4: Mocking & Monkeypatching (`unittest.mock`, `pytest-mock`)
  - Module 5: Custom Markers, Configuration (`pytest.ini`, `pyproject.toml`), and Plugins
  - Module 6: Coverage Analysis (`pytest-cov`) and CI Integration

---

### 6. Django (`technologies/django`)
- **Category:** Technology
- **Referencing Courses:** `learning_paths/python-full-stack`, Backend Engineering Paths.
- **Justification:** Major high-demand Python enterprise web framework. Completes the Python web framework trio (`flask`, `fastapi`, `django`).
- **Proposed Syllabus Scope (20 Hours):**
  - Module 1: Django MTV Architecture & Project Configuration
  - Module 2: Django ORM Models, Migrations, and QuerySets
  - Module 3: Views, URL Routing, and Templates
  - Module 4: Django Forms and CSRF Protection
  - Module 5: Django Admin Customization
  - Module 6: Django REST Framework (DRF) Serializers and ViewSets
  - Module 7: Authentication, Permissions, and Production Deployment

---

## 3. Implementation Recommendation

Upon user approval of the migration plan, create empty canonical course directory scaffolds (`README.md`, `COURSE_METADATA.md`, `SYLLABUS/<slug>.md`, `CURRICULUM/`) for these 6 technologies in `exports/technologies/`.
