@echo off
:: Root folder name
set ROOT_FOLDER=DeepLearningTopics

:: Create root folder
mkdir %ROOT_FOLDER%
cd %ROOT_FOLDER%

:: I. Fundamentals
mkdir "I. Fundamentals\Basic Concepts\Neural Networks"
mkdir "I. Fundamentals\Basic Concepts\Activation Functions"
mkdir "I. Fundamentals\Basic Concepts\Loss Functions"
mkdir "I. Fundamentals\Basic Concepts\Optimization Algorithms"
mkdir "I. Fundamentals\Basic Concepts\Backpropagation"

mkdir "I. Fundamentals\Architectures\Feedforward Neural Networks"
mkdir "I. Fundamentals\Architectures\Multilayer Perceptrons"

:: II. Supervised Learning
mkdir "II. Supervised Learning\Classification\Image Classification"
mkdir "II. Supervised Learning\Classification\Text Classification"
mkdir "II. Supervised Learning\Classification\Binary vs Multi-Class"

mkdir "II. Supervised Learning\Regression\Time Series Prediction"
mkdir "II. Supervised Learning\Regression\Stock Price Prediction"
mkdir "II. Supervised Learning\Regression\House Price Prediction"

:: III. Unsupervised Learning
mkdir "III. Unsupervised Learning\Clustering\Autoencoders"
mkdir "III. Unsupervised Learning\Clustering\Variational Autoencoders (VAEs)"

mkdir "III. Unsupervised Learning\Dimensionality Reduction\PCA"
mkdir "III. Unsupervised Learning\Dimensionality Reduction\t-SNE"
mkdir "III. Unsupervised Learning\Dimensionality Reduction\UMAP"

:: IV. Advanced Architectures
mkdir "IV. Advanced Architectures\Convolutional Neural Networks (CNNs)\Object Detection"
mkdir "IV. Advanced Architectures\Convolutional Neural Networks (CNNs)\Image Segmentation"
mkdir "IV. Advanced Architectures\Convolutional Neural Networks (CNNs)\Image Generation"

mkdir "IV. Advanced Architectures\Recurrent Neural Networks (RNNs)\LSTM"
mkdir "IV. Advanced Architectures\Recurrent Neural Networks (RNNs)\GRU"
mkdir "IV. Advanced Architectures\Recurrent Neural Networks (RNNs)\Sequence Prediction"

mkdir "IV. Advanced Architectures\Transformer Models\BERT"
mkdir "IV. Advanced Architectures\Transformer Models\GPT"
mkdir "IV. Advanced Architectures\Transformer Models\Vision Transformers (ViT)"

mkdir "IV. Advanced Architectures\Graph Neural Networks (GNNs)\Node Classification"
mkdir "IV. Advanced Architectures\Graph Neural Networks (GNNs)\Graph Embedding"
mkdir "IV. Advanced Architectures\Graph Neural Networks (GNNs)\Link Prediction"

:: V. Generative Models
mkdir "V. Generative Models\Generative Adversarial Networks (GANs)\Image-to-Image Translation"
mkdir "V. Generative Models\Generative Adversarial Networks (GANs)\Deepfake Generation"
mkdir "V. Generative Models\Generative Adversarial Networks (GANs)\Style Transfer"

mkdir "V. Generative Models\Variational Autoencoders (VAEs)\Latent Space Representation"
mkdir "V. Generative Models\Variational Autoencoders (VAEs)\Data Generation"

:: VI. Reinforcement Learning
mkdir "VI. Reinforcement Learning\Value-Based Methods\Deep Q-Learning"
mkdir "VI. Reinforcement Learning\Value-Based Methods\Double DQN"

mkdir "VI. Reinforcement Learning\Policy-Based Methods\REINFORCE Algorithm"
mkdir "VI. Reinforcement Learning\Policy-Based Methods\Actor-Critic Models"

mkdir "VI. Reinforcement Learning\Applications\Game AI"
mkdir "VI. Reinforcement Learning\Applications\Robotics"

:: VII. Specialized Topics
mkdir "VII. Specialized Topics\Natural Language Processing (NLP)\Sentiment Analysis"
mkdir "VII. Specialized Topics\Natural Language Processing (NLP)\Machine Translation"
mkdir "VII. Specialized Topics\Natural Language Processing (NLP)\Question Answering"

mkdir "VII. Specialized Topics\Computer Vision\Face Recognition"
mkdir "VII. Specialized Topics\Computer Vision\Video Analysis"
mkdir "VII. Specialized Topics\Computer Vision\Medical Imaging"

mkdir "VII. Specialized Topics\Speech and Audio\Speech Recognition"
mkdir "VII. Specialized Topics\Speech and Audio\Music Generation"
mkdir "VII. Specialized Topics\Speech and Audio\Audio Classification"

mkdir "VII. Specialized Topics\Time-Series Analysis\Weather Forecasting"
mkdir "VII. Specialized Topics\Time-Series Analysis\Anomaly Detection in IoT"

mkdir "VII. Specialized Topics\Anomaly Detection\Fraud Detection"
mkdir "VII. Specialized Topics\Anomaly Detection\Fault Detection in Machines"

:: VIII. Tools and Techniques
mkdir "VIII. Tools and Techniques\Frameworks\TensorFlow"
mkdir "VIII. Tools and Techniques\Frameworks\PyTorch"
mkdir "VIII. Tools and Techniques\Frameworks\Keras"

mkdir "VIII. Tools and Techniques\Model Compression\Pruning"
mkdir "VIII. Tools and Techniques\Model Compression\Quantization"

mkdir "VIII. Tools and Techniques\Explainable AI\SHAP"
mkdir "VIII. Tools and Techniques\Explainable AI\LIME"

mkdir "VIII. Tools and Techniques\Hyperparameter Tuning\Grid Search"
mkdir "VIII. Tools and Techniques\Hyperparameter Tuning\Bayesian Optimization"

:: IX. Applications
mkdir "IX. Applications\Healthcare\Disease Prediction"
mkdir "IX. Applications\Healthcare\Drug Discovery"

mkdir "IX. Applications\Finance\Credit Scoring"
mkdir "IX. Applications\Finance\Portfolio Management"

mkdir "IX. Applications\Autonomous Systems\Self-Driving Cars"
mkdir "IX. Applications\Autonomous Systems\Drones"

mkdir "IX. Applications\IoT\Smart Home Automation"
mkdir "IX. Applications\IoT\Predictive Maintenance"

:: Finish
echo All folders and subfolders created successfully!
pause
