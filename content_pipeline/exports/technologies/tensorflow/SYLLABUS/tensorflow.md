# TensorFlow & Keras — Master Syllabus

**Target Role:** ML Engineer / Edge AI Developer / Deep Learning Practitioner  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 15 Hours  
**Prerequisites:** foundations/core-python, foundations/ds-math  
**Required Courses:** foundations/core-python, foundations/ds-math  
**Optional Courses:** technologies/docker  

---

## Study Flow

### Module 1 — TensorFlow Core Architecture & Tensors
1. **TensorFlow 2.x Architecture** (Tensors, constants, variables, operations, eager execution vs graph mode with `@tf.function`)
2. **Gradient Tape & Custom Training Steps** (`tf.GradientTape`, automatic differentiation, watching non-trainable tensors)
3. **TensorFlow Mathematical Operations** (`tf.matmul`, `tf.einsum`, tensor slicing, reduction ops)

### Module 2 — Keras Sequential & Functional APIs
1. **Keras Model Construction** (Sequential API vs Functional API for multi-input/multi-output architectures)
2. **Keras Built-in & Custom Layers** (Dense, Conv2D, Dropout, LayerNorm, subclassing `tf.keras.layers.Layer`)
3. **Model Compilation & Training** (`compile()`, `fit()`, `evaluate()`, loss functions, metrics)

### Module 3 — High-Performance Data Pipelines with `tf.data`
1. **Building `tf.data.Dataset` Pipelines** (From numpy arrays, generators, CSV, TFRecord files)
2. **Dataset Transformations & Optimization** (`map()`, `batch()`, `prefetch()`, `interleave()`, `AUTOTUNE`)
3. **Keras Image Preprocessing Layers** (`Rescaling`, `RandomFlip`, `RandomRotation`)

### Module 4 — Callbacks, Checkpointing & TensorBoard
1. **Keras Built-in Callbacks** (`EarlyStopping`, `ModelCheckpoint`, `ReduceLROnPlateau`, `CSVLogger`)
2. **Writing Custom Keras Callbacks** (Overriding `on_epoch_end`, `on_train_batch_begin`)
3. **TensorBoard Integration** (Scalar graphs, weight histograms, confusion matrices)

### Module 5 — Model Export, Serving & TensorFlow Lite
1. **SavedModel Format** (Exporting model architecture, weights, and signature definitions)
2. **TensorFlow Serving** (Deploying models via Docker with gRPC/REST endpoints)
3. **TensorFlow Lite (TFLite) Quantization & Export** (TFLite Converter, dynamic range quantization, full integer INT8 quantization for edge devices)
