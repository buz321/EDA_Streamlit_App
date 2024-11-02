import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Missing Values Analysis")

# Check if data exists in Session State
if 'uploaded_data' in st.session_state:
    df = st.session_state['uploaded_data']
    
    st.write("### Missing Values Count")
    st.write(df.isnull().sum())

    # Display a heatmap of missing values
    st.write("### Missing Values Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis", ax=ax)
    st.pyplot(fig)
else:
    st.write("Please upload data on the main page.")
