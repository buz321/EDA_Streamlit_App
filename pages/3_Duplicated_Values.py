import streamlit as st
import pandas as pd

st.title("Duplicate Observations Detection")

# Check if data exists in Session State
if 'uploaded_data' in st.session_state:
    df = st.session_state['uploaded_data']
    
    # Find duplicate observations
    st.write("### Duplicate Observations")
    duplicated_rows = df[df.duplicated(keep=False)]  # keep=False marks all duplicates as True
    
    # Check if there are any duplicates
    if not duplicated_rows.empty:
        st.write("Found duplicated observations:")
        st.write(duplicated_rows)
    else:
        st.write("No duplicated observations found.")
else:
    st.write("Please upload data on the main page.")
