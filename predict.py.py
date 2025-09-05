{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "25ebc231-7401-480a-a8bf-955ea509187b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Model loaded!\n",
      "Applicant 1: Default=0 (Risk Probability=0.45)\n",
      "Applicant 2: Default=0 (Risk Probability=0.00)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "# Load trained model\n",
    "model = joblib.load(\"models/credit_model_rf.joblib\")\n",
    "print(\"✅ Model loaded!\")\n",
    "\n",
    "# Example new applicants (hardcoded)\n",
    "new_data = pd.DataFrame([{\n",
    "    \"income\": 45000,\n",
    "    \"age\": 29,\n",
    "    \"debt\": 12000,\n",
    "    \"credit_util\": 0.45,\n",
    "    \"num_late\": 2,\n",
    "    \"prev_defaults\": 0,\n",
    "    \"emp_len\": 5,\n",
    "    \"credit_hist\": 10,\n",
    "    \"home_ownership\": \"RENT\",\n",
    "    \"purpose\": \"credit_card\",\n",
    "    \"debt_to_income\": 12000/45000,\n",
    "    \"young\": 1 if 29 < 25 else 0\n",
    "},\n",
    "{\n",
    "    \"income\": 120000,\n",
    "    \"age\": 45,\n",
    "    \"debt\": 5000,\n",
    "    \"credit_util\": 0.15,\n",
    "    \"num_late\": 0,\n",
    "    \"prev_defaults\": 0,\n",
    "    \"emp_len\": 15,\n",
    "    \"credit_hist\": 20,\n",
    "    \"home_ownership\": \"MORTGAGE\",\n",
    "    \"purpose\": \"home\",\n",
    "    \"debt_to_income\": 5000/120000,\n",
    "    \"young\": 0\n",
    "}])\n",
    "\n",
    "# Predict\n",
    "predictions = model.predict(new_data)\n",
    "proba = model.predict_proba(new_data)[:,1]\n",
    "\n",
    "for i, (p, pr) in enumerate(zip(predictions, proba)):\n",
    "    print(f\"Applicant {i+1}: Default={p} (Risk Probability={pr:.2f})\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
