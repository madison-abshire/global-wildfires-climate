import pandas as pd
import plotly.express as px
import streamlit as st
from src.cause_color_map_util import cause_color_map  # optional if you want consistent colors

def total_fires_trend(df: pd.DataFrame, year_range: tuple) -> None:
    start_year, end_year = year_range

    if df.empty:
        st.warning("No data available for Total Fires Trend.")
        return

    yearly_fires = df.groupby("Year")["Fires_Count"].sum().reset_index()

    fig = px.line(
        yearly_fires,
        x="Year",
        y="Fires_Count",
        title=f"Total Fires Trend ({start_year}-{end_year})",
        markers=True,
        labels={"Fires_Count": "Total Fires", "Year": "Year"},
    )
    st.plotly_chart(fig, use_container_width=True)


def comparative_trend(df: pd.DataFrame, comparison_type: str, year_range, top_n: int = 5) -> None:
    start_year, end_year = year_range

    if df.empty:
        st.warning(f"No data available for {comparison_type} trend.")
        return

    if comparison_type == "Top 5 Countries":
        top_countries = (
            df.groupby("Country")["Fires_Count"].sum()
            .sort_values(ascending=False)
            .head(top_n)
            .index.tolist()
        )
        filtered_df = df[df["Country"].isin(top_countries)]
        title = f"Total Fires Trend by Top {top_n} Countries ({start_year}-{end_year})"
        color_column = "Country"

    elif comparison_type == "Causes":
        filtered_df = df.copy()
        title = f"Total Fires Trend by Cause ({start_year}-{end_year})"
        color_column = "Cause"

    else:
        st.error("Invalid comparison type")
        return

    trend_df = (
        filtered_df.groupby(["Year", color_column])["Fires_Count"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        trend_df,
        x="Year",
        y="Fires_Count",
        color=color_column,
        markers=True,
        title=title,
        labels={"Fires_Count": "Total Fires", "Year": "Year"},
        color_discrete_map=cause_color_map() if color_column=="Cause" else None
    )

    st.plotly_chart(fig, use_container_width=True)