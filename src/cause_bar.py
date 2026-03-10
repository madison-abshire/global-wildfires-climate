import pandas as pd
import streamlit as st
import plotly.express as px
from src.cause_color_map_util import cause_color_map

def cause_country_plot(df: pd.DataFrame, year_range) -> None:
    start_year, end_year = year_range

    if df.empty:
        st.warning("No data available.")
        return

    country_cause = (df.groupby(["Country", "Cause"])["Fires_Count"].sum().reset_index())

    fig = px.bar(country_cause, x="Country", y="Fires_Count",
                 color="Cause",
                 barmode="group",
                 title=f"Wildfire Causes by Country ({start_year}-{end_year})",
                 labels={"Fires_Count": "Total Fires",
                         "Country": "Country",
                         "Cause": "Wildfire Cause"},
                 color_discrete_map=cause_color_map()
                 )
    fig.update_layout(xaxis_tickangle=0)
    fig.update_xaxes(categoryorder="category ascending")

    st.plotly_chart(fig, width='stretch')
