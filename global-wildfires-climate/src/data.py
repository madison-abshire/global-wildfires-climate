import streamlit as st
import pandas as pd

#the rest is up to you
@st.cache_data(show_spinner=False)
def load_data(path: str) -> pd.DataFrame:
    """Loading a small CSV and caching it so the app stays responsive."""
    df = pd.read_csv(path)

    return df