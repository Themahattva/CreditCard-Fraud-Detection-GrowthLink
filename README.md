# CreditCard-Fraud-Detection-GrowthLink
A machine learning project that detects fraudulent credit card transactions using transaction time, amount, merchant ID and user ID.

💳 Credit Card Fraud Detection
🔹 Project Overview:
This project is a machine learning-based web application designed to detect fraudulent credit card transactions.
It uses transaction details such as transaction time, user ID, merchant information, purchase amount, and other attributes to predict whether a transaction is fraudulent or legitimate.
The backend is powered by a trained machine learning model, and the frontend is built using Flask for a smooth, interactive user experience.

🔹 Key Features:
📅 Transaction Data Processing: Handles and processes transaction datasets using pandas and numpy.

📈 Machine Learning Model: Predicts fraudulent transactions based on transaction patterns.

🎨 Web Interface: A simple and responsive Flask web application where users can input transaction details and get instant fraud detection results.

📊 Visualisation Support: Ability to generate and display plots using matplotlib (optional).

🛠️ Model Loading: Pre-trained machine learning model is loaded using pickle.

🔹 Technologies Used:
Python 3

Flask (for the web application)

Pandas and NumPy (for data handling)

Matplotlib (for visualisation)

Scikit-learn (for machine learning model training and usage)

Pickle (for model serialisation)

🔹 Workflow:
Train the model on historical transaction data.

Save the trained model using pickle.

Create a Flask app to interact with the model via a web interface.

Input transaction details through the web form.

Predict and display whether the transaction is fraudulent or not.

🏆 Final Outcome:
A fast, lightweight, and easy-to-use Credit Card Fraud Detection System capable of helping financial platforms detect suspicious transactions and reduce fraud losses
STEPS TO RUN THE PROGRAM:
1. Clone or Download the Project.
2. Install Required Libraries(pip install -r requirements.txt)
3. Train the Model (RUN fraud_detection.py with the given FraudTest.csv dataset)
4. Start the Web Application (Run app.py).
5. Start a local server.
6. Upload the test CSV file (test.csv).
7. Observe the result of fraudulent credit card transactions.

#GROWTH LINK 
