# 🧠 06 - Deep Learning

Welcome to the Deep Learning module! This directory tracks my journey into artificial neural networks, computer vision, and deploying ML models to the web.

## 📁 Sub-Modules & Projects

## 🔥 [01 - PyTorch](01-PyTorch)

*Learning tensor math, GPU computing, and how deep learning frameworks actually work under the hood.*

- 🧱 **PyTorch Fundamentals:** Getting comfortable with tensor math, reshaping matrices, and running code on the GPU.
- 📈 **PyTorch Basic Models:** Building my first neural networks entirely from scratch.
  - Wrote custom architectures using `nn.Module` and built my own training loops with backpropagation.
  - *Projects:*
    - *Cubic Polynomial Regression* (Predicting continuous values)
    - *Breast Cancer Prediction* (Binary classification)
    - *MNIST Digit Recognizer* (Multiclass classification)

- 👁️ **PyTorch Computer Vision:** Processing image data and building convolutional networks.
  - *Why standard MLPs fail on images:* Tested a basic Multi-Layer Perceptron and saw firsthand how flattening an image destroys its 2D spatial features.
  - *Custom 6-Layer CNN:* Built my own architecture using `nn.Conv2d` and `nn.MaxPool2d` to extract image features while managing GPU memory limits.
  - *Transfer Learning (ResNet-18):* Took a massive, pre-trained model and fine-tuned it on a custom dataset to classify natural landscapes, comparing its accuracy against my custom CNN.

- 🌐 **Model Deployment & MLOps:** Taking my models out of Jupyter Notebooks and putting them on the internet!
  - *Streamlit Web App:* Deployed a live, interactive UI [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vikas-landscape-classifier.streamlit.app/) where anyone can upload an image and get a real-time prediction.
  - *Engineering Hurdles Solved:* Figured out how to configure PyTorch to run on free CPU-only cloud instances, used `@st.cache_resource` so the heavy models load instantly from memory, and wrote a script to download the massive 11MB+ `.pth` weight files from GitHub Releases since they were too big to push normally.

*🚧 This module is an active Work in Progress as I continue learning!*
