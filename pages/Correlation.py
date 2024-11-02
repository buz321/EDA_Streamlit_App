import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Correlation Analysis")

# Check if data exists in Session State
if 'uploaded_data' in st.session_state:
    df = st.session_state['uploaded_data']
    
    # Calculate correlation matrix
    st.write("### Correlation Matrix")
    correlation = df.corr()
    st.write(correlation)
    
    # Display a heatmap of the correlation matrix
    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Define correlation threshold
    threshold = st.slider("Set correlation threshold", 0.5, 1.0, 0.8)
    
    # Find pairs of variables with high correlation
    st.write(f"### Pairs of Variables with Correlation Above {threshold}")
    high_corr_pairs = correlation.abs().unstack().sort_values(ascending=False)
    high_corr_pairs = high_corr_pairs[high_corr_pairs != 1]  # Exclude self-correlation
    high_corr_pairs = high_corr_pairs[high_corr_pairs >= threshold].drop_duplicates()
    
    # Display the highly correlated pairs
    if not high_corr_pairs.empty:
        st.write(high_corr_pairs)
    else:
        st.write("No pairs of variables have a correlation above the threshold.")
else:
    st.write("Please upload data on the main page.")
