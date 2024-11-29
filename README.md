# EDA Streamlit App
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://edaappapp-xkrns2w2d8nki78h5grwuk.streamlit.app/)
## Overview

This repository contains a user-friendly **Exploratory Data Analysis (EDA) Web Application** built using **Streamlit**. The app allows users to upload datasets, explore data visually, and gain insights through interactive visualizations and summaries. It simplifies the EDA process, making it accessible even to those with minimal programming knowledge.

## Features

- **Dataset Upload**: Users can upload CSV files for analysis.
- **Summary Statistics**: Automatically generate key descriptive statistics for the uploaded dataset.
- **Data Visualizations**:
  - Interactive plots and graphs, including:
    - Histograms
    - Scatter plots
    - Bar charts
  - Customizable visualization parameters for deeper insights.
- **Missing Data Analysis**: Identify and handle missing values effectively.
- **Correlation Analysis**: Visualize relationships between variables using heatmaps.
- **User-Friendly Interface**: Intuitive design powered by Streamlit, allowing easy navigation.

## Installation
1. Clone the repository by running the following command in your terminal:
   ```bash
   git clone https://github.com/buz321/EDA_Streamlit_App.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd EDA_Streamlit_App
   ```
   
3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
   
4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```


## How to Use

1. Upload your dataset (CSV format) using the upload feature.
2. Explore the dataset through:
   - Descriptive statistics
   - Visualizations (histograms, scatter plots, bar charts, etc.)
   - Correlation heatmaps
   - Missing data summaries
3. Customize visualizations and explore insights interactively.

## Technologies Used

- **Programming Language**: Python
- **Framework**: Streamlit
- **Libraries**: Pandas, Matplotlib, Seaborn, Plotly

## Future Enhancements

- Add support for additional file formats (e.g., Excel, JSON).
- Include advanced visualizations like box plots and pair plots.
- Implement machine learning model integration for predictive analysis.

## Contributions

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
