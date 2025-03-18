# Project Overview

**Title**
A Comprehensive Analysis and Machine Learning Market Sales Prediction Model with Deployment

**Objective**
Develop a machine learning regression model to predict market sales using historical data. The goal is to generate actionable insights for business planning, inventory management, and marketing strategy.

**Scope:**  

- **Data Cleaning and Preprocessing:**  
  Address missing values, standardize column names, and ensure correct data types.
- **Exploratory Data Analysis (EDA):**  
  Visualize trends and relationships among variables to understand factors influencing market sales (unit price).
- **Modeling:**  
  Build and compare multiple regression models (e.g., Linear Regression, Decision Tree, Random Forest, and Gradient Boosting) to predict market sales.
- **Deployment:**  
  Create an interactive web application using Streamlit to deploy the best performing model, allowing users to input feature values and obtain life expectancy predictions.

## Business Problem

• Forecasting market sales can help businesses better allocate resources, adjust inventory levels,
and design effective marketing campaigns.
• Understanding the key factors driving sales will also empower decision-makers to plan for future growth.

## About Dataset

### Context

The Supermarket Sales Dataset provides a comprehensive overview of supermarket transactions, tracking details such as product categories, unit prices, quantities sold, and gross income. It also includes customer demographics, such as gender, payment method, and membership type. This dataset is ideal for analyzing sales trends, customer behavior, and revenue performance, offering insights to optimize promotions and product strategies.

### Column Descriptions

1. Invoice ID: A unique identifier for each transaction.
2. Branch: The specific supermarket branch (e.g., A, B, C).
3. City: The city where the branch is located.
4. Customer Type: Indicates if the customer is a "Member" or "Normal."
5. Gender: Customer's gender for demographic insights.
6. Product Line: Product category (e.g., Groceries, Clothing).
7. Unit Price: Price per product unit.
8. Quantity: Units bought in a transaction.
9. Tax (5%): Tax amount (5% of the total before tax).
10. Total: Total paid, including tax.

## Methodology

1. **Data Cleaning and Imputation:**  
   The project begins with cleaning the dataset by standardizing column names, converting data types.

2. **Exploratory Data Analysis (EDA):**  
   Various plots (histograms, heatmaps, barplot, pie plot ) are used to understand the distribution of unit price and the relationships among the predictor variables.

3. **Feature Engineering:**  
   - Categorical variables such as **Product line, City, Branch, Customer Type** are encoded.
   - Other numeric variables are standardized to ensure that models perform optimally.

4. **Model Development:**  
   Multiple regression models, including Random Forest (the primary model), are trained to predict market sales. Their performance is evaluated using metrics like Mean Squared Error (MSE) and R-squared.

5. **Deployment:**  
   The final model is deployed using Streamlit, allowing end-users to interact with the model by inputting various market indicators and receiving market sales predictions in real time.
