# AI & Machine Learning Engineering Portfolio

*Note:* This is an actively maintained repository documenting an applied progression from core programming paradigms to deep learning architectures and production inference pipelines. It emphasizes understanding low-level mechanics, mitigating training bottlenecks, and deploying functional models.

---

## 📂 Repository Structure

Each module contains dedicated notebooks, data pipelines, and architectural breakdowns:

- **[01-Python-Basics](01-Python-Basics)** 🐍  
  Foundational programming: data structures, control flow, functional programming, and modular scripting.

- **[02-OOPs](02-OOPs)** 🏗️  
  Object-Oriented Programming (Classes, Inheritance, Polymorphism, and Encapsulation) focused on scalable software design.

- **[03-Numpy](03-Numpy)** 🧮  
  Scientific computing, multidimensional array manipulation, vectorized operations, and tensor broadcasting mechanics.

- **[04-EDA](04-EDA)** 📊  
  Exploratory data analysis, automated cleaning pipelines, missing-value imputation, and visual distribution modeling with Pandas, Matplotlib, and Seaborn.

- **[05-Machine-Learning](05-Machine-Learning)** ⚙️  
  End-to-end predictive modeling workflows utilizing Scikit-Learn pipelines, hyperparameter optimization (`GridSearchCV`, `RandomizedSearchCV`), gradient boosting (`XGBoost`, `LightGBM`), and unsupervised cluster/reduction analysis (K-Means, DBSCAN, PCA, t-SNE).  
  *Featured Work:* Customer Segmentation, MNIST Dimensionality Reduction, Kaggle House Prices, and US Stock Returns Prediction.

- **[06-Deep-Learning](06-Deep-Learning)** 🧠  
  Neural network engineering with PyTorch, CUDA-accelerated workflows, data pipelines (`torchvision`), and interactive model deployment.  
  *Featured Work:* Breast Cancer Classification, MNIST Digit Recognition, Custom Multi-Layer CNNs, Pretrained ResNet-18 Feature Extraction, and Fine-Grained Food-101 Transfer Learning.

---

## 🚀 Featured Deployments & Benchmarks

### 1. Fine-Grained Vision: EfficientNet-B3 on Food-101
- **Architecture:** Pretrained `EfficientNet-B3` with custom deep classification head (`1536 -> 256 -> 128 -> 101`).
- **Optimization Strategy:** Partial unfreezing of final `MBConv` blocks, GPU-native metric calculation (`torchmetrics.update()`), dynamic spatial pooling (`AdaptiveAvgPool2d`), and heavy regularization via data augmentations.
- **Outcome:** **~71% Test Accuracy** across 101 fine-grained classes (outperforming baseline random probability of ~0.99%).

### 2. Interactive Web Apps
- **Natural Landscape Classifier:** ResNet-18 pipeline deployed on Streamlit Cloud for real-time inference.
- **Live Demo:** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vikas-landscape-classifier.streamlit.app/)

---

## 🛠️ Core Tech Stack

| Domain | Technologies & Libraries |
| :--- | :--- |
| **Languages** | Python |
| **Data & Math** | NumPy, Pandas |
| **Classical ML** | Scikit-Learn, LightGBM, XGBoost |
| **Deep Learning** | PyTorch (`torch`, `torch.nn`), `torchvision`, `torchmetrics` |
| **Deployment** | Streamlit, Git, GitHub Releases |
| **Visualization** | Matplotlib, Seaborn |
| **Environments** | Jupyter Notebook, Google Colab (T4 GPU), VS Code |

---

## 🧭 Navigation & Source Code

Refer to the internal directory links above to review raw notebook code, training curves, mathematical notes, and deployment scripts.
