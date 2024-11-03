import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Correlation Analysis")

# Check if data exists in Session State
if 'uploaded_data' in st.session_state:
    df = st.session_state['uploaded_data']
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['number'])
    
    if numeric_df.shape[1] > 1:
        # Calculate correlation matrix
        st.write("### Correlation Matrix")
        correlation = numeric_df.corr().fillna(0)  # Replace NaNs if any
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
        
        # Convert to DataFrame with labeled columns
        high_corr_df = pd.DataFrame(high_corr_pairs).reset_index()
        high_corr_df.columns = ["Variable 1", "Variable 2", "Correlation"]  # Label columns

        # Display the highly correlated pairs with labels
        if not high_corr_df.empty:
            st.write(high_corr_df)
        else:
            st.write("No pairs of variables have a correlation above the threshold.")
    else:
        st.write("Not enough numeric columns to compute correlation.")
else:
    st.write("Please upload data on the main page.")
