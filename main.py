import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
st.title("Data Analysis and Visualization App")
st.write("Upload a dataset (CSV or Excel) to visualize and count outliers for each numerical variable.")

# File uploader to accept CSV and Excel files
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xls", "xlsx"])

if uploaded_file is not None:
    # Check the file extension and read the file accordingly
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Dataset Overview:", df.head())

    # Detect outliers
    st.subheader("Outlier Counts by Variable")
    outliers_count = detect_outliers_zscore(df)
    outliers_df = pd.DataFrame(list(outliers_count.items()), columns=['Variable', 'Outlier Count'])
    st.write(outliers_df)

    # Plot selection
    st.subheader("Choose a Plot to Visualize Data")
    
    # Select variable for plotting
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    selected_column = st.selectbox("Select a column to plot:", numeric_columns)

    # Select plot type
    plot_type = st.selectbox("Choose a plot type:", ["Line Plot", "Box Plot", "Distribution Plot"])

    # Generate selected plot
    if plot_type == "Line Plot":
        st.subheader("Line Plot")
        fig, ax = plt.subplots()
        ax.plot(df[selected_column], color="skyblue")
        ax.set_title(f"Line Plot of {selected_column}")
        ax.set_xlabel("Index")
        ax.set_ylabel(selected_column)
        st.pyplot(fig)

    elif plot_type == "Box Plot":
        st.subheader("Box Plot")
        fig, ax = plt.subplots()
        sns.boxplot(data=df, y=selected_column, ax=ax, color="lightcoral")
        ax.set_title(f"Box Plot of {selected_column}")
        st.pyplot(fig)

    elif plot_type == "Distribution Plot":
        st.subheader("Distribution Plot")
        fig, ax = plt.subplots()
        sns.histplot(df[selected_column], kde=True, ax=ax, color="lightblue")
        ax.set_title(f"Distribution Plot of {selected_column}")
        ax.set_xlabel(selected_column)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
else:
    st.write("Please upload a CSV or Excel file to get started.")
