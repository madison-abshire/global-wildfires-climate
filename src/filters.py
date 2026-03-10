import pandas as pd
import streamlit as st

def date_slider(df: pd.DataFrame) -> tuple:
    # Key variable differentiates the multiple year slider widgets
    min_year = int(df["Year"].min())
    max_year = int(df["Year"].max())

    year_range = st.slider("Select year range",
                           min_value=min_year,
                           max_value=max_year,
                           value=(min_year, max_year))
    return year_range

def weather_condition_select() -> str:
    cols = ["Temperature_C","Humidity_Percent","Wind_Speed_kmh"]
    return st.selectbox("Select weather condition", cols)


def country_select(df: pd.DataFrame, year_range: tuple, key: str) -> list:
    start_year, end_year = year_range

    filtered_df = df[
        (df["Year"] >= start_year) &
        (df["Year"] <= end_year)
        ]

    countries = sorted(filtered_df["Country"].unique())

    selected_countries = st.multiselect("Select country(s)", options=countries, default=countries, key=key)

    return selected_countries
