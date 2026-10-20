# 🧠 AI & Machine Learning Engineering Portfolio

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

> **Note:** An actively maintained repository documenting my applied progression from core Python and OOP paradigms to classical machine learning pipelines, deep learning architectures, and production-ready computer vision deployments.

---

## 🏗️ Learning Progression Architecture

```text
[01-Python-Basics] ──► [02-OOPs] ──► [03-Numpy] ──► [04-EDA]
                                                       │
                                                       ▼
        [Production Web Apps & CV] ◄── [06-Deep-Learning] ◄── [05-Machine-Learning]
```

---

## 📂 Repository Structure

| Module | Core Focus & Implementations |
| :--- | :--- |
| **[`01-Python-Basics`](./01-Python-Basics)** | 🐍 Foundational programming: core data structures, control flow, functional programming, and modular scripting. |
| **[`02-OOPs`](./02-OOPs)** | 🏗️ Object-Oriented Programming (Classes, Inheritance, Polymorphism, Encapsulation, Magic Methods) for scalable ML software design. |
| **[`03-Numpy`](./03-Numpy)** | 🧮 Scientific computing, multidimensional array manipulation, vectorized math, and tensor broadcasting mechanics. |
| **[`04-EDA`](./04-EDA)** | 📊 Exploratory data analysis, automated data cleaning pipelines, missing-value imputation, and statistical visualization (`Pandas`, `Matplotlib`, `Seaborn`). |
| **[`05-Machine-Learning`](./05-Machine-Learning)** | ⚙️ End-to-end predictive modeling using `Scikit-Learn` pipelines, hyperparameter tuning (`GridSearchCV`, `RandomizedSearchCV`), gradient boosting (`XGBoost`, `LightGBM`), and unsupervised learning (`K-Means`, `DBSCAN`, `PCA`, `t-SNE`).<br>**Featured Work:** *Customer Segmentation, MNIST Dimensionality Reduction, Kaggle House Prices, US Stock Returns Prediction.* |
| **[`06-Deep-Learning`](./06-Deep-Learning)** | 🧠 Neural network engineering with `PyTorch`, CUDA-accelerated training loops, custom `torchvision` datasets, transfer learning, and object detection mechanics.<br>**Featured Work:** *Breast Cancer ANN, MNIST Digit Recognition, Custom Multi-Layer CNNs, Pretrained ResNet-18 Feature Extraction, Fine-Grained Food-101 Classification, and Object Detection from Scratch (R-CNN & YOLOv1).* |

---

## 🚀 Featured Models, Object Detection & Live Deployments

### 1. Object Detection Architectures (`06-Deep-Learning`)
* **R-CNN & YOLOv1 Mechanics:** Implemented foundational object detection pipelines covering region proposals, grid-based bounding box regression, **Intersection over Union (IoU)** math, and **Non-Maximum Suppression (NMS)** post-processing.

### 2. Fine-Grained Computer Vision: EfficientNet-B3 on Food-101
* **Architecture:** Pretrained `EfficientNet-B3` backbone with a custom deep classification head (`1536 -> 256 -> 128 -> 101`).
* **Optimization Strategy:** Partial unfreezing of final MBConv blocks, GPU-native metric calculation (`torchmetrics`), dynamic spatial pooling (`AdaptiveAvgPool2d`), and heavy regularization via data augmentations.
* **Benchmark:** Achieved **~71% Test Accuracy** across 101 fine-grained culinary categories (vs. ~0.99% random baseline). Model weights published in [GitHub Releases](../../releases).

### 3. Live Interactive Web Applications
| Application | Model Architecture | Live Deployment |
| :--- | :--- | :--- |
| **Natural Landscape Classifier** | Pretrained `ResNet-18` Transfer Learning Pipeline | [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vikas-landscape-classifier.streamlit.app/) |
| **Food-101 Culinary Classifier** | Custom `EfficientNet-B3` Deep Classifier | [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://food101-classifier-vikas.streamlit.app/) |

---

## 🛠️ Core Tech Stack

| Domain | Technologies & Libraries |
| :--- | :--- |
| **Languages** | Python, C++ (DSA) |
| **Data & Math** | NumPy, Pandas |
| **Classical ML** | Scikit-Learn, LightGBM, XGBoost |
| **Deep Learning** | PyTorch (`torch`, `torch.nn`), `torchvision`, `torchmetrics` |
| **Computer Vision** | OpenCV, R-CNN, YOLO Mechanics, IoU & NMS Math |
| **Deployment & MLOps** | Streamlit Cloud, Git, GitHub Releases |
| **Visualization** | Matplotlib, Seaborn |
| **Environments** | Jupyter Notebook, Google Colab (T4 GPU), VS Code |

---

## 💻 Quick Start (Clone & Explore Locally)

```bash
# 1. Clone the repository
git clone [https://github.com/vikassinngh123/AI-ML-Learning.git](https://github.com/vikassinngh123/AI-ML-Learning.git)
cd AI-ML-Learning

# 2. Create and activate a virtual environment
python -m venv .venv
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# macOS / Linux:
# source .venv/bin/activate

# 3. Launch Jupyter Notebook to explore modules
pip install jupyter numpy pandas matplotlib seaborn scikit-learn torch torchvision opencv-python
jupyter notebook
```
