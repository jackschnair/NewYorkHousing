# New York Housing Predictor
Final Project for CS539 Machine Learning <br>
By Jack Schnair

## Overview

Give an overview of the project, the data, and the results

## Summary

Whether you're looking to buy or sell, the most common approach to evaluating properties is using a real estate agent. I am to create a model that will allow homeowners or buyers to evalutate the market and come to their own conclusions. My project takes a dataset of properties in New York City and uses machine learning to assess the value of a property based on the property type, area of New York, number of bedrooms and number of bathrooms. There are multiple regression models useful for this problem such as linear regression and random forest regression, but catboost has prooved the most accurate due to it's built in functionality to work with categorical data. 

## Project Description:

- First, describe the motivation for the project

- Next, describe what you intended to discover, possibly as a list of aims

# Dataset

I originally used [real estate data collected by the state of Connecticut](https://catalog.data.gov/dataset/real-estate-sales-2001-2018) as my dataset. It is a comprehensive collection of real estate records in Connecticut put together by the government. I found that the data provided in the original dataset was limiting to the scope of my project. I thought that I would be able to get more quality information from the data, but in reality, there are only about 3 dependent variables that matter (Town, Date sold, and property type). After doing some exploratory data analysis, I determined that I would need more relevant infomration such as square footage, the number of bedrooms or bathrooms. 

I searched for a relevant dataset that would fit my needs while keeping my proposed research question, eventually finding a [New York Housing Market dataset](https://www.kaggle.com/datasets/nelgiriyewithana/new-york-housing-market).
I chose this dataset because it is similar to the Connecticut one in the sense that it a localized real estate dataset. However, what makes it more applicable are the independent variables such as square footage, bedrooms, bathrooms, and locality within the city. 
From this dataset, I am able to identify trends in the market and reasonably predict what properties will sell for based on its location, property type, square footage, bedrooms and bathrooms compared to other similar properties. The unfortunate downside to this dataset is it's small size of just under 5,000 records, but I'm willing to sacrafice quantity for quality.

## Methods

Describe the methods used fro the data analysis

## Conclusion

A final section that summarizes the results and conclusions, including any relevant figures/visualizations

(Probably going to be my shiny app)
