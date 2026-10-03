# 🔍 03 - PyTorch Object Detection

Welcome to the **Object Detection** sub-module! This directory is dedicated to understanding and implementing the core mechanics of seminal object detection architectures using PyTorch. 

Rather than building every traditional computer vision algorithm from absolute scratch (e.g., manually coding Selective Search), the focus here is on implementing the **key deep learning concepts**, custom loss functions, and architectural designs that make these models work.

---

## 📂 Directory Contents

### `01_R_CNN.ipynb`
A foundational notebook implementing the core pipeline of the R-CNN (Regions with CNN features) architecture.
- **Data Parsing:** Extracts and parses the Pascal VOC 2007 dataset for specific target classes (e.g., Person, Dog, Car).
- **Region Extraction:** Applies Selective Search to generate candidate region proposals and serializes coordinate metadata to JSON to optimize RAM usage.
- **Data Pipeline:** Implements a custom, lazy-loading PyTorch `Dataset` and `DataLoader` that dynamically crops, resizes, and applies ImageNet normalization to region tensors.
- **Target Assignment:** Maps proposed regions to ground-truth boxes using IoU thresholds to create balanced positive and negative (background) training samples.
- **Model Architecture:** Constructs a multi-task deep learning model using a headless pretrained ResNet-18 backbone with custom dense heads for classification and parameterized bounding box regression (coordinate deltas).

### `detection_utils.py`
The foundational math and utility script required for evaluating and filtering bounding box predictions.
- **Intersection over Union (IoU):** Calculates the overlap between predicted and ground-truth bounding boxes to measure accuracy.
- **Non-Max Suppression (NMS):** Cleans up overlapping bounding box predictions by filtering out lower-confidence duplicates for the same object.

---

## 🛠️ Tech Stack & Concepts
- **Frameworks:** PyTorch (`torch`, `torchvision`), OpenCV (for traditional CV tasks like region proposals).
- **Core Math:** Bounding box coordinate transformations (midpoint to corners), coordinate offsets ($t_x, t_y, t_w, t_h$), intersection area calculation, tensor broadcasting.
