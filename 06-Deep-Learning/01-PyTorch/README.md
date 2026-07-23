# 🔥 01 - PyTorch

Welcome to the PyTorch sub-module! This directory is dedicated to learning **PyTorch**, one of the most popular and powerful open-source machine learning frameworks used for deep learning research and production.

## 📁 Notebooks & Projects

* **🧱 00: PyTorch Fundamentals**
  * **File:** [00_Pytorch_Fundamentals.ipynb](00_Pytorch_Fundamentals.ipynb)
  * **Overview:** Complete foundation of PyTorch tensors, operations, and metadata manipulation.
  * **Key Concepts Covered:**
    * **Tensor Creation & Setup:** Environment setup, GPU (CUDA) availability checks, scalars, vectors, matrices, random tensors, and tensor ranges (`arange`, `zeros_like`).
    * **Tensor Attributes:** Checking metadata using `.shape`, `.ndim`, `.dtype`, and `.device`.
    * **Tensor Math & Operations:** Element-wise arithmetic (`+`, `-`, `*`, `/`), matrix multiplication (`torch.matmul` / `torch.mm`), and resolving shape mismatches using Transposition (`.T`).
    * **Aggregation:** Summary statistics using `min()`, `max()`, `mean()`, `sum()`, `argmin()`, and `argmax()`.
    * **Shape Manipulation:** Reshaping (`.reshape()`), memory-shared views (`.view()`), stacking (`torch.stack()`), and adding/removing dimensions (`squeeze()` / `unsqueeze()`).

## 🎯 Upcoming Topics

As I progress through my deep learning journey, this folder will expand to include:
* **Indexing & Reproducibility:** Slicing tensors, setting manual seeds (`torch.manual_seed`), and device-agnostic code (`.to(device)`).
* **The PyTorch Workflow:** Data preparation, building custom models (`nn.Module`), writing training/testing loops, loss functions, and optimizers.
* **Neural Network Classification:** Building models to classify linear and non-linear data.
* **Computer Vision:** Leveraging `torchvision` and Convolutional Neural Networks (CNNs).
