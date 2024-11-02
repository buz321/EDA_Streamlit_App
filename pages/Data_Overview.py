import streamlit as st
import pandas as pd

st.title("Data Overview")

# Check if data exists in Session State
if 'uploaded_data' in st.session_state:
    df = st.session_state['uploaded_data']  # Retrieve the data
    
    # Display number of observations and variables with commas
    num_observations, num_variables = df.shape
    st.write(f"**Number of Observations:** {num_observations:,}")
    st.write(f"**Number of Variables:** {num_variables:,}")

    # Display dataset preview
    st.write("### Dataset Preview")
    st.write(df.head())

    # Display summary statistics with commas
    st.write("### Summary Statistics")
    st.write(df.describe().applymap(lambda x: f"{x:,.2f}" if isinstance(x, (int, float)) else x))

    # Display individual data types with labeled columns
    st.write("### Data Types")
    st.write("Here are the data types for each variable:")
    
    # Convert data types to DataFrame and label columns
    data_types_df = pd.DataFrame(df.dtypes, columns=["Data Type"]).reset_index()
    data_types_df.columns = ["Variable", "Data Type"]  # Rename columns
    st.write(data_types_df)  # Display the data types with column labels

    # Display count of each unique data type with custom column name and commas
    st.write("#### Count of Each Data Type")
    data_type_counts = df.dtypes.value_counts().rename_axis("Data Type").reset_index(name="Data Type Count")
    data_type_counts["Data Type Count"] = data_type_counts["Data Type Count"].apply(lambda x: f"{x:,}")
    st.write(data_type_counts)
else:
    st.write("Please upload data on the main page.")
