from flask import Flask, request, jsonify
from pydantic import ValidationError
import joblib
import json
import pandas as pd
from data.schema import PredictionModel
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Create the paths to the files
model_path = os.path.join(current_dir, 'trained_data', 'random_forest_all_features.pkl')
mapping_dict_path = os.path.join(current_dir, 'data', 'mapping_dict.json')

# Load the model and data
model = joblib.load(model_path)
with open(mapping_dict_path) as f:
    mapping_dict = json.load(f)

app = Flask(__name__)


@app.route('/predict_one', methods=['POST'])
def predict():
    try:
        # Validate request data
        data = PredictionModel(**request.get_json())
    except ValidationError as err:
        return jsonify(err.errors()), 400

    # Convert data into dataframe
    df = pd.DataFrame([data.dict()])

    # Rename the columns using the mapping dictionary
    try:
        df.rename(columns=mapping_dict, inplace=True, errors='raise')
    except KeyError as e:
        app.logger.error(f"Error renaming columns: {e}")
        return jsonify(error=f"Error renaming columns: {e}"), 500

    # Make prediction using model loaded from disk as per the data
    columns_order = model.feature_names_in_  # assuming that the model has `feature_names_in_` attribute
    df = df[columns_order]
    prediction = model.predict(df)

    # Take the first value of prediction
    output = prediction[0]

    return jsonify(gdp_per_capita=output)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
