import pandas as pd
import streamlit as st

def sidebar_filters(df: pd.DataFrame) -> tuple:

    st.sidebar.header("Filters")

    # Year range
    min_year = int(df["Year"].min())
    max_year = int(df["Year"].max())

    year_range = st.sidebar.slider(
        "Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )

    # Country multiselect
    countries = sorted(df["Country"].unique())

    selected_countries = st.sidebar.multiselect(
        "Country",
        options=countries,
        default=countries
    )

    # Cause multiselect
    causes = sorted(df["Cause"].unique())

    selected_causes = st.sidebar.multiselect(
        "Cause",
        options=causes,
        default=causes
    )

    return year_range, selected_countries, selected_causes


def weather_condition_select() -> str:
    cols = ["Temperature_C","Humidity_Percent","Wind_Speed_kmh"]
    return st.selectbox("Select weather condition", cols)