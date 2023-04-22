# Student Performance Regression Project

## This end to end project uses regression analysis to explore the relationship between various factors and student performance in a dataset of student records. The goal is to develop a regression model that can accurately predict student grades based on selected features.

## Dataset

The dataset used for this project contains information about student demographics, st	udy habits, and performance in various subjects. The dataset includes the following variables:

* gender: Student gender (binary).
* race/ethnicity: Student race/ethnicity (categorical).
* parental level of education: Parental education level (categorical).
* lunch: Whether the student receives free/reduced lunch (binary).
* test preparation course: Whether the student completed a test * preparation course (binary).
* math score: Student score in math (continuous).
* reading score: Student score in reading (continuous).
* writing score: Student score in writing (continuous).

## EDA

### The following steps were taken in the analysis:
1- check column data type.
2- check missing values.
3- check duplication drop if found.
4- get unique values for each categorical feature.
5- get realtion between total, average score and rest features.
6- visulize realtion between features to understand it will.

## Preoaring
- Apply oneHotEncoder on categorical features ('gender', 'race/ethnicity',  'parental level of education', 'lunch','test preparation course')
- Apply StandardScaler ('reading score', 'writing score')

## Training & Testing 
Model selection and development using various regression techniques, such as Linear Regression, Lasso, Ridge, K-Neighbors Regressor, Decision Tree, Random Forest Regressor, XGBRRegressor, CatBoostiong Regressor, and AdaBoost Regressor.
Model evaluation using metrics such as Root Mean Squared Error, Mean Absolute Error, and R2 Score.
