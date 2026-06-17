# Machine Learning & Predictive Modeling

This folder contains end-to-end **Supervised Machine Learning** projects focusing on Regression, Classification, Feature Selection, Hyperparameter Tuning, and production-grade Pipeline Architecture. The workflows transition from exploratory modeling to hyper-tuned ensembles, interactive model user interfaces, and model serialization.

---

## 🛠️ Tech Stack & Advanced ML Concepts

* **Core Modeling Ecosystem:** `scikit-learn` (Linear Models, Tree Ensembles, Preprocessing, Feature Selection, Evaluation Metrics)
* **Algorithms Evaluated:** Linear Regression, Ridge, Lasso, Decision Tree, Random Forest, Gradient Boosting, Support Vector Regression (SVR), K-Nearest Neighbors (KNN)
* **Optimization Frameworks:** Comprehensive Grid Search (`GridSearchCV`) and efficient randomized tuning pipelines (`RandomizedSearchCV`).
* **Key Frameworks Mastered:** Custom Class Weighting, Temporal Train/Test Splitting (Data Leakage Mitigation), Occam's Razor Performance Optimization, Multi-Algorithm Benchmarking, Pipeline Serialization.

---

## 📂 Projects Directory

### 🏡 1. California Housing Price Prediction ([California_Housing_Prediction.ipynb](https://github.com/vikassinngh123/AI-ML-Learning/blob/main/Machine-Learning/California_Housing_Prediction.ipynb))
A comprehensive regression framework built to predict median house values using geospatial, demographic, and economic features.
* **Feature Engineering & Geospatial EDA:**
  * Engineered geospatial scatter maps matching California's geography using Plotly (`template='plotly_dark'`), sizing data clusters by local population and coloring by true value.
  * Conducted deep correlation analysis mapping `median_income` ($r \approx 0.69$) as the primary valuation driver.
  * Applied `OneHotEncoder` to decode proximity variables safely.
* **Iterative Modeling Strategy:**
  * *Baseline:* Linear Regression (Test RMSE: ~$69,297$)
  * *Ensemble Upgrade:* Random Forest Regressor (Test RMSE: ~$48,922$)
  * *Champion Model:* `HistGradientBoostingRegressor` with tuned depth constraints (Test RMSE: ~$47,084$)
* **Interactive Admin Prototype:** Integrated a full graphical UI using `ipywidgets` (`FloatText`, `IntSlider`, `Dropdown`, `Button`) allowing end-users to compute instant, real-time valuation estimates using the serialized gradient boosting backend.

### 🌧️ 2. Australia Rain Prediction System ([Logistic_Regression_Weather.ipynb](https://github.com/vikassinngh123/AI-ML-Learning/blob/main/Machine-Learning/Logistic_Regression_Weather.ipynb))
A binary classification project optimized to resolve severe class imbalance and predict whether it will rain tomorrow based on country-wide meteorological features.
* **Data Leakage Mitigation & Imputation:**
  * Implemented strict temporal splitting (`train < 2015` and `test >= 2015`) to ensure real-world predictive validity.
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

### 🏆 4. Kaggle Advanced House Prices Regression ([Kaggle_House_Prices_Regression.ipynb](https://github.com/vikassinngh123/AI-ML-Learning/blob/main/Machine-Learning/Kaggle_House_Prices_Regression.ipynb))
An extensive, multi-model optimization benchmark leveraging the Ames Housing Dataset to predict house valuations for an active global Kaggle competition leaderboard.
* **Advanced Pipeline Preprocessing:**
  * **Numerical Pipeline:** Handled dense structural null spaces using a median `SimpleImputer` paired with flexible scaling mechanisms (`StandardScaler` vs. `MinMaxScaler`).
  * **Categorical Pipeline:** Injected a most-frequent `SimpleImputer` baseline combined with an unknown-ignoring `OneHotEncoder` setup to dynamically expand feature categories safely.
* **Multi-Model Tournament Benchmarking:** Evaluated 8 separate machine learning architectures under identical cross-validation conditions to optimize hyperparameter footprints:
  * Linear Regression (CV $R^2$: `0.7548`)
  * Ridge Regression (CV $R^2$: `0.8290`)
  * Lasso Regression (CV $R^2$: `0.8279`)
  * Decision Tree Regressor (CV $R^2$: `0.7071`)
  * K-Nearest Neighbors Regressor (CV $R^2$: `0.7916`)
  * Support Vector Regression (CV $R^2$: `0.6066`)
  * Random Forest Ensemble (`RandomizedSearchCV`, CV $R^2$: `0.8387`)
  * Gradient Boosting Regressor (`RandomizedSearchCV`, CV $R^2$: `0.8732`)
* **Advanced Ensemble Engineering (Champion Architecture):** * Combined the top 3 base estimators (Gradient Boosting, Random Forest, Ridge) into advanced **Voting** and **Stacking** regressors.
  * Extracted models into a top-level pipeline to process raw categorical text safely, utilizing `passthrough=True` with a `RidgeCV` meta-learner to dynamically weigh predictions against original structural features.
* **Ultimate Testing & Leaderboard Deployment:**
  * Tested the finalized **Stacking Ensemble Blueprint** against unseen testing data, successfully breaking the 90% accuracy barrier with a **Validation $R^2$ Score of 0.9074**.
  * Programmatically parsed Kaggle's hidden evaluation vectors (`test.csv`) to generate and export an official leaderboard submission (`submission_stacking_ensemble.csv`).
  * **Global Leaderboard Result:** Achieved an official **RMSLE score of 0.1402**, placing the model competitively in the global rankings!

### 📈 5. Kaggle US Stock Returns Prediction ([US_Stock_Returns_kaggel_comp.ipynb](https://github.com/vikassinngh123/AI-ML-Learning/blob/main/Machine-Learning/US_Stock_Returns_kaggel_comp.ipynb))
An end-to-end machine learning pipeline predicting 1-year US stock market returns based on corporate fundamentals for a Kaggle competition.
* **High-Cardinality Categorical Engineering:**
  * Bypassed standard One-Hot Encoding for 1,700+ unique stock tickers to prevent the "curse of dimensionality" and memory bloat.
  * Implemented `TargetEncoder` (with smoothing) from the `category_encoders` library to map historical return biases directly into a single, highly predictive dense column.
* **Custom Scikit-Learn Transformers:**
  * Built a custom `StockDateFeatureExtractor` class integrated directly at the head of the `scikit-learn` Pipeline.
  * Automatically parses raw text dates to extract financial quarters, calculate durations, and drop raw strings on the fly, ensuring zero pipeline crashes when passing untouched Kaggle test data (`test.csv`).
* **Baseline Strategy & Evaluation:**
  * Established a highly optimized **LightGBM (`LGBMRegressor`)** baseline submission to safely benchmark future ensemble and log-transformation experiments.
  * Generated an official Kaggle leaderboard submission (`Stock_submission_LGB.csv`), successfully evaluating the pipeline architecture against RMSE constraints.

---

## 🚀 How to Run These Notebooks

Ensure your python environment has all machine learning dependencies provisioned:

```bash
pip install numpy pandas matplotlib seaborn plotly sklearn ipywidgets joblib kagglehub pyarrow fastparquet notebook
