import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Function to detect outliers using Z-score
def detect_outliers_zscore(df, threshold=3):
    outliers_count = {}
    for column in df.select_dtypes(include=[np.number]):  # Only numerical columns
        z_scores = zscore(df[column].dropna())  # Compute Z-scores
        outliers = np.abs(z_scores) > threshold  # Identify outliers
        outliers_count[column] = np.sum(outliers)  # Count of outliers for the column
    return outliers_count

# Streamlit app
st.title("Outlier Detection App with Z-Score")
st.write("Upload a dataset to visualize and count outliers for each numerical variable.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Overview:", df.head())

    # Detect outliers
    st.subheader("Outlier Counts by Variable")
    outliers_count = detect_outliers_zscore(df)
    outliers_df = pd.DataFrame(list(outliers_count.items()), columns=['Variable', 'Outlier Count'])
    st.write(outliers_df)

    # Plot box plots with outliers
    st.subheader("Box Plot of Each Variable with Outliers")
    for column in df.select_dtypes(include=[np.number]):
        fig, ax = plt.subplots()
        ax.boxplot(df[column].dropna(), vert=False)
        ax.set_title(f'Box Plot of {column}')
        ax.set_xlabel(column)
        st.pyplot(fig)
else:
    st.write("Please upload a CSV file to get started.")

