# 04. Data Analysis with Pandas & Visualization

This folder houses a collection of comprehensive, end-to-end data analysis projects focused on **Data Cleaning, Feature Manipulation, and Advanced Visualizations**. These notebooks demonstrate how to transform messy, real-world data into structured, actionable insights using Python's core data science ecosystem.

---

## 🛠️ Tech Stack & Libraries Used

* **Data Manipulation & Processing:** `pandas` (DataFrames, Merges, Queries, Explodes), `numpy`
* **Static Visualization Architecture:** `matplotlib.pyplot`, `seaborn` (for statistical distributions, line overlays, and publication-ready graphs)
* **Interactive Visualization Dashboards:** `plotly.express` (utilizing advanced dark-themed layout configurations via `template='plotly_dark'`)

---

## 📂 Projects Directory

### 1. 🍟 Chips Experimental Practice ([01_Chips_Experimental_Practice.ipynb](https://github.com/vikassinngh123/AI-ML-Learning/blob/main/04-Pandas/01_Chips_Experimental_Practice.ipynb))
* **Core Concepts:** Data transformation, sequential grouping, and time-series feature alignment.
* **Key Implementations:** * Applying **rolling windows** to track business performance moving averages over distinct spans.
  * Constructing localized **sales ranking systems** grouped by unique data partitions.
  * Cleaning product experimental metrics and normalizing transactional anomalies.

### 🏅 2. 120 Years of Olympic History EDA ([02_Olympics_History_EDA.ipynb](https://github.com/vikassinngh123/AI-ML-Learning/blob/main/04-Pandas/02_Olympics_History_EDA.ipynb))
An extensive exploratory analysis combining historical biographies and competition result tables (`bios.csv` + `results.parquet`) to track global and domestic athletic profiles from 1896 to 2022.
* **Advanced Data Cleaning & Normalization:**
  * **Geopolitical Consolidation:** Standardized historically shifting regimes into unified analytical categories (e.g., mapping `Soviet Union` ➡️ `Russian Federation` and `East Germany` ➡️ `Germany`).
  * **State Filtering:** Handled massive structural null inputs across individual physical dimensions (`height_cm`, `weight_kg`) and competition variables (`medal`).
* **Detailed Analytical Layouts:**
  * **Domestic Regional Breakdown:** Filtered unique participants natively from India (`NOC == "India" & born_country == "IND"`) to visualize distribution patterns across Indian states and territories.
  * **Gender & Age Trajectories:** Modeled demographic timelines over a century of games, pairing line graphs and multi-variable box/distribution plots to track historical shifts in peak competitive maturity.
  * **The "Host Bump" Metric:** Constructed an integrated chart using unique star annotations (`marker='*'`) and localized text callouts to map the monumental gold medal spikes experienced by host nations during home-soil events.

### 💻 3. Stack Overflow Developer Survey Analysis ([03_StackOverflow_Survey_Analysis.ipynb](https://github.com/vikassinngh123/AI-ML-Learning/blob/main/04-Pandas/03_StackOverflow_Survey_Analysis.ipynb))
An analytical dive into international developer career profiles, income benchmarks, and architectural choices utilizing annual multi-variable survey records.
* **Advanced Data Cleaning & Normalization:**
  * **String Decomposition:** Parsed semicolon-separated data blocks (`"Python;JavaScript;SQL"`) by engineering complex string splitting pipelines coupled with `.explode()` actions to isolate specific technical choices.
  * **Categorical Feature Compression:** Compressed verbose text categories into standardized strings (e.g., mapping lengthy educational degrees into concise tags like `Master's` or `Bachelor's`).
  * **Outlier Eradication:** Set definitive boundary constraints on compensation tracking columns (`ConvertedCompYearly`) to isolate clear salary patterns from extreme statistical distortion.
* **Detailed Analytical Layouts (Plotly Dark Architecture):**
  * **Salary Dynamics vs. Experience:** Tracked multi-line average compensation growth patterns across 0 to 25 experience ranges, comparing regional market dynamics between the USA, India, and Global baseline metrics.
  * **Market Adoption Matrix:** Built multi-dimensional interactive scatter plots mapping developer counts directly against average salaries to discover language popularity vs. true market value.
  * **Structural Income Distribution:** Leveraged advanced interactive `px.violin` charts to expose internal salary variance across educational thresholds (`EdLevel`), remote flexibility configurations (`RemoteWork`), and back-end inventory implementations.

---

## 🚀 How to Run These Notebooks

Ensure your environment is properly provisioned with the analytical software stack:

```bash
pip install pandas numpy matplotlib seaborn plotly pyarrow fastparquet notebook
