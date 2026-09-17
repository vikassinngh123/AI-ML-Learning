# 🔍 03 - PyTorch Object Detection

Welcome to the **Object Detection** sub-module! This directory is dedicated to understanding and implementing the core mechanics of seminal object detection architectures using PyTorch. 

Rather than building every traditional computer vision algorithm from absolute scratch (e.g., manually coding Selective Search), the focus here is on implementing the **key deep learning concepts**, custom loss functions, and architectural designs that make these models work.

## 📂 Directory Contents

### `detection_utils.py`
The foundational math and utility script required for evaluating and filtering bounding box predictions.
- **Intersection over Union (IoU):** Calculates the overlap between predicted and ground-truth bounding boxes to measure accuracy.
- **Non-Max Suppression (NMS):** Cleans up overlapping bounding box predictions by filtering out lower-confidence duplicates for the same object.

## 🚀 Roadmap & Key Implementations

This folder will host implementations of the core mechanics behind major object detection architectures:

### 1. R-CNN (Regions with CNN features)
- **Focus:** Understanding the two-stage detector pipeline.
- **Key Concepts to Implement:** 
  - Using pre-computed region proposals (via tools like OpenCV's Selective Search).
  - Warping regions and passing them through a CNN feature extractor.
  - Implementing the final classification and bounding box regression heads.

### 2. YOLO-v1 (You Only Look Once)
- **Focus:** Understanding single-stage, grid-based object detection.
- **Key Concepts to Implement:** 
  - The $S \times S$ grid prediction formatting.
  - The custom YOLO multi-part loss function (coordinate loss, objectness score, no-object penalty, and class probabilities).
  - End-to-end training pipeline mapping images directly to bounding box tensors.

## 🛠️ Tech Stack & Concepts
- **Frameworks:** PyTorch (`torch`, `torchvision`), OpenCV (for traditional CV tasks like region proposals).
- **Core Math:** Bounding box coordinate transformations (midpoint to corners), intersection area calculation, tensor broadcasting.
