# Machine Learning & Predictive Modeling

This folder contains end-to-end **Supervised Machine Learning** projects focusing on Regression, Classification, Feature Selection, Hyperparameter Tuning, and production-grade Pipeline Architecture. The workflows transition from exploratory modeling to hyper-tuned ensembles, interactive model user interfaces, and model serialization.

---

## 🛠️ Tech Stack & Advanced ML Concepts

* **Core Modeling Ecosystem:** `scikit-learn` (Linear Models, Tree Ensembles, Preprocessing, Feature Selection, Evaluation Metrics)
* **Algorithms Evaluated:** Linear Regression, Logistic Regression, Random Forest Regressor/Classifier, HistGradientBoostingRegressor
* **Production & UI Utilities:** `ipywidgets` (Interactive Dashboard Prototyping), `joblib` (Model Serialization/Deployment pipelines)
* **Key Frameworks Mastered:** Custom Class Weighting, Temporal Train/Test Splitting (Data Leakage Mitigation), Occam's Razor Performance Optimization, Pipeline Serialization.

---

## 📂 Projects Directory

### 🏡 1. California Housing Price Prediction ([California_Housing_Prediction.ipynb](https://github.com/vikassinngh123/AI-ML-Learning/blob/main/Machine-Learning/California_Housing_Prediction.ipynb))
A comprehensive regression framework built to predict median house values using geospatial, demographic, and economic features.
* **Feature Engineering & Geospatial EDA:** * Engineered geospatial scatter maps matching California's geography using Plotly (`template='plotly_dark'`), sizing data clusters by local population and coloring by true value.
    * Conducted deep correlation analysis mapping `median_income` ($r \approx 0.69$) as the primary valuation driver.
    * Applied `OneHotEncoder` to decode proximity variables safely.
* **Iterative Modeling Strategy:**
    * *Baseline:* Linear Regression (Test RMSE: ~$69,297$)
    * *Ensemble Upgrade:* Random Forest Regressor (Test RMSE: ~$48,922$)
    * *Champion Model:* `HistGradientBoostingRegressor` with tuned depth constraints (Test RMSE: ~$47,084$)
* **Interactive Admin Prototype:** Integrated a full graphical UI using `ipywidgets` (`FloatText`, `IntSlider`, `Dropdown`, `Button`) allowing end-users to compute instant, real-time valuation estimates using the serialized gradient boosting backend.

### 🌧️ 2. Australia Rain Prediction System ([Logistic_Regression_Weather.ipynb](https://github.com/vikassinngh123/AI-ML-Learning/blob/main/Machine-Learning/Logistic_Regression_Weather.ipynb))
A binary classification project optimized to resolve severe class imbalance and predict whether it will rain tomorrow based on country-wide meteorological features.
* **Data Leakage Mitigation & Imputation:** * Implemented strict temporal splitting (`train < 2015` and `test >= 2015`) to ensure real-world predictive validity.
    * Applied numeric `SimpleImputer` using median calculations and fit the `StandardScaler` strictly on training data prior to transforming test data.
* **Addressing Class Imbalance:**
    * *Raw Logistic Regression:* Delivered 84.3% accuracy but failed on recall due to severe false negatives (Type 2 Error).
    * *Balanced Logic:* Configured `class_weight='balanced'` and custom penalty matrices (`{'No': 0.95, 'Yes': 1.8}`) to strike the optimal mathematical trade-off, boosting target recall significantly to 63.8%.
* **Feature Selection & Ensemble Pruning:**
    * Tuned a massive `RandomForestClassifier` (500 estimators, max depth 20) to extract feature importances.
    * Applied `SelectFromModel` with a strict variance threshold to discard non-informative wind and location columns, shrinking data dimensionality without losing accuracy.
* **Operational Conclusion:** Honored **Occam's Razor**. Since the heavy Random Forest barely outperformed the optimized linear model (~83.9% vs ~83.1%), Logistic Regression was selected as the superior production model due to zero computational latency and instant training capabilities.

### ⚙️ 3. Production Rain Prediction Pipeline ([Weather_Logistic_Pipeline.ipynb](https://github.com/vikassinngh123/AI-ML-Learning/blob/main/Machine-Learning/Weather_Logistic_Pipeline.ipynb))
Refactoring the exploratory weather analysis workspace into clean, reproducible software patterns.
* **Pipeline Architecture:** Implemented an end-to-end `scikit-learn` Pipeline object that seamlessly strings together data imputation, scaling, categorical one-hot encoding, and the final optimized classifier.
* **Model Serialization:** Utilized `joblib` to export the finalized training pipeline object into compact binaries, allowing the entire model blueprint to be stored, imported, and deployed instantly in separate production scripts or web applications.

---

## 🚀 How to Run These Notebooks

Ensure your python environment has all machine learning dependencies provisioned:

```bash
pip install numpy pandas matplotlib seaborn plotly sklearn ipywidgets joblib kagglehub pyarrow fastparquet notebook
