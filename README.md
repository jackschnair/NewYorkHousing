# New York Housing Predictor
Final Project for CS539 Machine Learning <br>
By Jack Schnair


** MAKE SURE TO SPELL CHECK ALL THIS COPYING FROM GOOGLE DOCK **
# Overview

Give an overview of the project, the data, and the results

# Summary

Whether you're looking to buy or sell, the most common approach to evaluating properties is using a real estate agent. I am to create a model that will allow homeowners or buyers to evalutate the market and come to their own conclusions. My project takes a dataset of properties in New York City and uses machine learning to assess the value of a property based on the property type, area of New York, number of bedrooms and number of bathrooms. There are multiple regression models useful for this problem such as linear regression and random forest regression, but catboost has prooved the most accurate due to it's built in functionality to work with categorical data. 

# Project Description:

## Motivation
When searching for a reasearch problem, I browsed many datasets and the ones that caught my eye the most were the real estate ones. The tangibility and relevance of realestate as something I can see in the real world is appealing.
Real estate has been on my mind recently as I'm getting to an age where many of my peers are interesting in buying a property of their own. 
I am currently renting an apartment and am curious about the possibilities of one day buying property when I am financially stable enough. 
Knowing more about the market and determining what factors more prominantly impact the price of housing will make me more prepared when I reach a point in life when I'm ready to buy property.

## Goals

My primary objective is to predict the price of a house based on some of it's features such as square footage, location, number of bedrooms and number of bathrooms. 

However, there are other questions I've gotten curious about as I've explored the dataset. 
Determining which features of a property impact the price most directly would be benificial for homeowners or real estate investors because they can focus on which features will gain them the most profit. 
Perhaps houses in a certain town sell for much higher when they have more bedrooms due to the amount of families that want to live there as opposed to single people. 
A model that could determine that the number of bedrooms directly coorilate to how much a property sells for would be useful information. 
With it, a developer could determine if it's cost effective to have a floor plan with an additional bedroom or not.

Another question that can be answered is if we can classify where a buyer should look for property based on their list of criteria. 
For instance, if a buyer wants a two bedroom condo but can only afford something in the 300,000 - 400,000 range, what town should they look in?
This would require me to additionally implement a classification model using the same dataset, but changing my dependent variable to location instead of price.

## Dataset

I originally used [real estate data collected by the state of Connecticut](https://catalog.data.gov/dataset/real-estate-sales-2001-2018) as my dataset. It is a comprehensive collection of real estate records in Connecticut put together by the government. I found that the data provided in the original dataset was limiting to the scope of my project. I thought that I would be able to get more quality information from the data, but in reality, there are only about 3 dependent variables that matter (Town, Date sold, and property type). After doing some exploratory data analysis, I determined that I would need more relevant infomration such as square footage, the number of bedrooms or bathrooms. 

I searched for a relevant dataset that would fit my needs while keeping my proposed research question, eventually finding a [New York Housing Market dataset](https://www.kaggle.com/datasets/nelgiriyewithana/new-york-housing-market).
I chose this dataset because it is similar to the Connecticut one in the sense that it a localized real estate dataset. However, what makes it more applicable are the independent variables such as square footage, bedrooms, bathrooms, and locality within the city. 
From this dataset, I am able to identify trends in the market and reasonably predict what properties will sell for based on its location, property type, square footage, bedrooms and bathrooms compared to other similar properties. The unfortunate downside to this dataset is it's small size of just under 5,000 records, but I'm willing to sacrafice quantity for quality.

Ultimately the data I use looks like this: 
|  | Type | Price | Beds | Bath | Property sqft | Sublocality
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 0 | Condo for sale | 315000 | 2 | 2 | 1400.00 | Manhattan |
| 2 | House for sale | 260000 | 4 | 2 | 2015.00 | Richmond County |
| 3 | Condo for sale | 69000  | 3 | 1 | 445.00 | New York |
| 5 | House for sale | 690000 | 5 | 2 | 4004.00 | Kings County |
| 6 | Condo for sale | 899500 | 2 | 2 | 2184.20 | New York |
| ... | ... | ... | ... | ... | ... | ... |
| 4796 | Co-op for sale | 599000 | 1 | 1 | 2184.20 | New York |
| 4797 | Co-op for sale | 245000 | 1 | 1 | 2184.20 | Queens |
| 4798 | Co-op for sale | 1275000 | 1 | 1 | 2184.20 | New York |
| 4799 | Condo for sale | 598125 | 2 | 1 | 655.00 | Queens |
| 4800 | Co-op for sale | 349000 | 1 | 1 | 750.00 | Brooklyn |


# Methods

## One-Hot Encoding

In order to use categorical values in a regression problem, the dataset will need to be transformed using one-hot encoding. 
This method takes categorical values in a column and creates a separate column for each, marked 1 if true and 0 if false.
Pandas has a built in function to easily do this. <br>

`encoded = pd.get_dummies(df, columns=['TYPE', 'SUBLOCALITY'], drop_first=True)`

<br>This encoded dataset now has 5 additional columns for each value that was in TYPE and 7 additional columsn for each value in SUBLOCALITY. 
This brings the total from 6 to 16, increasing the size of the dataset while making it compatible with regression models. 

## SMOTE (Not Used)

Throughout the span of this project I have posted on the class discussion board with every milestone, often mentioning problems with my dataset.
When I switched to my current New York Housing dataset my problem became the small size of my dataset.
It was suggested that I try SMOTE (Synthetic Minority Over-sampling Technique) to remedy the small size of the dataset.
I gave it a shot and even tired SMOTENC for my categorical data, but had poor results.
I then thought about why this would be and realized that oversampling doesn't really make sense for a regression problem.
The point of minority oversampling is to make up for a size disperity in a classification problem.
Not only does it not make sense to do for regression, but it could actually overfit the data if the synthetic data is too similar to what is already there.
Unfortunately I'm not sure there is a solution to a small dataset when doing a regression problem.
The best bet is probably finding a more appropriate model or using feature engineering to improve performance.

## GridSearchCV

When choosing the best model for a problem it's not only important to choose the modle itself, but also the parameters used in it. GridSearchCV can be used to tune a model's parameters by performing cross validation on all the different combinations of parameters. Once the most accurate combination is found, the user can get the model and parameters for future use. <br>

Example of GridSearchCV being used on a Random Forest model:
```
rf = RandomForestRegressor(random_state=12)

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
    'bootstrap': [True, False]
}

grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)

grid_search.fit(x_train, y_train)

best_params = grid_search.best_params_
```
Fits 5 folds for each of 72 candidates, totalling 360 fits.<br>
Best Parameters: {'bootstrap': True, 'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 200}

## Model Results
Describe the methods used fro the data analysis

| Model | Cross Fold Validation Score |
| ----------- | ----------- |
| Linear Regression        | 0.5032 |
| Random Forest Regression | 0.6547 |
| Ridge Forest Regression  | 0.5034 |
| Lasso Regression         | 0.5033 |
| CatBoost Regression      | 0.6670 |


# Conclusion

A final section that summarizes the results and conclusions, including any relevant figures/visualizations

(Probably going to be my shiny app)
