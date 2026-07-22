# Module 05: Machine Learning

Welcome to the Machine Learning module! This directory contains end-to-end predictive modeling workflows. The focus here is on writing production-ready code, building custom data pipelines, and optimizing advanced algorithms to solve complex, real-world datasets.

## 📁 Sub-Modules & Projects

### 01 - Supervised Learning
*Learning from labeled data to predict continuous values (Regression) or categorical outcomes (Classification).*

* **🏠 Kaggle Advanced House Prices:** Implemented advanced feature engineering, handled missing data, and built a powerful Stacking Ensemble.
* **📈 US Stock Returns Prediction:** Financial forecasting using custom `StockDateFeatureExtractor` pipelines, target encoding for high-cardinality tickers, and a highly tuned LightGBM baseline.
* **☀️ Weather Prediction Pipelines:** End-to-end Logistic Regression classification focusing on custom Scikit-Learn transformers and robust data cleaning.
* **📍 California Housing:** Core regression techniques and predictive modeling fundamentals.

---

### 02 - Unsupervised Learning
*Discovering hidden patterns, groupings, and structures in unlabeled data without predefined target variables.*

* **🛍️ Customer Segmentation (Mall Customers):** Grouping retail customers using a 4-dimensional K-Means model (Age, Gender, Annual Income, Spending Score). Includes a comparative analysis highlighting why DBSCAN struggles with varying cluster densities, and implements **PCA** to reduce 4D segments into 2D for visualization.
* **🔢 Dimensionality Reduction (MNIST Digits):** Compressing 784-dimensional handwritten digits. Features an in-depth comparative study between linear reduction (**PCA**) and non-linear neighborhood mapping (**t-SNE**), demonstrating why linear methods struggle with complex feature spaces.

---

## 🛠️ Key Techniques & Architecture

Across all projects in this module, the following engineering best practices are strictly applied:

* **Custom Scikit-Learn Pipelines:** Building modular `BaseEstimator` and `TransformerMixin` classes to prevent data leakage during cross-validation.
* **Hyperparameter Tuning:** Utilizing `GridSearchCV` and `RandomizedSearchCV` to find the mathematical optimum for model parameters.
* **Ensemble Methods:** Combining multiple weak learners using Bagging, Boosting (XGBoost, LightGBM), and Stacking.
* **Dimensionality Reduction & Clustering:** Uncovering structures with PCA, t-SNE, K-Means, and DBSCAN.
* **Robust Evaluation:** Using appropriate evaluation metrics (RMSE, ROC-AUC, Silhouette Score, F1-Score) tailored to data distribution and class balance.
