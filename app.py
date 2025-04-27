from flask import Flask, render_template, request
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import os
import numpy as np

# Initialize app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Preprocessing function (customize based on your dataset)
def preprocess(data):
    # Assuming your model expects features like 'amount', 'merchant_id', etc.
    # Here just selecting numeric columns
    features = data[['amount', 'merchant_id', 'user_id', 'time']]
    return features

# Home Page
@app.route('/')
def index():
    return render_template('index.html')



# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get uploaded file
        file = request.files['file']
        if not file:
            return "No file uploaded", 400
        
        # Read CSV file
        data = pd.read_csv(file, encoding='latin1', on_bad_lines='warn')


        
        # Preprocess the data
        processed_data = preprocess(data)

        # Make predictions
        preds = model.predict(processed_data)
        probs = model.predict_proba(processed_data)[:,1]

        # Attach predictions
        data['Fraud_Prediction'] = preds
        data['Fraud_Probability'] = probs

        # Convert to HTML table
        results = data.to_html(classes='table table-striped table-dark', index=False)

        return render_template('result.html', tables=[results])

if __name__ == '__main__':
    app.run(debug=True)
