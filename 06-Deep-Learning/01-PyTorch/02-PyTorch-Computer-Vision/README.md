# 👁️ PyTorch Computer Vision

This folder documents my progression into **computer vision with PyTorch**, starting with a fully connected baseline for image classification and moving toward custom CNN architectures and transfer learning with pretrained models. 

The focus is on understanding **why different architectures behave differently on image data**, while experimenting with preprocessing, augmentation, model design, GPU usage, training workflows, transfer learning, and web deployment.

## 🎯 Objectives

- Understand how image data is represented and processed in PyTorch
- Build image-classification pipelines with `torchvision`
- Compare fully connected networks with convolutional neural networks
- Design and train custom CNN architectures
- Experiment with image preprocessing and augmentation
- Analyze parameter growth and GPU memory usage
- Learn transfer learning with pretrained CNNs
- Compare models using accuracy, training time, and parameter counts
- **Deploy trained PyTorch models to an interactive web application using Streamlit**

## 📂 Notebooks & Applications

### 01_food101_mlp_baseline.ipynb

A baseline experiment on the **Food-101** dataset using a multilayer perceptron. 
The images are resized and flattened before being passed to fully connected layers. This experiment helps demonstrate an important limitation of fully connected networks for image data: spatial relationships between neighboring pixels are not represented explicitly. 

*Concepts explored:*
- Image classification
- Image preprocessing
- Flattening image tensors
- Fully connected neural networks
- Training and evaluation
- Limitations of MLPs for image data

### 02_food101_cnn_model.ipynb

Introduces convolutional neural networks for image classification on Food-101. 
The experiment moves from flattened image representations to convolution-based feature extraction, allowing the model to learn spatial patterns directly from images.

*Concepts explored:*
- `Conv2d`
- `MaxPool2d`
- Feature maps
- CNN architecture
- Image augmentation
- Training and evaluation
- GPU training

### 03_intel_image_classification-cnn_sandbox.ipynb

Builds a custom CNN for the **Intel Image Classification** dataset. 
The model uses multiple convolutional blocks followed by a fully connected classifier. 

*Architecture components include:*
- `Conv2d`
- `ReLU`
- `BatchNorm2d`
- `MaxPool2d`
- `Dropout`
- Fully connected layers

The experiment also provided practical experience with **GPU memory usage and model parameter growth**.

### 04_intel_image_classification_transfer_learning_comparison.ipynb

Extends the Intel image-classification experiment by comparing the custom CNN against an **ImageNet-pretrained ResNet18**. 

The current experiment includes:
- Custom CNN trained from scratch
- ResNet18 with a frozen pretrained backbone
- Test accuracy comparison
- Training-time comparison
- Trainable parameter comparison
- Total parameter comparison
- Training-loss and accuracy visualization
- Saving trained model weights with `state_dict()`

### 🌐 streamlit_app

Takes the trained models (Custom CNN and ResNet-18) from the previous experiment and deploys them into a live, interactive web application. 
- 🚀 **Live Demo:** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vikas-landscape-classifier.streamlit.app/)
- Users can upload custom images of natural landscapes and get real-time predictions from both model architectures to compare their performance in the real world.

## Current Results

| **Model** | **Trainable Parameters** | **Total Parameters** | **Training Time** | **Test Accuracy** |
| :--- | :--- | :--- | :--- | :--- |
| Custom CNN | 11.33M | 11.33M | 18.13 min | 79.70% |
| ResNet18 — Frozen Backbone | 0.165M | 11.34M | 8.93 min | 90.30% |

Results are from the current experiment and may vary slightly depending on hardware, runtime, and training conditions.

## Observation

In this experiment, the pretrained ResNet18 achieved higher test accuracy than the custom CNN while updating substantially fewer parameters and requiring less training time. The experiment is being extended to investigate **partial fine-tuning and full fine-tuning**.

## 🧠 Concepts Covered

### Image & Dataset Handling
- `torchvision.datasets.ImageFolder`
- Image preprocessing (resizing, center cropping, normalization)
- Data augmentation
- `DataLoader` (batching and shuffling)

### Neural Network Foundations
- Fully connected networks
- Convolutional layers & Feature maps
- Pooling & Activation functions
- Batch normalization & Dropout
- Loss functions & Optimizers
- Training loops & GPU acceleration

### CNNs
- Custom CNN architecture design
- Convolutional feature extraction
- Spatial downsampling
- Parameter growth & GPU/VRAM considerations

### Transfer Learning
- Pretrained ImageNet models (ResNet18)
- Frozen feature extractors
- Replacing classification heads

### MLOps & Deployment
- Streamlit web applications
- Cloud environment dependency management (`requirements.txt`)
- Model caching (`@st.cache_resource`)
- Hosting large `.pth` model weights via GitHub Releases

### Experiment Analysis
- Training loss & accuracy vs Test accuracy
- Training time & parameter tracking
- Model checkpoints & Training visualizations

## 🔬 Learning Progression

The experiments in this folder follow a progression from basic image classification toward pretrained computer-vision models and web deployment:

    Image Classification
            ↓
    Food-101 MLP
            ↓
    Food-101 CNN
            ↓
    Custom CNN Architecture
            ↓
    Intel Image Classification
            ↓
    Transfer Learning
            ↓
    Feature Extraction
            ↓
    Partial Fine-Tuning
            ↓
    Full Fine-Tuning
            ↓
    Live Web Deployment (Streamlit)
