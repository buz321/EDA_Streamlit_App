import streamlit as st
import pandas as pd

st.title(":bar_chart: EDA Dashboard")
st.write("Upload your data to start exploring various EDA tasks.")

# Upload data file
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

# Store the uploaded data in Session State
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    # Save the data to Session State
    st.session_state['uploaded_data'] = df
    st.write("Data uploaded successfully!")
    st.write(df.head())
else:
    st.write("Please upload a CSV or Excel file.")
