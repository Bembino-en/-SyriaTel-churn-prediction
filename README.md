# # Syria Telecom Customer Churn Prediction Analysis

## Introduction
Customer churn prediction is critical for telecommunications companies to retain valuable customers and reduce acquisition costs. This project analyzes customer behavior patterns to predict churn using machine learning techniques. By identifying at-risk customers early, telecom providers can implement targeted retention strategies.

## Dataset
**Source:** [Kaggle - Churn in Telecom's Dataset](https://www.kaggle.com/datasets/becksddf/churn-in-telecoms-dataset)  
**Description:** Contains 3,333 customer records with 21 features including:
- Account information (`account length`, `area code`)
- Service plans (`international plan`, `voice mail plan`)
- Usage patterns (day, evening, night, international minutes/charges)
- Customer service interactions (`customer service calls`)
- Target variable: `churn` (binary: Yes/No)

**Key Characteristics:**
- ⚠️ **Class imbalance**: Only 14.5% churn rate
- 📊 **Feature types**: Mix of numerical and categorical variables
- ✅ **Completeness**: No missing values

## Project Objectives
1. Perform exploratory data analysis (EDA) to uncover churn patterns
2. Build predictive models:
   - Logistic Regression (baseline)
   - Untuned Decision Tree
   - Hyperparameter-tuned Decision Tree
3. Evaluate model performance using appropriate metrics
4. Identify key drivers of customer churn

## Analysis Workflow
```mermaid
    A[Data Loading] --> B[Exploratory Data Analysis]
    B --> C[Data Preprocessing]
    C --> D[Model Building]
    D --> E[Model Evaluation]
    E --> F[Feature Importance]
    F --> G[Conclusions & Recommendations]