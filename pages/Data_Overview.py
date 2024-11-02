import streamlit as st
import pandas as pd

st.title("Data Overview")

uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])
if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("### Dataset Preview")
    st.write(df.head())

    st.write("### Summary Statistics")
    st.write(df.describe())

    st.write("### Data Types")
    st.write(df.dtypes)
