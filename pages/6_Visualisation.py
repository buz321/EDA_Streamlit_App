import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Data Visualization")

# Check if data exists in Session State
if 'uploaded_data' in st.session_state:
    df = st.session_state['uploaded_data']
    
    # Select columns for visualization (multiple selection allowed)
    selected_cols = st.multiselect("Select one or more columns for visualization", df.columns)
    plot_type = st.selectbox("Select plot type", ["Histogram", "Line Plot", "Box Plot"])

    # Generate the selected plot
    if plot_type == "Histogram":
        for col in selected_cols:
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            ax.set_title(f"Histogram of {col}")
            st.pyplot(fig)

    elif plot_type == "Line Plot":
        fig, ax = plt.subplots()
        for col in selected_cols:
            ax.plot(df.index, df[col], label=col)
        ax.legend()
        ax.set_title("Line Plot of Selected Columns")
        st.pyplot(fig)

    elif plot_type == "Box Plot":
        if len(selected_cols) > 0:
            fig, ax = plt.subplots()
            sns.boxplot(data=df[selected_cols], ax=ax)
            ax.set_title("Box Plot of Selected Columns")
            st.pyplot(fig)
        else:
            st.write("Please select at least one column for a box plot.")
else:
    st.write("Please upload data on the main page.")
