# E-commerce Analytics Dashboard

An advanced e-commerce analytics dashboard for clothing brands, providing comprehensive performance tracking with dynamic and interactive data visualization.

## Features

- Interactive data visualization with Plotly charts
- Intelligent dropdown filters for categories and cities
- Flexible date range selection with independent start and end date inputs
- Comprehensive product and location performance metrics
- Export filtered data to CSV
- Category-wise performance analysis with visual banners

## Requirements

Before running the project, ensure you have Python 3.8+ installed. The following packages are required:

- streamlit
- pandas
- numpy
- plotly

## Installation

1. Clone this repository or download the source code.

2. Install the required packages using the package manager:

```bash
python -m pip install streamlit pandas numpy plotly
```

## Running the Application

1. Navigate to the project directory in your terminal.

2. Start the Streamlit server:

```bash
streamlit run main.py
```

3. The application will start and automatically open in your default web browser. If it doesn't, you can access it at `http://localhost:5000`.

## Usage

1. **Date Range Selection**:

   - Use the "Start Date" and "End Date" inputs in the sidebar to filter data by date range
   - Each date can be modified independently

2. **Category and City Filters**:

   - Select one or multiple categories from the dropdown menu
   - Choose specific cities to analyze from the dropdown menu
   - All options are selected by default

3. **Data Visualization**:

   - View sales distribution by category
   - Analyze daily sales trends
   - Track geographic sales performance
   - Monitor top-performing products

4. **Category Performance**:

   - Detailed metrics for each selected category
   - Visual banners for category representation
   - Individual performance indicators

5. **Data Export**:
   - Use the "Export Filtered Data" button to download the current view as a CSV file

## Project Structure

- `main.py`: Main application file containing the Streamlit dashboard
- `utils.py`: Utility functions for creating charts and calculating metrics
- `data_generator.py`: Mock data generation for demonstration
- `.streamlit/config.toml`: Streamlit configuration file

## Notes

- The dashboard uses mock data generated for demonstration purposes
- All charts are interactive and respond to the sidebar filters
- The application is configured to run in headless mode for server deployment
