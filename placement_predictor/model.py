import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier


data = pd.read_csv("C:\\Users\\manas\\OneDrive\\Desktop\\placementdata.csv", index_col="StudentID")
print(data.head())

yes_no_map = {"Yes": 1, "No": 0}

data["ExtracurricularActivities"] = data["ExtracurricularActivities"].map(yes_no_map)
data["PlacementTraining"] = data["PlacementTraining"].map(yes_no_map)


features = [
    'CGPA',
    'Internships',
    'Projects',
    'Workshops/Certifications',
    'AptitudeTestScore',
    'SoftSkillsRating',
    'ExtracurricularActivities',
    'PlacementTraining',
    'SSC_Marks',
    'HSC_Marks'
]

X = data[features]
y = data['PlacementStatus']


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)



le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)
y_test_encoded = le.transform(y_test)


my_model = XGBClassifier(
    random_state=42,
    eval_metric="logloss"
)

my_model.fit(X_train, y_train_encoded)


pred = my_model.predict(X_test)
accuracy = accuracy_score(y_test_encoded, pred)
print("Accuracy:", accuracy)


joblib.dump(my_model, "placement_predictor.pkl")
joblib.dump(le, "label_encoder.pkl")
joblib.dump(features, "feature_order.pkl")

print("Model and Encoders Saved Successfully!")

import os
print(os.getcwd())