Student Placement Prediction System
A machine learning-based web application that predicts whether a student is likely to be placed based on academic performance, skills, and activity-related features. The project is deployed using Flask and provides real-time predictions through a web interface.
Live Demo
https://student-placement-predictor-rzd5.onrender.com⁠
Project Overview
This project focuses on building a supervised machine learning model to predict student placement outcomes. It demonstrates an end-to-end workflow including data preprocessing, model training, evaluation, and deployment as a web application.
Tech Stack
Python
Pandas
NumPy
Scikit-learn
XGBoost
Flask
HTML / CSS
Machine Learning Model
Algorithm: XGBoost Classifier
Task: Binary Classification (Placed / Not Placed)
Evaluation Metric: Accuracy
Accuracy: ~80% (approx.)
Project Workflow
Data Collection (Kaggle dataset)
Data Cleaning and Preprocessing
Feature Selection and Engineering
Model Training using XGBoost
Model Evaluation
Web Application Development using Flask
Deployment on Render
Web Application Features
Input form for student data
Real-time prediction output
Backend integration with trained ML model
Simple and functional user interface
Challenge Faced
A major issue during deployment was related to the requirements.txt file.
It was generated using:
pip freeze > requirements.txt
This included unnecessary system-level dependencies from the local environment, which caused deployment failures on Render. The issue was resolved by cleaning and optimizing the dependencies.
Project Structure
student-placement-predictor/
│
├── app.py
├── placement_predictor.pkl
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── dataset/
└── README.md
Key Learnings
End-to-end machine learning workflow
Model development using XGBoost
Flask-based web application development
Deployment on cloud platforms
Debugging real-world environment issues
Importance of clean dependency management
Future Improvements
Improve model performance through hyperparameter tuning
Add data visualization dashboard
Enhance UI/UX design
Deploy using Docker for better scalability
Author
Manasvi Verma
B.Tech (Mathematics and Computing)
