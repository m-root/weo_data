# WEO Analysis Flask Project

This project uses Python Flask to provide an API that interacts with a Machine Learning model trained on the WEOOct2020all dataset. The Jupyter notebook `weo_notebook.ipynb` includes the exploratory data analysis, visualizations, and model training process.

## Prerequisites

- Python 3.7 or later
- Libraries: flask, pandas, numpy, sklearn, joblib, pydantic
- A trained machine learning model in `.pkl` format

## Installation

1. Clone the repository:
   ```
   git clone git@github.com:m-root/weo_data.git
   ```
2. Navigate to the project directory:
   ```
   cd weo_data
   ```
3. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the necessary libraries:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask app:
   ```
   python main.py
   ```
2. The application will start on localhost port 5000. To use the prediction endpoint, make a POST request to `http://localhost:5000/predict` with a JSON body that contains the feature values.

## Running the Notebook

The `weo_notebook.ipynb` Jupyter notebook contains the data exploration, visualization, and model training steps. To run the notebook:

1. Install Jupyter if you haven't already:
   ```
   pip install jupyter
   ```
2. Start Jupyter Notebook:
   ```
   jupyter notebook
   ```
3. In the Jupyter Notebook interface in your browser, navigate to the project directory and open `weo_notebook.ipynb`.


