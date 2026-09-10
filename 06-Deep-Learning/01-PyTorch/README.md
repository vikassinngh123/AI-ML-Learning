# 🔥 01 - PyTorch

Welcome to the **PyTorch** sub-module! This directory tracks my progress from learning basic tensor math to building custom deep learning models and deploying them to the web.

## 📁 Directory Structure & Projects

### 🧱 [00: PyTorch Fundamentals](00_pytorch_fundamentals.ipynb)
*   **Overview:** Getting started with PyTorch! Figuring out how to create tensors, reshape them, do matrix multiplication, and move operations over to the GPU to make them run faster.
*   **Key Concepts:** `.view()`, `.reshape()`, `torch.permute()`, and writing device-agnostic code (`.to(device)`).

### 🧠 [01-PyTorch-Basic-Models](01-PyTorch-Basic-Models)
*   **Overview:** Moving from raw numbers to actually building neural networks from scratch using `torch.nn`. 
*   **Key Projects:**
    *   **Regression & Binary Classification:** Wrote custom training loops to predict continuous values and classify binary outcomes.
    *   **MNIST Digit Recognizer:** Built a custom feed-forward neural network that hit **97.18% accuracy**! Used `CrossEntropyLoss`, `nn.Dropout` to stop overfitting, and Seaborn to visualize the confusion matrix.

### 👁️ [02-PyTorch-Computer-Vision](02-PyTorch-Computer-Vision)
*   **Overview:** Working with images! This folder covers image pipelines, Convolutional Neural Networks (CNNs), and my first web app deployment.
*   **Key Projects:**
    *   **Food-101 MLP Baseline:** Tested a basic Multi-Layer Perceptron to see what happens when you flatten an image (spoiler: it completely ruins the 2D spatial features).
    *   **Custom 6-Layer CNN:** Built my own image classifier using `nn.Conv2d` and `nn.MaxPool2d` to extract visual features while managing GPU memory limits.
    *   **Transfer Learning (ResNet-18):** Fine-tuned a massive pre-trained ResNet-18 model on a custom dataset to classify natural landscapes.
    *   **Live Web Deployment:** Turned my landscape classifier into an interactive Streamlit web app! Solved environment limitations and bypassed GitHub size limits to make it work.
        *   🚀 **Live Demo:** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vikas-landscape-classifier.streamlit.app/)

## 🛠️ Tech Stack & Libraries
*   **Frameworks:** PyTorch (`torch`, `torch.nn`, `torchvision`), Streamlit
*   **Data & Visualization:** NumPy, Pandas, Matplotlib, Seaborn
*   **Environment:** Google Colab (T4 GPU)
