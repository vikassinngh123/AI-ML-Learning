# 🔥 01 - PyTorch

Welcome to the **PyTorch** sub-module! This directory documents my end-to-end journey in mastering PyTorch, progressing from foundational tensor mechanics to advanced Deep Learning and Computer Vision architectures.

---

## 📁 Directory Structure & Projects

### 🧱 [00: PyTorch Fundamentals](00_pytorch_fundamentals.ipynb)
* **Overview:** A complete walkthrough of PyTorch tensor setup, metadata inspection, mathematical operations, dimension manipulation, and GPU acceleration.
* **Key Concepts:** Tensor creation, shape manipulation (`.view()`, `.reshape()`, `torch.permute()`), matrix multiplication, and device-agnostic code (`.to(device)`).

### 🧠 [01-PyTorch-Basic-Models](01-PyTorch-Basic-Models)
* **Overview:** Transitioning from raw tensors to building, training, and evaluating neural network architectures from scratch using `torch.nn`. 
* **Key Projects:**
  * **Regression & Binary Classification:** Building models to predict continuous values and binary outcomes using custom explicit training loops.
  * **MNIST Multiclass Classification:** Engineered a custom feed-forward neural network achieving **97.18% accuracy**, utilizing `CrossEntropyLoss`, `nn.Dropout` for regularization, and Seaborn confusion matrices for deep evaluation.

### 👁️ [02-PyTorch-Computer-Vision](02-PyTorch-Computer-Vision)
* **Overview:** Handling spatial data, building custom image pipelines (`torchvision.transforms`, `DataLoader`), and exploring Convolutional Neural Networks (CNNs).
* **Key Projects:**
  * **Food-101 MLP Baseline:** Implemented a baseline Multi-Layer Perceptron to empirically prove why feedforward networks fail on high-dimensional visual data (demonstrating the destruction of spatial features via `nn.Flatten()`).
  * *(Upcoming)* Custom CNN Architectures (`nn.Conv2d`) and Transfer Learning.

---

## 🛠️ Tech Stack & Libraries
* **Framework:** PyTorch (`torch`, `torch.nn`, `torchvision`)
* **Data Manipulation:** NumPy, Pandas
* **Visualization:** Matplotlib, Seaborn
* **Environment:** Google Colab (T4 GPU)
