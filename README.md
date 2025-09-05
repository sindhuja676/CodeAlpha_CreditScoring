💳 Credit Scoring Model
🚀 Project Overview

This project predicts an individual's creditworthiness using financial data.
It is part of the CodeAlpha Machine Learning Internship and demonstrates practical skills in data preprocessing, model training, and evaluation using Python and Scikit-learn.

The model helps lenders assess risk by classifying applicants as likely to default or not.

📊 Dataset

Training Data: data/simulated.csv
Simulated dataset with features such as income, age, debt, credit utilization, employment length, number of late payments, previous defaults, credit history, home ownership, and purpose.

Prediction Data: data/applicants.csv
New applicants for whom the model predicts creditworthiness.

🧩 Features

Numerical: income, age, debt, credit_util, num_late, prev_defaults, emp_len, credit_hist
Categorical: home_ownership, purpose
Target Variable: label (0 = Good Credit, 1 = Bad Credit)

🗂 Project Structure
CodeAlpha_CreditScoring/
│── data/
│   ├── simulated.csv
│   ├── applicants.csv
│── models/
│   ├── credit_model.pkl       ← saved trained model
│── train.py                   ← script to train model
│── predict.py                 ← script to predict
│── requirements.txt
│── README.md

🏃 How to Run
1️⃣ Train the Model
python train.py


Trains the model on simulated.csv and saves it as models/credit_model.pkl.

2️⃣ Predict on New Applicants
python predict.py


Loads the saved model and predicts creditworthiness for applicants.csv.

📈 Model Evaluation

The model is evaluated using:

Accuracy

Precision

Recall

F1-Score

🛠 Dependencies

All required Python packages are listed in requirements.txt:

pandas

numpy

scikit-learn

joblib

(Install them using pip install -r requirements.txt if needed)

💡 Notes

Categorical features are one-hot encoded.

Make sure the datasets are in the data/ folder.

You can retrain the model anytime by running train.py.

The trained model is saved as models/credit_model.pkl and can be reused for predictions without retraining.