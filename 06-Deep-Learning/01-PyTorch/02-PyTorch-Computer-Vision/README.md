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
- Learn transfer learning with pretrained CNNs (ResNet, EfficientNet)
- Tackle fine-grained classification problems (100+ classes)
- Compare models using accuracy, training time, and parameter counts
- **Deploy trained PyTorch models to an interactive web application using Streamlit**

## 📂 Notebooks & Applications

### 01_food101_mlp_baseline.ipynb
A baseline experiment on the **Food-101** dataset using a multilayer perceptron. 
The images are resized and flattened before being passed to fully connected layers. This experiment helps demonstrate an important limitation of fully connected networks for image data: spatial relationships between neighboring pixels are not represented explicitly. 

### 02_food101_cnn_model.ipynb
Introduces convolutional neural networks for image classification on Food-101. 
The experiment moves from flattened image representations to convolution-based feature extraction, allowing the model to learn spatial patterns directly from images.

### 03_intel_image_classification-cnn_sandbox.ipynb
Builds a custom CNN for the **Intel Image Classification** dataset. 
The model uses multiple convolutional blocks followed by a fully connected classifier, providing practical experience with **GPU memory usage and model parameter growth**.

### 04_intel_image_classification_transfer_learning_comparison.ipynb
Extends the Intel image-classification experiment by comparing the custom CNN against an **ImageNet-pretrained ResNet18**. Explores feature extraction by freezing the backbone and only training a custom classification head.

### 05_food101_transfer_learning_EfficientNetB3.ipynb
Tackles a massive **fine-grained classification** problem (101 distinct food classes) using a pretrained **EfficientNet-B3**. 
This experiment pushed the limits of free GPU hardware, requiring strategic partial fine-tuning (unfreezing specific `MBConv` blocks), custom classifier design, heavy data augmentation for regularization, and exporting class dictionaries (`.json`) for future web deployment.

### 🌐 streamlit_app
Takes the trained models from the previous experiments and deploys them into a live, interactive web application. 
- 🚀 **Live Demo:** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vikas-landscape-classifier.streamlit.app/)
- Users can upload custom images and get real-time predictions to evaluate model performance in the real world.

## 📊 Current Results

| **Model** | **Dataset (Classes)** | **Test Accuracy** | **Notes** |
| :--- | :--- | :--- | :--- |
| Custom CNN | Intel Image (6) | 79.70% | Trained from scratch |
| ResNet18 | Intel Image (6) | 90.30% | Frozen Backbone |
| **EfficientNet-B3** | **Food-101 (101)** | **~71.00%** | **Partial Fine-Tuning** |

*Note: Achieving ~71% on Food-101 is highly significant, as random guessing yields <1% accuracy, and distinguishing between 101 highly similar food textures requires complex feature extraction.*

## 🧠 Concepts Covered

### Image & Dataset Handling
- `torchvision.datasets.ImageFolder`
- Image preprocessing & Data augmentation (Rotation, ColorJitter, Flips)
- Handling dynamic input sizes with `AdaptiveAvgPool2d`

### Neural Network Foundations
- CNN architecture design (`Conv2d`, `MaxPool2d`, `BatchNorm2d`)
- Parameter growth & GPU/VRAM bottleneck mitigation

### Transfer Learning
- Pretrained ImageNet models (ResNet18, EfficientNetB3)
- Feature extraction vs. Partial fine-tuning
- Unfreezing specific backbone layers

### MLOps & Deployment
- Macro vs. Micro metric averaging for multiclass problems
- Exporting Python structures to JSON for UI integration
- Streamlit web applications & Model caching (`@st.cache_resource`)
- Hosting large `.pth` model weights via GitHub Releases

## 🔬 Learning Progression

The experiments in this folder follow a progression from basic image classification toward complex fine-grained modeling and web deployment:

    Image Classification
            ↓
    Food-101 MLP
            ↓
    Food-101 CNN
            ↓
    Custom CNN Architecture
            ↓
    Transfer Learning (Feature Extraction)
            ↓
    Partial Fine-Tuning (EfficientNet)
            ↓
    Fine-Grained Classification (101 Classes)
            ↓
    Live Web Deployment (Streamlit)
