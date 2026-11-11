<div align="center">

# 💬 Review Sentiment Analysis App (WIP)
### *NLP API powered by FastAPI, Hugging Face, and Supabase*

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)

**An in-development Natural Language Processing application. Currently, this project features a RESTful backend API that loads a fine-tuned GPT-2 sequence classification model to analyze customer review sentiments, securely logging the results to a cloud-based Supabase database.**

</div>

---

## 🏗️ Current Architecture

*   **Machine Learning Inference:** Utilizes the Hugging Face `pipeline` API to load a locally saved, fine-tuned GPT-2 model on server startup. Features graceful degradation to keep the API alive even if model loading fails.
*   **FastAPI Backend (`/backend`):** Exposes endpoints to receive customer reviews, run them through the NLP model, and structure the data.
*   **Database (Supabase):** Currently uses the `supabase-py` client to log reviews, star ratings, and predicted sentiments (Positive, Negative, Neutral) to a cloud PostgreSQL instance.

---

## 📂 Repository Structure

```text
review-sentiment-app/
├── backend/
│   └── api.py                 # FastAPI server, ML inference pipeline, and Supabase connection
└── README.md                  # Project documentation
```
*(Note: The fine-tuned model weights are expected in a local `sentiment_model/` directory, which is excluded from version control).*

---

## 🚀 Local Quick Start (Backend)

**1. Install Dependencies:**
```bash
pip install fastapi uvicorn supabase transformers pydantic torch
```

**2. Add Model Weights:**
Extract your fine-tuned Hugging Face model and tokenizer files into a `backend/sentiment_model/` directory.

**3. Environment Variables:**
Export your Supabase credentials to your local environment:
```bash
export SUPABASE_URL="your_supabase_project_url"
export SUPABASE_KEY="your_supabase_anon_key"
```
*(On Windows PowerShell, use `$env:SUPABASE_URL="your_url"`).*

**4. Start the API Server:**
Navigate to the `backend` directory and run:
```bash
uvicorn api:app --reload
```
*The API will be available at `http://localhost:8000`. You can test the endpoints interactively via the automatic Swagger UI at `http://localhost:8000/docs`.*

---

## 🗺️ Upcoming Roadmap

*   **Frontend Development:** Build a decoupled Streamlit interface with a customer-facing submission form and an admin data visualization dashboard.
*   **Database Migration:** Transition the database layer from cloud Supabase to a local, containerized PostgreSQL instance using `psycopg2`.

---

<div align="center">
<b>Built by <a href="https://github.com/vikassinngh123">Vikas Singh</a></b>
</div>