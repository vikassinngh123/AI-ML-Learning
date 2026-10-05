# R-CNN Object Detection from Scratch (PyTorch)

A modular, ground-up implementation of the classic R-CNN (Region-based Convolutional Neural Network) architecture using PyTorch. This project demonstrates the fundamental mechanics of two-stage object detectors, including Selective Search region proposals, bounding box delta regression, and custom tensor-based loss functions.

## 📂 Repository Structure

* **`rcnn_model.py`**: Contains the dual-head `RCNN` class built on a pre-trained (frozen) ResNet-18 backbone. It splits into a classification head (identifying classes) and a regression head (predicting bounding box offsets).
* **`rcnn_dataset.py`**: Handles the PyTorch `Dataset` and `DataLoader` logic. Responsible for ingesting Pascal VOC images, applying Selective Search proposals, and cropping/resizing regions of interest (RoIs) to 224x224 for the backbone.
* **`rcnn_detection_utils.py`**: The core mathematics engine. Contains pure PyTorch tensor implementations for:
  * Bounding box parameterization (calculating Δx, Δy, Δw, Δh)
  * Delta decoding (transforming predictions back to image coordinates)
  * Intersection over Union (IoU)
  * Custom PyTorch Tensor Loss functions (avoiding NumPy to maintain the autograd graph)
* **`R_CNN.ipynb`**: The main experiment tracker. Contains the end-to-end training loop, loss tracking (Classification vs. Regression), and the final Mean Average Precision (mAP) evaluation script using `torchvision.ops.nms` and `torchmetrics`.
* **`.gitignore`**: Excludes heavy dataset files (`*.json`) and model weights (`*.pth`) from version control.

## 🧠 Architecture & Methodology

1. **Region Proposals:** Utilizes classical Selective Search to generate ~500 region proposals per image.
2. **Feature Extraction:** Extracts features from 224x224 cropped proposals using a frozen ResNet-18 `AdaptiveAvgPool2d` output.
3. **Classification Head:** A linear layer trained with Cross-Entropy Loss to classify proposals into specific foreground classes (`person`, `dog`, `car`) or `background`.
4. **Regression Head:** A linear layer trained with Mean Squared Error (MSE) Loss on normalized bounding box deltas, strictly masked to only train on foreground proposals.
5. **Post-Processing:** Applies PyTorch's native Non-Maximum Suppression (NMS) per class to eliminate redundant overlapping bounding boxes.

## 📊 Performance Baseline

This custom implementation achieves a **~25% mAP@50** on the evaluation set. 

*Note: For a frozen ResNet-18 backbone utilizing only 500 Selective Search proposals per image, ~25% mAP is a mathematically sound baseline. It proves the end-to-end pipeline (crop extraction -> dual-head inference -> delta decoding -> NMS -> mAP calculation) is functioning correctly.*

## 🚀 How to Run

1. Clone the repository and install dependencies (`torch`, `torchvision`, `torchmetrics`, `numpy`).
2. Ensure you have the required proposal datasets (`train_data.json`, `test_data.json`, `rcnn_proposals_data.json`) in the same directory (not included in the repo due to size limits).
3. Run **`R_CNN.ipynb`** cell-by-cell to instantiate the dataset loaders, train the model across 10 epochs, and evaluate the final mAP score.

## 🛠️ Future Improvements

* **Unfreeze Backbone Layers:** Fine-tune `layer4` of the ResNet-18 backbone with a small learning rate (`1e-5`) to specialize the convolutional filters for Pascal VOC objects.
* **Loss Weighting:** Add a scaling multiplier (e.g., `5.0 * bbox_loss`) to balance the gradient magnitudes between the classification and regression heads.
* **Proposal Density:** Increase Selective Search proposals from 500 to 2,000 per image to raise the theoretical recall ceiling for small and occluded objects.
