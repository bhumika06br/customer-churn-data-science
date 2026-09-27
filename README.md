# Customer Churn Prediction

A project-based Data Science learning project focused on understanding customer churn using Python, NumPy, Pandas, and Matplotlib.

This project is being developed step by step as part of my Data Science learning journey.

## 🎯 Project Goal

The goal of this project is to explore customer data, identify patterns associated with customer churn, and eventually build a machine learning model to predict whether a customer is likely to churn.

## 📊 Dataset

The dataset contains customer information such as:

- Customer ID
- Age
- Gender
- Tenure
- Usage Frequency
- Support Calls
- Payment Delay
- Subscription Type
- Contract Length
- Total Spend
- Last Interaction
- Churn

### Target Variable

`Churn`

- `0` → Customer did not churn
- `1` → Customer churned

The dataset is used for educational and project-based learning purposes.

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Git
- GitHub

## 📚 What I Have Learned So Far

### NumPy

- Creating NumPy arrays
- Calculating mean, minimum, maximum and sum
- Boolean masking
- Counting values using NumPy

### Pandas

- Loading CSV files
- Exploring DataFrames
- Checking shape, columns and data types
- Checking missing values
- Using `describe()`
- Using `value_counts()`
- Calculating percentages
- Using `groupby()`
- Calculating churn rates

### Data Visualization

- Creating bar charts using Matplotlib
- Comparing churn rates across categories
- Visualizing customer churn distribution

## 🔍 Exploratory Data Analysis

Some of the questions explored so far:

1. What is the overall distribution of churn?
2. What is the churn rate for different subscription types?
3. What is the churn rate for different contract lengths?
4. Do churned customers have more support calls?
5. Do churned customers have higher payment delays?
6. Do churned customers have different total spending patterns?

### Initial Findings

In this dataset:

- Churned customers have a higher average number of support calls.
- Churned customers have a higher average payment delay.
- Churned customers have a lower average total spend.
- Churn rates differ across subscription types and contract lengths.

These observations represent associations in the dataset and do not establish causation.

## 📁 Project Structure

```text
customer_churn_project/
│
├── data/
│   └── customer_churn_dataset-testing-master.csv
│
├── src/
│   ├── 01_numpy_basics.py
│   └── 01_data_exploration.py
│
├── .gitignore
└── README.md