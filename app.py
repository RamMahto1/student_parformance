from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and preprocessor
model = pickle.load(open("artifacts/model.pkl", "rb"))
preprocessor = pickle.load(open("artifacts/preprocessor.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = {
            "gender": request.form['gender'],
            "race_ethnicity": request.form['race_ethnicity'],
            "parental_level_of_education": request.form['parental_level_of_education'],
            "lunch": request.form['lunch'],
            "test_preparation_course": request.form['test_preparation_course'],
            "reading_score": float(request.form['reading_score']),
            "writing_score": float(request.form['writing_score'])
        }

        df = pd.DataFrame([data])

        # Transform and predict
        transformed = preprocessor.transform(df)
        prediction = model.predict(transformed)

        return render_template(
            'index.html',
            prediction_text=f"Predicted Math Score: {round(prediction[0],2)}"
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=True)