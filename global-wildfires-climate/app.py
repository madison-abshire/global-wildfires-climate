import streamlit as st
from src.data import load_data

def main() -> None:
    st.set_page_config(
        page_title="Global Wildfire Occurrences (1881-2025)",
        layout="wide",
    )

    st.title("Global Wildfire Occurrences (1881-2025)")
    st.caption("Historical view of wildfire occurrences in fire-prone regions")

    df = load_data("data/sample.csv")


if __name__ == "__main__":
    main()
