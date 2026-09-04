# 👁️ 02 - PyTorch Computer Vision

Welcome to the **PyTorch Computer Vision** module! This directory documents my progression from baseline feedforward architectures to custom Convolutional Neural Networks (CNNs). Rather than simply optimizing for the highest accuracy, this module focuses on architectural experimentation—scientifically documenting *why* certain models fail and succeed on complex visual tasks.

## 🎯 Overview & Objectives

Computer vision requires models to understand spatial hierarchies, edges, textures, and color relationships across 2D/3D grids of pixels. This section explores:
- **Data Pipelines & Augmentation:** Implementing custom `torchvision.transforms` (resizing, jittering, flips, normalization), handling raw directory structures with `ImageFolder`, and efficient `DataLoader` streaming.
- **Spatial Feature Extraction:** Understanding why standard Multi-Layer Perceptrons (MLPs) fail on complex image datasets and transitioning to convolutional architectures (`nn.Conv2d`, `nn.MaxPool2d`).
- **Architectural Benchmarking:** Identifying the limits of shallow CNNs trained from scratch, applying regularization, and preparing for advanced techniques like Transfer Learning.

## 📁 Notebooks & Experiments

### 🥪 01. The MLP Baseline Failure (Food-101)
- **File:** `01_food101_mlp_baseline.ipynb`
- **Dataset:** Food-101 (101 food categories, resized to 224x224x3)
- **Architecture:** Multi-Layer Perceptron (MLP) with `nn.Flatten()` and stacked `nn.Linear` + `nn.ReLU` layers.
- **Result:** ~1% to 4% Accuracy.
- **Key Finding:** Flattening 2D RGB images into 1D vectors destroys local spatial structures. An MLP mathematically cannot extract 2D hierarchical features (shapes, edges), proving standard feedforward networks are fundamentally unfit for complex vision tasks.

### 🥪 02. The Custom 6-Layer CNN Bottleneck (Food-101)
- **File:** `02_food101_cnn_model.ipynb`
- **Architecture:** Custom 6-layer CNN (TinyVGG variant) using `nn.Conv2d`, `nn.MaxPool2d`, and `nn.ReLU`.
- **Result:** Plateaus around ~20-30% Accuracy.
- **Key Finding:** While CNNs successfully preserve spatial awareness, shallow networks trained from scratch lack the parameter capacity and depth required for fine-grained 101-class classification (e.g., distinguishing *beef carpaccio* from *beef tartare*). Additionally, the absence of modern components like `BatchNorm2d` and residual skip connections causes gradient degradation and stalls learning.

### 🏞️ 03. The Sandbox Benchmark: Regularization (Intel Landscapes)
- **File:** `03_intel_image_classification_cnn_sandbox.ipynb`
- **Dataset:** Intel Image Classification (6 landscape classes, resized to 150x150, streamed directly via Kaggle API)
- **Architecture:** Custom 4-layer CNN integrating `nn.BatchNorm2d`, `nn.Dropout(p=0.3)`, and L2 Weight Decay. 
- **Result:** ~82.93% Test Accuracy.
- **Key Finding:** Applying heavy regularization (Spatial Data Augmentation like flips/rotations, Batch Normalization, and Dropout on the flattened linear input) successfully prevents the model from rapidly overfitting the training data. However, hitting ~83% accuracy highlights the mathematical "roof" of shallow custom CNNs, setting the stage for Transfer Learning.

---

## 🚧 Upcoming Milestones

- **Model 04: Transfer Learning** — Returning to the full Food-101 dataset (or similar high-complexity tasks) to fine-tune a pre-trained state-of-the-art backbone (e.g., EfficientNet, ResNet) to break past the 90%+ accuracy barrier.
