# 🤖 01 - PyTorch Basic Models

Welcome to the PyTorch Basic Models directory! This folder contains end-to-end neural network implementations built from scratch and trained on simple, synthetic, or toy datasets.

---

## 🎯 Approach
Instead of isolating theory, every notebook in this module represents a complete, self-contained pipeline:
* **Data Generation & Handling:** Creating synthetic datasets, feature transformations, and tensor structuring.
* **Model Architecture:** Custom neural networks built using `nn.Module` and `nn.Parameter`.
* **Optimization Setup:** Defining loss functions (`nn.MSELoss`, etc.) and optimizers (`SGD`, `Adam`).
* **Training & Evaluation:** Writing explicit training loops, backpropagation (`loss.backward()`), optimization steps (`optimizer.step()`), and evaluation using `torch.inference_mode()`.
* **Serialization:** Saving and loading model `state_dict()` weights.

---

## 📁 Implemented Models

* **📈 Model 01: Cubic Polynomial Regression**
  * **File:** [`01_cubic_regression_model.ipynb`](./01_cubic_regression_model.ipynb)
  * **Equation:** $y = w_1 x^3 + w_2 x^2 + w_3 x + b$
  * **Dataset:** Synthetic non-linear continuous data generated over $[-5, 5]$.
  * **Key Concepts:** Custom parameter initialization with `nn.Parameter`, non-linear forward computation, train/test splitting, and loss tracking.

---
*🚧 Work in Progress: Additional end-to-end basic architectures will be added here as they are built.*
