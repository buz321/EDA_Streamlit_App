import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

st.title("Outlier Detection")

# Check if data exists in Session State
if 'uploaded_data' in st.session_state:
    df = st.session_state['uploaded_data']
    
    # Set Z-score threshold for outliers
    st.write("### Outliers by Z-Score")
    threshold = st.slider("Set Z-score threshold", 1, 4, 3)
    
    # Identify outliers based on Z-score for numerical columns
    outliers = pd.DataFrame()
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        outliers[col] = zscore(df[col]).abs() > threshold

    # Count outliers for each column and create a DataFrame with a labeled column
    outlier_counts = pd.DataFrame(outliers.sum(), columns=["Outlier Count"]).reset_index()
    outlier_counts.columns = ["Variable", "Outlier Count"]  # Rename columns
    st.write(outlier_counts)  # Display the outlier count table with column labels
    
    # Scatter plot to visualize data points and highlight outliers for each column
    st.write("### Scatter Plot of Numerical Columns with Outliers Highlighted")
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        fig, ax = plt.subplots()
        
        # Plot all data points in blue
        ax.scatter(df.index, df[col], label="Data Points", color="blue", s=10)
        
        # Highlight outliers in red
        outliers_points = df[col][outliers[col]]
        ax.scatter(outliers_points.index, outliers_points, color="red", label="Outliers", s=30, zorder=5)
        
        # Set plot title and labels
        ax.set_title(f'Scatter Plot of {col} with Outliers Highlighted')
        ax.set_xlabel("Index")
        ax.set_ylabel(col)
        ax.legend()
        
        st.pyplot(fig)
else:
    st.write("Please upload data on the main page.")