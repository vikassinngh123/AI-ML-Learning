#  Module 05: Machine Learning

Welcome to the Machine Learning module! This directory contains end-to-end predictive modeling workflows. The focus here is on writing production-ready code, building custom data pipelines, and optimizing advanced algorithms to solve complex, real-world datasets.

---

##  01 - Supervised Learning
*Learning from labeled data to predict continuous values (Regression) or categorical outcomes (Classification).*

This folder contains notebooks where models are trained to predict a specific target variable. 

**Featured Projects:**
* **🏠 Kaggle Advanced House Prices:** Implemented advanced feature engineering, handled missing data, and built a powerful Stacking Ensemble.
* **📈 US Stock Returns Prediction:** Financial forecasting using custom `StockDateFeatureExtractor` pipelines, target encoding for high-cardinality tickers, and a highly tuned LightGBM baseline.
* **☀️ Weather Prediction Pipelines:** End-to-end Logistic Regression classification focusing on custom Scikit-Learn transformers and robust data cleaning.
* **📍 California Housing:** Core regression techniques and predictive modeling fundamentals.

---

##  02 - Unsupervised Learning [Coming Soon]
*Discovering hidden patterns, groupings, and structures in unlabeled data.*

> **Status:** *Currently setting up the environment and hunting for the perfect datasets!*

This upcoming subfolder will focus on exploring data without target variables. Planned topics include:
* **Dimensionality Reduction:** Compressing high-dimensional datasets using PCA (Principal Component Analysis) and t-SNE to visualize complex data in 2D/3D.
* **Clustering:** Grouping similar data points together using K-Means, DBSCAN, and Hierarchical Clustering for customer segmentation and pattern recognition.
* **Anomaly Detection:** Identifying outliers and unusual data points in large datasets.

---

##  Key Techniques & Architecture

Across all projects in this module, the following engineering best practices are strictly applied:

* **Custom Scikit-Learn Pipelines:** Building modular `BaseEstimator` and `TransformerMixin` classes to prevent data leakage during cross-validation.
* **Hyperparameter Tuning:** Utilizing `GridSearchCV` and `RandomizedSearchCV` to find the absolute mathematical optimum for model parameters.
* **Ensemble Methods:** Combining multiple weak learners into strong models using Bagging, Boosting (XGBoost, LightGBM), and Stacking.
* **Robust Evaluation:** Using appropriate metrics (RMSE, ROC-AUC, F1-Score) based on data distribution and class balance.
