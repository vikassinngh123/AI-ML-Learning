<div align="center">

# 🔍 R-CNN Object Detection from Scratch
### *A Ground-Up PyTorch Implementation of Region-based CNNs*

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)

**A modular, from-scratch implementation of the classic R-CNN architecture using PyTorch. This project demonstrates the fundamental mechanics of two-stage object detectors, including Selective Search region proposals, bounding box delta regression, Non-Maximum Suppression (NMS), and custom tensor-based loss functions.**

</div>

---

## 🧠 Architecture & Methodology

This implementation breaks down the R-CNN pipeline into an interpretable, educational workflow trained on a filtered subset of Pascal VOC 2007 (Person, Dog, Car):

1. **Region Proposals:** Utilizes classical Selective Search to generate bounding box proposals per image.
2. **Feature Extraction:** Extracts features from `224x224` resized crops using a frozen `ResNet-18` backbone.
3. **Classification Head:** A linear layer trained with Cross-Entropy Loss to classify proposals into foreground classes (`person`, `dog`, `car`) or `background`.
4. **Regression Head:** A linear layer trained with Mean Squared Error (MSE) Loss on normalized bounding box deltas to refine proposal coordinates.
5. **Post-Processing & Inference:** Applies bounding box delta refinement and `batched_nms` (IoU thresholding) to eliminate redundant overlapping bounding boxes during inference.

---

## 📂 Repository Structure

| File / Module | Description |
| :--- | :--- |
| **`R-CNN.ipynb`** | The main experiment notebook. Contains the data parsing, training loop, evaluation script (mAP), and the visual inference pipeline for testing the model on new images. |
| **`rcnn_model.py`** | Contains the dual-head R-CNN class built on a pre-trained ResNet-18 backbone. |
| **`rcnn_dataset.py`** | Handles the PyTorch Dataset logic, Selective Search generation, and RoI cropping/resizing. |
| **`rcnn_detection_utils.py`** | Pure PyTorch tensor implementations for bounding box math, delta decoding, and Intersection over Union (IoU). |
| **`detection_utils.py`** | Helper utilities for NMS and box regression. |

---

## 📊 Performance Baseline

This custom implementation achieves a **~24.47% mAP@50** on the evaluation set. 
*Note: For a frozen ResNet-18 backbone utilizing a limited number of Selective Search proposals, this is a mathematically sound baseline that proves the end-to-end pipeline (crop extraction → dual-head inference → delta decoding → batched NMS) functions correctly.*

---

## 🚀 Local Quick Start & Testing

**1. Clone the repository and install dependencies:**
```bash
git clone [https://github.com/vikassinngh123/AI-ML-Learning.git](https://github.com/vikassinngh123/AI-ML-Learning.git)
cd AI-ML-Learning/06-Deep-Learning/01-PyTorch/03-PyTorch-Object-Detection/01_rcnn
pip install torch torchvision torchmetrics opencv-python selectivesearch seaborn
```

**2. Prepare the datasets:**
Ensure you have the required JSON data files (`train_data.json`, `test_data.json`, `rcnn_proposals_data.json`) in the root directory.

**3. Run Inference on a Test Image:**
Open `R-CNN.ipynb` and run the bottom cells to test the model on custom images (e.g., `man_dog_image.jpg`). The pipeline will:
- Extract Selective Search proposals.
- Filter out microscopic/garbage boxes (`<50x50`).
- Resize crops to `224x224` and run them through the ResNet-18 backbone.
- Apply bounding box regression and `batched_nms` (IoU = 0.15) to render the final detections using OpenCV.

---

<div align="center">
<b>Built by <a href="https://github.com/vikassinngh123">Vikas Singh</a></b>
</div>