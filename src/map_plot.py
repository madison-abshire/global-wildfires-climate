import pandas as pd
import streamlit as st
import plotly.express as px

def wildfire_worldmap_plot(df: pd.DataFrame, year_range) -> None:
    start_year, end_year = year_range

    fig = px.scatter_map(df,
                         lat='Latitude',
                         lon='Longitude',
                         color="Fires_Count",
                         size="Burned_Area_Km",
                         title=f"Historical Wildfire World Map ({start_year}-{end_year})",
                         color_continuous_scale="Sunsetdark",
                         hover_data=["Year", "Country", "Region"],
                         width=800,
                         height=700,
                         zoom=.75)

    st.plotly_chart(fig, width="stretch")