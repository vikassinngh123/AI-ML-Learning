<div align="center">

# 🗣️ Modern NLP with PyTorch & Hugging Face
### *Applied Natural Language Processing and LLM Fine-Tuning*

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-FFD21E?style=for-the-badge&logoColor=black)](https://huggingface.co/)

**A progressive learning repository focused on modern Natural Language Processing (NLP). This module applies foundational PyTorch knowledge to the Transformer architecture, leveraging the Hugging Face ecosystem for tokenization, pre-trained inference, and custom LLM fine-tuning.**

</div>

---

## 📂 Repository Structure

| Notebook | Description | Key Concepts Covered |
| :--- | :--- | :--- |
| **`01_huggingface_pipelines_basics.ipynb`** | Introduction to the Hugging Face `transformers` library via high-level pipelines. | Sentiment Analysis (DistilBERT), Text Generation (GPT-2), Context-based Q&A (SmolLM3), GPU device mapping. |
| **`02_gpt2_sentiment_finetuning.ipynb`** | End-to-end fine-tuning of GPT-2 for sequence (sentiment) classification. | `AutoTokenizer` (padding/truncation), Hugging Face `datasets` API, `Trainer` API, gradient accumulation, model exporting. |

---

## 🧠 Core Technologies & Methodologies

*   **Tokenization & Embeddings:** Converting raw text into integer sequences and managing padding/truncation for fixed-length tensor operations.
*   **Transformer Architectures:** Utilizing pre-trained Decoder-only (GPT variants) and Encoder-only models for sequence generation and classification.
*   **Transfer Learning in NLP:** Taking foundation models and fine-tuning classification heads on custom text datasets (e.g., `mteb/tweet_sentiment_extraction`).
*   **Hardware Optimization:** Managing batch sizes, gradient accumulation steps, and CUDA memory limits during LLM training.

---

## 🚀 Upcoming Roadmap
*   Vector Databases and Dense Text Embeddings.
*   Retrieval-Augmented Generation (RAG) for document-based Q&A.
*   Deploying fine-tuned NLP models via **FastAPI** backends and **Streamlit** frontends.

---

<div align="center">
<b>Built by <a href="https://github.com/vikassinngh123">Vikas Singh</a></b>
</div>
