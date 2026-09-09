# 🌿 Natural Image Classifier - Streamlit App

This folder contains the front-end interface and inference engine for the **Natural Image Classifier**. The application is built using Streamlit and allows users to upload natural landscape images to get real-time predictions using PyTorch models.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vikas-landscape-classifier.streamlit.app/)

## 📂 Folder Structure

*   **`app.py`**: The main Streamlit application file containing the UI layout, file uploader logic, and result rendering.
*   **`utils.py`**: A modular script containing the model architecture classes, Streamlit caching functions (`@st.cache_resource`), and image transformation pipelines.
*   **`requirements.txt`**: The list of Python dependencies required to run the app in the cloud, specifically configured for lightweight CPU inference.

## ⚙️ How to Run Locally

If you want to run this application on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vikassinngh123/AI-ML-Learning.git
   ```
2. **Navigate to the app directory:**
   ```bash
   cd AI-ML-Learning/06-Deep-Learning/01-PyTorch/02-PyTorch-Computer-Vision/streamlit_app
   ```
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Launch the application:**
   ```bash
   streamlit run app.py
   ```

*(Note: The heavy `.pth` model weights are hosted via GitHub Releases to bypass standard repository size limits. The `utils.py` script is configured to automatically download these weights to your local machine the very first time you boot the app!)*

## Models Available

The app compares two different architectures:
*   **Custom CNN**: A convolutional neural network built and trained entirely from scratch in PyTorch.
*   **ResNet-18**: A robust transfer learning model, fine-tuned for high-accuracy landscape classification.
