# New York Housing Predictor
Final Project for CS539 Machine Learning <br>
By Jack Schnair

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

# Methods

Describe the methods used fro the data analysis

# Conclusion

A final section that summarizes the results and conclusions, including any relevant figures/visualizations

(Probably going to be my shiny app)
