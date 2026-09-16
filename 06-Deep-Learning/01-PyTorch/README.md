# 🔥 01 - PyTorch

Welcome to the **PyTorch** sub-module! This directory tracks my progress from learning basic tensor math to building custom deep learning models and deploying them to the web.

## 📁 Directory Structure & Projects

### 🧱 [00: PyTorch Fundamentals](./00_pytorch_fundamentals.ipynb)
- **Overview:** Getting started with PyTorch! Figuring out how to create tensors, reshape them, do matrix multiplication, and move operations over to the GPU to make them run faster.
- **Key Concepts:** `.view()`, `.reshape()`, `torch.permute()`, and writing device-agnostic code (`.to(device)`).

### 🧠 [01-PyTorch-Basic-Models](./01-PyTorch-Basic-Models)
- **Overview:** Moving from raw numbers to actually building neural networks from scratch using `torch.nn`.
- **Key Projects:**
  - **Regression & Binary Classification:** Wrote custom training loops to predict continuous values and classify binary outcomes.
  - **MNIST Digit Recognizer:** Built a custom feed-forward neural network that hit **97.18% accuracy**! Used `CrossEntropyLoss`, `nn.Dropout` to stop overfitting, and Seaborn to visualize the confusion matrix.

### 👁️ [02-PyTorch-Computer-Vision](./02-PyTorch-Computer-Vision)
- **Overview:** Working with images! This folder covers data pipelines, Convolutional Neural Networks (CNNs), transfer learning on massive datasets, and web app deployment.
- **Key Projects:**
  - **Food-101 MLP Baseline:** Tested a basic Multi-Layer Perceptron to see what happens when you flatten an image (spoiler: it destroys 2D spatial features).
  - **Custom 6-Layer CNN:** Built an image classifier using `nn.Conv2d` and `nn.MaxPool2d` to extract visual features while managing GPU memory limits.
  - **Transfer Learning (ResNet-18):** Fine-tuned an ImageNet-pretrained ResNet-18 model on a custom dataset to classify natural landscapes (achieving **90.30% accuracy**).
  - **Fine-Grained Classification (EfficientNet-B3):** Pushed into complex multiclass modeling on the **Food-101** dataset. Tackled hardware constraints via partial layer unfreezing, custom multi-layer classification heads, and optimized batch evaluation, reaching **~71% accuracy** across 101 fine-grained classes.
  - **Live Web Deployments:** 
    - 🌲 **Landscape Classifier:** Deployed the fine-tuned ResNet-18 model as an interactive Streamlit app.
      - 🚀 **Live Demo:** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vikas-landscape-classifier.streamlit.app/)
    - 🍔 **Food-101 Classifier:** Deployed the fine-tuned EfficientNet-B3 model into a dedicated culinary web app featuring a dark UI theme.
      - 🚀 **Live Demo:** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://food101-efficientnetb3.streamlit.app/)

## 🛠️ Tech Stack & Libraries
- **Frameworks:** PyTorch (`torch`, `torch.nn`, `torchvision`), `torchmetrics`, Streamlit
- **Data & Visualization:** NumPy, Pandas, Matplotlib, Seaborn
- **Environment:** Google Colab (T4 GPU)
