import os

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum\_11_deep_learning'

LESSONS = [
    # MOD 01 - DL Foundations
    ("_11_01_dl_foundations","_11_01_01_artificial_neuron_and_perceptron.md",1,1,"The Artificial Neuron and Perceptron","DL Foundations",["perceptron","mcculloch-pitts","linear-separability","xor"],"beginner"),
    ("_11_01_dl_foundations","_11_01_02_feedforward_neural_networks_mlp.md",1,2,"Feedforward Neural Networks MLP","DL Foundations",["mlp","hidden-layers","universal-approximation","matrix-formulation"],"beginner"),
    ("_11_01_dl_foundations","_11_01_03_activation_functions.md",1,3,"Activation Functions","DL Foundations",["relu","gelu","sigmoid","tanh","swish","mish","softmax"],"intermediate"),
    ("_11_01_dl_foundations","_11_01_04_loss_functions_deep_learning.md",1,4,"Loss Functions for Deep Learning","DL Foundations",["bce","focal-loss","triplet-loss","nt-xent","label-smoothing"],"intermediate"),
    ("_11_01_dl_foundations","_11_01_05_backpropagation_computational_graphs.md",1,5,"Backpropagation and Computational Graphs","DL Foundations",["backprop","chain-rule","autograd","gradient-tape","vanishing-gradient"],"intermediate"),
    ("_11_01_dl_foundations","_11_01_06_weight_initialization.md",1,6,"Weight Initialization","DL Foundations",["xavier","kaiming","he","lecun","orthogonal","symmetry-breaking"],"intermediate"),
    ("_11_01_dl_foundations","_11_01_07_regularization_techniques.md",1,7,"Regularization Techniques","DL Foundations",["dropout","weight-decay","batch-norm","layer-norm","early-stopping","label-smoothing"],"intermediate"),
    ("_11_01_dl_foundations","_11_01_08_neural_network_capacity_generalization.md",1,8,"Neural Network Capacity and Generalization","DL Foundations",["vc-dimension","double-descent","memorization","pac-learning"],"advanced"),
    # MOD 02 - PyTorch
    ("_11_02_pytorch_framework","_11_02_01_pytorch_tensors_autograd.md",2,1,"PyTorch Tensors and Autograd","PyTorch Framework",["torch-tensor","autograd","requires-grad","backward","no-grad"],"intermediate"),
    ("_11_02_pytorch_framework","_11_02_02_building_models_nn_module.md",2,2,"Building Models with nn.Module","PyTorch Framework",["nn-module","forward","sequential","module-list","torchinfo"],"intermediate"),
    ("_11_02_pytorch_framework","_11_02_03_pytorch_optimizers.md",2,3,"PyTorch Optimizers","PyTorch Framework",["sgd","adam","adamw","rmsprop","gradient-clipping"],"intermediate"),
    ("_11_02_pytorch_framework","_11_02_04_learning_rate_scheduling.md",2,4,"Learning Rate Scheduling","PyTorch Framework",["step-lr","cosine-annealing","one-cycle","reduce-on-plateau","lr-finder"],"intermediate"),
    ("_11_02_pytorch_framework","_11_02_05_pytorch_data_pipeline.md",2,5,"PyTorch Data Pipeline","PyTorch Framework",["dataset","dataloader","transforms","weighted-random-sampler","torchvision"],"intermediate"),
    ("_11_02_pytorch_framework","_11_02_06_training_loop_architecture.md",2,6,"Training Loop Architecture","PyTorch Framework",["training-loop","mixed-precision","gradient-accumulation","checkpointing","tqdm"],"intermediate"),
    ("_11_02_pytorch_framework","_11_02_07_debugging_profiling_pytorch.md",2,7,"Debugging and Profiling PyTorch","PyTorch Framework",["torch-profiler","anomaly-detection","tensorboard","torchviz","memory-management"],"advanced"),
    ("_11_02_pytorch_framework","_11_02_08_distributed_training_pytorch.md",2,8,"Distributed Training with PyTorch","PyTorch Framework",["ddp","torchrun","fsdp","deepspeed","nccl","allreduce"],"advanced"),
    ("_11_02_pytorch_framework","_11_02_09_torchscript_model_export.md",2,9,"TorchScript and Model Export","PyTorch Framework",["torchscript","torch-compile","onnx","onnx-runtime","torch-export"],"advanced"),
    # MOD 03 - TensorFlow
    ("_11_03_tensorflow_keras","_11_03_01_tensorflow_2x_architecture.md",3,1,"TensorFlow 2.x Architecture","TensorFlow and Keras",["tensorflow","eager-execution","tf-function","gradient-tape","xla"],"intermediate"),
    ("_11_03_tensorflow_keras","_11_03_02_keras_sequential_functional_api.md",3,2,"Keras Sequential and Functional API","TensorFlow and Keras",["sequential","functional-api","model-subclassing","custom-layers"],"intermediate"),
    ("_11_03_tensorflow_keras","_11_03_03_keras_training_callbacks.md",3,3,"Keras Training and Callbacks","TensorFlow and Keras",["model-fit","callbacks","early-stopping","model-checkpoint","reduce-lr"],"intermediate"),
    ("_11_03_tensorflow_keras","_11_03_04_tf_data_pipeline.md",3,4,"tf.data Pipeline","TensorFlow and Keras",["tf-data","autotune","tfrecord","prefetch","cache","map-filter"],"intermediate"),
    ("_11_03_tensorflow_keras","_11_03_05_keras_tuner_autokeras.md",3,5,"Keras Tuner and AutoKeras","TensorFlow and Keras",["keras-tuner","hyperband","bayesian-optimization","autokeras"],"intermediate"),
    ("_11_03_tensorflow_keras","_11_03_06_tensorflow_savedmodel_serving.md",3,6,"TensorFlow SavedModel and Serving","TensorFlow and Keras",["savedmodel","tflite","tf-serving","grpc","quantization"],"intermediate"),
    ("_11_03_tensorflow_keras","_11_03_07_tensorboard_experiment_tracking.md",3,7,"TensorBoard and Experiment Tracking","TensorFlow and Keras",["tensorboard","tf-summary","hparams","wandb","mlflow-tensorflow"],"intermediate"),
    # MOD 04 - Training Optimization
    ("_11_04_training_optimization","_11_04_01_advanced_optimizers.md",4,1,"Advanced Optimizers","Training Optimization",["adamw","lamb","lion","shampoo","muon","nadam","radam"],"advanced"),
    ("_11_04_training_optimization","_11_04_02_learning_rate_techniques.md",4,2,"Learning Rate Techniques","Training Optimization",["warmup","one-cycle","cosine-restarts","layer-wise-lr","differential-lr"],"intermediate"),
    ("_11_04_training_optimization","_11_04_03_batch_size_gradient_accumulation.md",4,3,"Batch Size and Gradient Accumulation","Training Optimization",["batch-size","gradient-accumulation","linear-scaling","ghost-batch-norm"],"intermediate"),
    ("_11_04_training_optimization","_11_04_04_mixed_precision_training.md",4,4,"Mixed Precision Training","Training Optimization",["fp16","bf16","grad-scaler","autocast","tensor-cores","gradient-checkpointing"],"intermediate"),
    ("_11_04_training_optimization","_11_04_05_gradient_clipping_stability.md",4,5,"Gradient Clipping and Stability","Training Optimization",["clip-grad-norm","exploding-gradient","vanishing-gradient","residual-connections"],"intermediate"),
    ("_11_04_training_optimization","_11_04_06_normalization_layers_deep_dive.md",4,6,"Normalization Layers Deep Dive","Training Optimization",["batch-norm","layer-norm","group-norm","rms-norm","spectral-norm","instance-norm"],"intermediate"),
    ("_11_04_training_optimization","_11_04_07_data_augmentation_deep_learning.md",4,7,"Data Augmentation for Deep Learning","Training Optimization",["mixup","cutmix","augmix","randaugment","albumentations","tta"],"intermediate"),
    ("_11_04_training_optimization","_11_04_08_curriculum_learning_strategies.md",4,8,"Curriculum Learning and Training Strategies","Training Optimization",["curriculum-learning","progressive-resizing","stochastic-depth","r-drop","distillation"],"advanced"),
    # MOD 05 - CNN
    ("_11_05_convolutional_neural_networks","_11_05_01_convolution_operation_and_filters.md",5,1,"Convolution Operation and Filters","CNNs",["conv2d","kernel","stride","padding","dilated-conv","depthwise","transposed-conv"],"intermediate"),
    ("_11_05_convolutional_neural_networks","_11_05_02_pooling_and_spatial_reduction.md",5,2,"Pooling and Spatial Reduction","CNNs",["max-pooling","avg-pooling","global-average-pooling","strided-conv","spp"],"intermediate"),
    ("_11_05_convolutional_neural_networks","_11_05_03_classic_cnn_architectures.md",5,3,"Classic CNN Architectures","CNNs",["lenet","alexnet","vgg","googlenet","inception","torchvision-models"],"intermediate"),
    ("_11_05_convolutional_neural_networks","_11_05_04_resnet_skip_connections.md",5,4,"ResNet and Skip Connections","CNNs",["resnet","residual-block","bottleneck","resnext","wide-resnet","se-net"],"intermediate"),
    ("_11_05_convolutional_neural_networks","_11_05_05_efficient_cnn_architectures.md",5,5,"Efficient CNN Architectures","CNNs",["mobilenet","efficientnet","convnext","shufflenet","compound-scaling","depthwise"],"intermediate"),
    ("_11_05_convolutional_neural_networks","_11_05_06_image_classification_pipeline.md",5,6,"Image Classification Pipeline","CNNs",["imagefolder","fine-tuning","grad-cam","tta","top-1","top-5"],"intermediate"),
    ("_11_05_convolutional_neural_networks","_11_05_07_object_detection_yolo.md",5,7,"Object Detection YOLO","CNNs",["yolov8","ultralytics","iou","nms","map","anchor-boxes","data-yaml"],"intermediate"),
    ("_11_05_convolutional_neural_networks","_11_05_08_object_detection_faster_rcnn_ssd.md",5,8,"Object Detection Faster RCNN SSD","CNNs",["faster-rcnn","rpn","roi-align","fpn","retinanet","focal-loss","ssd"],"intermediate"),
    ("_11_05_convolutional_neural_networks","_11_05_09_image_segmentation.md",5,9,"Image Segmentation","CNNs",["semantic-seg","unet","deeplabv3","panoptic","mask-rcnn","sam"],"intermediate"),
    ("_11_05_convolutional_neural_networks","_11_05_10_pose_estimation_face_recognition.md",5,10,"Pose Estimation and Face Recognition","CNNs",["hrnet","openpose","mtcnn","facenet","arcface","siamese"],"advanced"),
    ("_11_05_convolutional_neural_networks","_11_05_11_video_understanding.md",5,11,"Video Understanding","CNNs",["3d-cnn","i3d","slowfast","video-swin","optical-flow","action-detection"],"advanced"),
    # MOD 06 - RNN
    ("_11_06_recurrent_neural_networks","_11_06_01_vanilla_rnn_architecture.md",6,1,"Vanilla RNN Architecture","RNNs",["rnn","bptt","vanishing-gradient","sequence-modelling","nn-rnn"],"intermediate"),
    ("_11_06_recurrent_neural_networks","_11_06_02_lstm_architecture.md",6,2,"LSTM Architecture","RNNs",["lstm","forget-gate","cell-state","bidirectional","packed-sequences","stacked-lstm"],"intermediate"),
    ("_11_06_recurrent_neural_networks","_11_06_03_gru_architecture.md",6,3,"GRU Architecture","RNNs",["gru","reset-gate","update-gate","nn-gru","gru-vs-lstm"],"intermediate"),
    ("_11_06_recurrent_neural_networks","_11_06_04_sequence_to_sequence_models.md",6,4,"Sequence to Sequence Models","RNNs",["seq2seq","encoder-decoder","teacher-forcing","beam-search","greedy-decoding"],"intermediate"),
    ("_11_06_recurrent_neural_networks","_11_06_05_attention_mechanism_rnn.md",6,5,"Attention Mechanism RNN","RNNs",["bahdanau","luong","context-vector","alignment-score","copy-mechanism"],"intermediate"),
    ("_11_06_recurrent_neural_networks","_11_06_06_rnns_for_time_series.md",6,6,"RNNs for Time Series","RNNs",["univariate-forecasting","multivariate","sliding-window","deepar","lstm-forecasting"],"intermediate"),
    ("_11_06_recurrent_neural_networks","_11_06_07_temporal_convolutional_networks.md",6,7,"Temporal Convolutional Networks","RNNs",["tcn","causal-conv","dilated-causal","wavenet","tcn-vs-lstm"],"intermediate"),
    ("_11_06_recurrent_neural_networks","_11_06_08_anomaly_detection_rnns.md",6,8,"Anomaly Detection with RNNs","RNNs",["lstm-autoencoder","reconstruction-error","deepant","mscred","spot","streaming"],"advanced"),
    # MOD 07 - Transformers
    ("_11_07_attention_and_transformers","_11_07_01_scaled_dot_product_attention.md",7,1,"Scaled Dot-Product Attention","Attention and Transformers",["qkv","attention-scores","scaling","causal-mask","flash-attention"],"intermediate"),
    ("_11_07_attention_and_transformers","_11_07_02_multi_head_attention.md",7,2,"Multi-Head Attention","Attention and Transformers",["multi-head","projection","concat","nn-multihead-attention","head-analysis"],"intermediate"),
    ("_11_07_attention_and_transformers","_11_07_03_positional_encoding.md",7,3,"Positional Encoding","Attention and Transformers",["sinusoidal","learned-pe","rope","alibi","relative-pe","rotary"],"intermediate"),
    ("_11_07_attention_and_transformers","_11_07_04_transformer_encoder_architecture.md",7,4,"Transformer Encoder Architecture","Attention and Transformers",["encoder-block","ffn","add-norm","pre-ln","post-ln","nn-transformer-encoder"],"intermediate"),
    ("_11_07_attention_and_transformers","_11_07_05_transformer_decoder_architecture.md",7,5,"Transformer Decoder Architecture","Attention and Transformers",["decoder-block","causal-mask","cross-attention","autoregressive","nn-transformer-decoder"],"intermediate"),
    ("_11_07_attention_and_transformers","_11_07_06_vision_transformer_vit.md",7,6,"Vision Transformer ViT","Attention and Transformers",["vit","patch-embedding","cls-token","timm","positional-embedding","vit-vs-cnn"],"intermediate"),
    ("_11_07_attention_and_transformers","_11_07_07_hierarchical_vision_transformers.md",7,7,"Hierarchical Vision Transformers","Attention and Transformers",["swin","window-attention","shifted-windows","deit","beit","mvit"],"advanced"),
    ("_11_07_attention_and_transformers","_11_07_08_efficient_attention_mechanisms.md",7,8,"Efficient Attention Mechanisms","Attention and Transformers",["linear-attention","longformer","bigbird","flash-attention-2","mqa","gqa"],"advanced"),
    ("_11_07_attention_and_transformers","_11_07_09_detr_detection_transformers.md",7,9,"DETR and Detection Transformers","Attention and Transformers",["detr","object-queries","hungarian-matching","deformable-detr","dino-detr"],"advanced"),
    # MOD 08 - Generative
    ("_11_08_generative_models","_11_08_01_autoencoders.md",8,1,"Autoencoders","Generative Models",["autoencoder","bottleneck","denoising-ae","sparse-ae","contractive-ae"],"intermediate"),
    ("_11_08_generative_models","_11_08_02_variational_autoencoders_vae.md",8,2,"Variational Autoencoders VAE","Generative Models",["vae","elbo","reparameterization","kl-divergence","beta-vae","vq-vae"],"intermediate"),
    ("_11_08_generative_models","_11_08_03_gan_foundations.md",8,3,"GAN Foundations","Generative Models",["gan","minimax","generator","discriminator","dcgan","mode-collapse","wgan"],"intermediate"),
    ("_11_08_generative_models","_11_08_04_advanced_gans.md",8,4,"Advanced GANs","Generative Models",["wgan-gp","stylegan","cyclegan","pix2pix","progan","conditional-gan","infogan"],"advanced"),
    ("_11_08_generative_models","_11_08_05_score_based_flow_models.md",8,5,"Score-Based and Flow Models","Generative Models",["normalizing-flows","realnvp","glow","score-matching","ncsn","flow-matching"],"advanced"),
    ("_11_08_generative_models","_11_08_06_diffusion_models.md",8,6,"Diffusion Models","Generative Models",["ddpm","ddim","noise-schedule","unet-denoiser","latent-diffusion","stable-diffusion","cfg"],"intermediate"),
    ("_11_08_generative_models","_11_08_07_text_to_image_systems.md",8,7,"Text to Image Systems","Generative Models",["stable-diffusion","dall-e","imagen","diffusers","dreambooth","lora","sdxl","flux"],"intermediate"),
    ("_11_08_generative_models","_11_08_08_evaluation_generative_models.md",8,8,"Evaluation of Generative Models","Generative Models",["fid","inception-score","clip-score","lpips","precision-recall","torch-fidelity"],"intermediate"),
    ("_11_08_generative_models","_11_08_09_generative_models_tabular_audio.md",8,9,"Generative Models for Tabular and Audio","Generative Models",["ctgan","tvae","sdv","wavenet","wavegan","melgan"],"advanced"),
    # MOD 09 - SSL
    ("_11_09_self_supervised_learning","_11_09_01_self_supervised_learning_foundations.md",9,1,"Self-Supervised Learning Foundations","Self-Supervised Learning",["pretext-tasks","contrastive","generative-ssl","data2vec","label-efficiency"],"intermediate"),
    ("_11_09_self_supervised_learning","_11_09_02_contrastive_learning.md",9,2,"Contrastive Learning","Self-Supervised Learning",["simclr","moco","byol","simsiam","nt-xent","lightly"],"intermediate"),
    ("_11_09_self_supervised_learning","_11_09_03_masked_autoencoders_mae.md",9,3,"Masked Autoencoders MAE","Self-Supervised Learning",["mae","masking","asymmetric","video-mae","audio-mae","linear-probing"],"intermediate"),
    ("_11_09_self_supervised_learning","_11_09_04_dino_self_distillation.md",9,4,"DINO and Self-Distillation","Self-Supervised Learning",["dino","dinov2","self-distillation","ema-teacher","centering","multi-crop"],"intermediate"),
    ("_11_09_self_supervised_learning","_11_09_05_clustering_based_ssl.md",9,5,"Clustering-Based SSL","Self-Supervised Learning",["deepcluster","swav","pcl","scan","sinkhorn-knopp"],"advanced"),
    ("_11_09_self_supervised_learning","_11_09_06_multimodal_ssl.md",9,6,"Multi-Modal Self-Supervised Learning","Self-Supervised Learning",["clip","open-clip","zero-shot","align","flava","imagebind"],"intermediate"),
    # MOD 10 - Transfer
    ("_11_10_transfer_learning_and_finetuning","_11_10_01_transfer_learning_fundamentals.md",10,1,"Transfer Learning Fundamentals","Transfer Learning and Fine-Tuning",["domain-adaptation","feature-extraction","fine-tuning","discriminative-lr","timm"],"intermediate"),
    ("_11_10_transfer_learning_and_finetuning","_11_10_02_finetuning_imagenet_pretrained_cnns.md",10,2,"Fine-Tuning ImageNet Pretrained CNNs","Transfer Learning and Fine-Tuning",["progressive-unfreeze","layer-wise-lr","randaugment","mixup","medical-imaging"],"intermediate"),
    ("_11_10_transfer_learning_and_finetuning","_11_10_03_few_shot_learning.md",10,3,"Few-Shot Learning","Transfer Learning and Fine-Tuning",["n-way-k-shot","siamese","prototypical-networks","maml","reptile","learn2learn"],"advanced"),
    ("_11_10_transfer_learning_and_finetuning","_11_10_04_domain_adaptation.md",10,4,"Domain Adaptation","Transfer Learning and Fine-Tuning",["dann","mmd","coral","covariate-shift","source-free-da","test-time-adaptation"],"advanced"),
    ("_11_10_transfer_learning_and_finetuning","_11_10_05_knowledge_distillation.md",10,5,"Knowledge Distillation","Transfer Learning and Fine-Tuning",["soft-targets","temperature","feature-distillation","distilbert","born-again-networks"],"intermediate"),
    ("_11_10_transfer_learning_and_finetuning","_11_10_06_peft_for_vision.md",10,6,"PEFT for Vision","Transfer Learning and Fine-Tuning",["lora","adapter","prompt-tuning","vpt","bitfit","peft-library"],"advanced"),
    ("_11_10_transfer_learning_and_finetuning","_11_10_07_multi_task_learning.md",10,7,"Multi-Task Learning","Transfer Learning and Fine-Tuning",["hard-sharing","soft-sharing","gradnorm","uncertainty-weighting","gradient-surgery"],"advanced"),
    # MOD 11 - Compression
    ("_11_11_model_compression_and_deployment","_11_11_01_quantization.md",11,1,"Quantization","Model Compression and Deployment",["int8","post-training-quant","quantization-aware-training","gptq","awq","bitsandbytes"],"advanced"),
    ("_11_11_model_compression_and_deployment","_11_11_02_pruning.md",11,2,"Pruning","Model Compression and Deployment",["unstructured-pruning","structured-pruning","magnitude-pruning","lottery-ticket","movement-pruning"],"advanced"),
    ("_11_11_model_compression_and_deployment","_11_11_03_model_distillation_applied.md",11,3,"Model Distillation Applied","Model Compression and Deployment",["kl-div-loss","teacher-student","temperature","online-distillation","dml"],"intermediate"),
    ("_11_11_model_compression_and_deployment","_11_11_04_onnx_tensorrt_deployment.md",11,4,"ONNX and TensorRT Deployment","Model Compression and Deployment",["onnx","onnx-runtime","tensorrt","trtexec","triton","torch2trt"],"advanced"),
    ("_11_11_model_compression_and_deployment","_11_11_05_tensorflow_lite_edge_deployment.md",11,5,"TensorFlow Lite Edge Deployment","Model Compression and Deployment",["tflite","edge-tpu","coral","tflm","esp32","raspberry-pi","delegate"],"advanced"),
    ("_11_11_model_compression_and_deployment","_11_11_06_serving_triton_fastapi.md",11,6,"Serving with Triton and FastAPI","Model Compression and Deployment",["triton","grpc","dynamic-batching","model-ensemble","fastapi","async-inference"],"advanced"),
    ("_11_11_model_compression_and_deployment","_11_11_07_benchmarking_profiling.md",11,7,"Benchmarking and Profiling","Model Compression and Deployment",["torch-profiler","fvcore","torchmetrics","latency","memory-profiling","mlperf"],"advanced"),
    # MOD 12 - Projects
    ("_11_12_industry_projects","_11_12_01_image_classification_system_production.md",12,1,"Image Classification System Production","Industry Projects",["efficientnetv2","amp","randaugment","onnx","docker","evidently"],"advanced"),
    ("_11_12_industry_projects","_11_12_02_object_detection_system.md",12,2,"Object Detection System","Industry Projects",["yolov8","faster-rcnn","roboflow","tensorrt","triton","map"],"advanced"),
    ("_11_12_industry_projects","_11_12_03_medical_image_segmentation.md",12,3,"Medical Image Segmentation","Industry Projects",["unet","swin-unetr","dice-loss","monai","btcv","hausdorff"],"advanced"),
    ("_11_12_industry_projects","_11_12_04_generative_image_pipeline.md",12,4,"Generative Image Pipeline","Industry Projects",["dreambooth","lora-diffusion","stable-diffusion","fid","clip-score","e-commerce"],"advanced"),
    ("_11_12_industry_projects","_11_12_05_time_series_forecasting_deep_learning.md",12,5,"Time Series Forecasting Deep Learning","Industry Projects",["nbeats","patchtst","timesnet","neuralforecast","smape","mase","crps"],"advanced"),
    ("_11_12_industry_projects","_11_12_06_anomaly_detection_industrial_iot.md",12,6,"Anomaly Detection Industrial IoT","Industry Projects",["lstm-ae","tranad","usad","smap","msl","mqtt","jetson","onnx-edge"],"advanced"),
]

created = 0
skipped = 0
for folder, fname, mod, les, title, mod_title, tags, diff in LESSONS:
    dirpath = os.path.join(BASE, folder)
    os.makedirs(dirpath, exist_ok=True)
    fpath = os.path.join(dirpath, fname)
    if not os.path.exists(fpath):
        lid = f"11_{mod:02d}_{les:02d}"
        tag_str = ", ".join('"' + t + '"' for t in tags)
        content = f'---\nid: "{lid}"\ntitle: "{title}"\ncourse: "Deep Learning"\nmodule: {mod}\nmodule_title: "{mod_title}"\nlesson: {les}\nversion: "2.0"\ndifficulty: "{diff}"\nduration_minutes: 60\ntags: [{tag_str}]\nprerequisites: []\nlab_required: true\n---\n\n# {title}\n\n> **Status**: Syllabus stub. Full lesson content to be authored.\n\n---\n\n## Topics Covered\n\n*(See Phase 2 DL Syllabus for full topic and subtopic breakdown)*\n\n---\n\n## Learning Objectives\n\n- To be defined during content authoring.\n'
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[CREATE] {fname}")
        created += 1
    else:
        print(f"[SKIP]   {fname}")
        skipped += 1

print(f"\nDONE - Created: {created}  Skipped: {skipped}  Total: {created+skipped}")
