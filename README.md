# Performance Predictor

This Streamlit-based web application predicts whether a student will **pass or fail** based on their academic and personal data from the [`student_mat.csv`](https://archive.ics.uci.edu/ml/datasets/Student+Performance) dataset. It supports model training, performance visualization, and real-time predictions through an interactive UI.

---

## 📂 Features

- Upload and explore student performance CSV data
- Automatic preprocessing (label encoding, missing value handling)
- Train models: Random Forest or Logistic Regression
- Set hyperparameters interactively
- Visualizations:
  - Histogram & Scatter EDA
  - Confusion Matrix
  - ROC Curve
  - Feature Importances
- Predict outcome for a single student input
- Batch prediction on entire dataset
- Download prediction results as CSV

---

## 🚀 Live Demo

Deployed on **Streamlit Cloud**:  
🔗 [https://your-username.streamlit.app](https://your-username.streamlit.app)  
*(Replace with your actual app link)*

---

## 📁 Dataset

The app expects a CSV file like [`student_mat.csv`](https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip), which should include fields like `G1`, `G2`, `G3`, and other categorical/numeric attributes.

Ensure the dataset includes a `G3` column for final grades.

---

## 🔧 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/Performance-Predictor.git
cd Performance-Predictor
pip install -r requirements.txt
