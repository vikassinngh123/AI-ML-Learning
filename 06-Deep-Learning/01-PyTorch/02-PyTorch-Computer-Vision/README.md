#  02 - PyTorch Computer Vision

Welcome to the **PyTorch Computer Vision** module! This directory documents the progression from baseline feedforward architectures to advanced Convolutional Neural Networks (CNNs) and Transfer Learning for visual recognition tasks.

---

##  Overview & Objectives

Computer vision requires models to understand spatial hierarchies, edges, textures, and color relationships across 2D/3D grids of pixels. This section explores:
* **Data Pipelines & Augmentation:** Implementing custom `torchvision.transforms` (resizing, jittering, flips, normalization) and efficient `DataLoader` streaming.
* **Spatial Feature Extraction:** Understanding why standard Multi-Layer Perceptrons (MLPs) fail on complex image datasets and transitioning to convolutional architectures (`nn.Conv2d`, `nn.MaxPool2d`).
* **Evaluation & Diagnostics:** Analyzing classification performance using multiclass metrics, confusion matrices, and tracking loss curves.

---

## 📁 Notebooks & Experiments

### 🥪 01. Food-101 MLP Baseline & The Need for CNNs
* **File:** [01_food101_mlp_baseline.ipynb](01_food101_mlp_baseline.ipynb)
* **Dataset:** [Food-101](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/) (101 food categories, resized to $224 \times 224 \times 3$)
* **Architecture:** Multi-Layer Perceptron (MLP) with `nn.Flatten()` and stacked `nn.Linear` + `nn.ReLU` layers.
* **Key Takeaways & Findings:**
  * Demonstrated the limitation of feedforward networks on high-dimensional visual data ($150,528$ input features per image).
  * Flattening 2D images into 1D vectors destroys local spatial structures (pixel neighborhoods).
  * Proved empirically that standard linear layers fail to generalize on complex color image datasets, establishing the necessity for **Convolutional Neural Networks (CNNs)**.

---

## 🚧 Upcoming Milestones
* **Model 02: TinyVGG / Custom CNN Architecture** — Building custom convolutional blocks with `nn.Conv2d` and `nn.MaxPool2d`.
* **Model 03: Custom Dataset Pipeline** — Loading and processing custom uncurated image datasets from disk.
* **Model 04: Transfer Learning** — Fine-tuning state-of-the-art pre-trained backbones (e.g., EfficientNet, ResNet) on custom vision tasks.
