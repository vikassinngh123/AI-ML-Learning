# 🍔  Food-101 Classifier

Welcome to the **Food-101 Streamlit Application**! This repository hosts a live web application that uses a deep learning model to classify images of food into 101 different categories.

## 🚀 Live Demo
**Try the app here:** [Food-101 Classifier on Streamlit](https://food101-efficientnetb3.streamlit.app)

## 🧠 Model Details
* **Architecture:** `EfficientNet-B3` (Pretrained on ImageNet)
* **Custom Head:** A deep classification head (`1536 -> 256 -> 128 -> 101`) to map the extracted features to the 101 specific food classes.
* **Dataset:** Trained on the classic **Food-101 Dataset** (101,000 images).

## 📂 Directory Structure

This folder contains the complete deployment package:

* `food101_app.py`: The main Streamlit application script containing the frontend UI (Dark mode configured) and logic.
* `food101_utils.py`: Contains the core PyTorch inference pipeline, including model loading (via `@st.cache_resource`), image transformations, and the prediction function.
* `food101_classes.json`: A JSON map containing the 101 human-readable class names.
* `requirements.txt`: The dependency file specifically configured to download the **CPU-only** wheels of PyTorch to ensure it runs efficiently on Streamlit Community Cloud.

## 💻 How to Run Locally

If you want to run this application on your local machine, follow these steps:

1. **Clone the repository and navigate to this folder:**
   ```bash
   git clone [https://github.com/vikassinngh123/AI-ML-Learning.git](https://github.com/vikassinngh123/AI-ML-Learning.git)
   cd AI-ML-Learning/06-Deep-Learning/01-PyTorch/02-PyTorch-Computer-Vision/food101_streamlit_app
   ```

2. **Install the dependencies:**
   *(It is recommended to use a virtual environment)*
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run food101_app.py
   ```

4. **Open your browser:** The app will automatically open at `http://localhost:8501`.

## 🛠️ Tech Stack
* **Deep Learning Framework:** PyTorch (`torch`, `torchvision`)
* **Web Framework:** Streamlit
* **Image Processing:** Pillow (PIL)
