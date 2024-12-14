#Author: Jack Schnair
#Class:  CS539 Machine Learning
#Assignment: Milestone 3

import faicons as fa
import plotly.express as px

# Load data and compute static values
from shared import app_dir, tips
from shinywidgets import output_widget, render_plotly

from shiny import App, reactive, render, ui

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

app_ui = ui.page_fluid(
    ui.row(
        ui.tags.style(
        """
        body {
            background-color: MediumSeaGreen;
        }
        """
        ),
        ui.panel_title("New York City Housing Price Predictor"),
        ui.input_select(
            "bedrooms",
            "Choose number of bedrooms:",
            choices=["1", "2", "3", "4", "5"]),
        ui.input_select(
            "bathrooms",
            "Choose number of bathrooms:",
            choices=["1", "2", "3", "4", "5"]),
        ui.input_select(
            "type",
            "Choose a property type:",
            {
                "Type": {"Condo for sale": "Condo",
                        "House for sale": "House",
                        "Townhouse for sale": "Townhouse",
                        "Multi-family home for sale": "Multi-family"},
            },
        ),
        ui.input_select(
            "area",
            "Choose an area:",
            {
                "Area": {"Manhattan": "Manhattan",
                        "Queens": "Queens",
                        "The Bronx": "The Bronx",
                        "Brooklyn": "Brooklyn",
                        "Staten Island": "Staten Island", },
            },
        ),
        ui.input_text("sqft", "Enter preferred square footage:", value="2000"),
        ui.input_checkbox_group("checkbox_group", "Checkbox group (Not Functional)",
        {"bed_check": "Bedrooms","bath_check": "Bathrooms","type_check": "Property Type","area_check": "Area", "sqft_check": "Square Footage"},),
        ui.output_text("selected_bedrooms"),
        ui.output_text("selected_bathrooms"),
        ui.output_text("selected_type"),
        ui.output_text("selected_area"),
        ui.output_text("selected_sqft"),
        ui.output_text("selected_checks"),
        ui.input_action_button("predict", "run_model"),
        ui.output_text("solution")
    )
)

def server(input, output, session):
    @render.text
    def selected_bedrooms():
        return f"{input.bedrooms()} Bedroom(s)"

    @render.text
    def selected_bathrooms():
        return f"{input.bathrooms()} Bathroom(s)"

    @render.text
    def selected_type():
        return "Type: " + str(input.type())

    @render.text
    def selected_area():
        return "Area: " + str(input.area())

    @render.text
    def selected_sqft():
        return "Square Footage: " + str(input.sqft())

    @render.text
    def solution():
        if input.predict():
            df = pd.read_csv("NY_cleaned.csv")

            x = df.drop(columns=['PRICE'])
            y = df['PRICE']

            # Match Type and Locality to encoded values
            isCondo = "0"
            isHouse = "0"
            isMulti = "0"
            isTown = "0"
            if input.type() == "Condo":
                isCondo = "1"
            if input.type() == "House":
                isHouse = "1"
            if input.type() == "Townhouse":
                isMulti = "1"
            if input.type() == "Multi-family":
                isTown = "1"

            
            isManhattan = "0"
            isQueens = "0"
            isStatenIsland = "0"
            isTheBronx = "0"
            isBrooklyn = "0"
            if input.area() == "Manhattan":
                isManhattan = "1"
            if input.area() == "Queens":
                isQueens = "1"
            if input.area() == "Staten Island":
                isStatenIsland = "1"
            if input.area() == "The Bronx":
                isTheBronx = "1"
            if input.area() == "Brooklyn":
                isBrooklyn = "1"

            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=12)

            rr_model = RandomForestRegressor(n_estimators=64, random_state=12)
            rr_model.fit(x_train, y_train)

            our_home = pd.DataFrame(np.array([[input.bedrooms(), input.bathrooms(), input.sqft(), isCondo, isHouse, isMulti, isTown, "0", "1", "0", "0"]]))
            our_home.columns = x_train.columns
            our_home_pred = rr_model.predict(our_home)
            pred_str = str(our_home_pred)
            return "Estimated Price: $" + pred_str[1:-7]

app = App(app_ui, server)
