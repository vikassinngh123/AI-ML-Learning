# 🧠 06 - Deep Learning

Welcome to the Deep Learning module! This directory covers artificial neural networks, deep learning frameworks, and advanced AI architectures.

## 📁 Sub-Modules & Projects

## 🔥 [01 - PyTorch](01-PyTorch)

*Foundational tensor manipulation, GPU computing, and framework mechanics.*

- 🧱 **PyTorch Fundamentals:** Complete guide covering tensor math, shape manipulation (`reshape`, `stack`, `permute`), indexing, NumPy conversion, reproducibility, and GPU device-agnostic execution (`.to(device)`).

- 📈 **PyTorch Basic Models:** End-to-end implementations of custom neural networks from scratch. Includes:
  - Custom architectures built using `nn.Module`, `nn.Parameter`, and `nn.Linear`.
  - Explicit training loops with backpropagation and optimization.
  - *Implemented Models:* 
    - **Cubic Polynomial Regression** (MSE Loss)
    - **Binary Classification** for Breast Cancer Prediction (`BCEWithLogitsLoss` and accuracy evaluation)
    - **Multiclass Classification** on the MNIST dataset (`CrossEntropyLoss`)

- 👁️ **PyTorch Computer Vision:** Custom vision pipelines and convolutional architectures designed to process complex, high-dimensional RGB image datasets. Includes:
  - **Data Engineering & Augmentation:** Building robust pipelines utilizing `torchvision.transforms` (ColorJitter, resizing) and optimized `DataLoader` streaming.
  - **The MLP Baseline Failure (Food-101):** Empirical benchmarking that proves the mathematical destruction of 2D spatial features when flattening images for standard Multi-Layer Perceptrons.
  - **Custom 6-Layer CNN Architecture:** Deep convolutional networks built using `nn.Conv2d` and `nn.MaxPool2d` to preserve spatial hierarchy, complete with architectural bottleneck analysis (parameter explosions and GPU VRAM constraints).

---

*🚧 This module is an active Work in Progress! New deep learning architectures, workflows, and projects are added as learning progresses.*
