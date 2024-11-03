import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Missing Values Analysis")

# Check if data exists in Session State
if 'uploaded_data' in st.session_state:
    df = st.session_state['uploaded_data']
    
    # Calculate missing values count for each column and covert to DataFrame
    missing_values = pd.DataFrame(df.isnull().sum(), columns = ["Missing Value Count"]).reset_index()
    missing_values.columns = ["Variable", "Missing Value Count"] # Label the columns

    # Display missing values count table
    st.write("### Missing Values Count")
    st.write(missing_values)

    # Check if there are any missing values in the dataset
    if missing_values["Missing Value Count"].sum() == 0:
        st.write("### Missing Values Heatmap")
        # If no missing values, display a message
        st.write("No missing values found in the dataset.")
    else:
        # If there are missing values, plot the heatmap
        st.write("### Missing Values Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis", ax=ax)
        st.pyplot(fig)
else:
    st.write("Please upload data on the main page.")

