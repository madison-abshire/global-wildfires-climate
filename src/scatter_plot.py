import pandas as pd
import plotly.express as px
import streamlit as st
from src.cause_color_map_util import cause_color_map

def scatter_weather_conditions_plot(df: pd.DataFrame, weather_metric: str, year_range) -> None:
    if df.empty:
        st.warning("No Data Available")
        return
    start_year, end_year = year_range

    name_map = {"Humidity_Percent": "Humidity Percent",
                "Temperature_C": "Temperature (C)",
                "Wind_Speed_kmh": "Wind Speed (km/h)"}
    palette = cause_color_map()

    fig = px.strip(df,
                     x=weather_metric,
                     y="Cause",
                     labels={"Cause": "Cause",
                             weather_metric: name_map[weather_metric]},
                     title=f"Distribution of Cause by Weather Condition ({start_year}-{end_year})",
                     color="Cause",
                     hover_data=["Country","Region","Year"],
                     color_discrete_map=palette)
    fig.update_yaxes(categoryorder='category ascending')
    fig.update_traces(jitter=1, opacity=0.75, marker=dict(size=5))

    st.plotly_chart(fig, width="stretch")