# 🔥 01 - PyTorch

Welcome to the PyTorch sub-module! This directory is dedicated to mastering **PyTorch**, from foundational tensor mechanics to advanced model training.

## 📁 Notebooks & Projects

* **🧱 00: PyTorch Fundamentals**
  * **File:** [00_Pytorch_Fundamentals.ipynb](00_Pytorch_Fundamentals.ipynb)
  * **Overview:** A complete walkthrough of PyTorch tensor setup, metadata inspection, mathematical operations, dimension manipulation, and GPU acceleration.
  * **Key Concepts Covered:**
    * **Tensor Creation:** Scalars, vectors, matrices, random tensors, ranges (`arange`), and `zeros_like` / `ones`.
    * **Tensor Attributes:** Checking metadata using `.shape`, `.ndim`, `.dtype`, and `.device`.
    * **Tensor Operations:** Element-wise arithmetic, matrix multiplication (`torch.matmul` / `.mm`), and shape fixes via Transpose (`.T`).
    * **Aggregations:** Statistical summary functions (`min()`, `max()`, `mean()`, `sum()`) and positional lookups (`argmin()`, `argmax()`).
    * **Shape Manipulation:** Reshaping (`.reshape()`), views (`.view()`), stacking (`torch.stack()`), squeezing/unsqueezing, and dimension permutation (`torch.permute()`).
    * **Indexing & Slicing:** Multi-axis tensor selection and targeted slicing across arbitrary dimensions.
    * **NumPy Interoperability:** Converting between NumPy arrays and PyTorch tensors (`torch.from_numpy()`, `.numpy()`).
    * **Reproducibility:** Setting manual seeds (`torch.manual_seed()`) for deterministic random tensor generation.
    * **GPU & Device-Agnostic Code:** Setting setup variables (`device = "cuda" if ... else "cpu"`), moving tensors to GPU (`.to(device)`), and returning tensors back to CPU for NumPy conversions (`.cpu()`).

---
*🚧 Work in Progress: Next notebook will cover the PyTorch Workflow (nn.Module, loss functions, optimizers, and training loops).*
