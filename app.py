from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("placement_predictor.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = pd.DataFrame([{
            "CGPA": float(request.form["cgpa"]),
            "Internships": int(request.form["internships"]),
            "Projects": int(request.form["projects"]),
            "Workshops/Certifications": int(request.form["workshops"]),
            "AptitudeTestScore": float(request.form["aptitude"]),
            "SoftSkillsRating": float(request.form["communication"]),

            # FIX: safe conversion from HTML dropdown (0/1)
            "ExtracurricularActivities": int(request.form["extracurricular"]),
            "PlacementTraining": int(request.form["training"]),

            "SSC_Marks": float(request.form["ssc"]),
            "HSC_Marks": float(request.form["hsc"])
        }])

        prediction = model.predict(data)

        result = "Placed ✅" if prediction[0] == 1 else "Not Placed ❌"

        return render_template("index.html", prediction=result)

    except Exception as e:
        # helpful debug instead of crashing
        return render_template("index.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)