from flask import Flask, render_template, request
import numpy as np
from database import *
import pickle

model = pickle.load(open('clf.pkl', 'rb'))
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# @app.route('/')
# def index():
#     return render_template('predictor.html')





@app.route('/', methods=['POST', 'GET'])
def predict_disease():
    
    if request.method == "POST":
        age = int(request.form.get('age'))
        gender = int(request.form.get('gender'))
        cp = int(request.form.get('cp'))
        trestbps = int(request.form.get('trestbps'))
        chol = int(request.form.get('chol'))
        fasting_blood_sugar = int(request.form.get('fasting_blood_sugar'))
        ecg = int(request.form.get('ecg'))
        thalach = int(request.form.get('thalach'))
        exang = int(request.form.get('exang'))
        oldpeak = float(request.form.get('oldpeak'))
        slope = int(request.form.get('slope'))
        ca = int(request.form.get('ca'))
        thal = int(request.form.get('thal'))

        

        final_features = np.array(
            [age, gender, cp, trestbps, chol, fasting_blood_sugar, ecg, thalach, exang, oldpeak, slope, ca,
             thal]).reshape(-1, 13)
        print(final_features)
        prediction = model.predict(final_features)
        print(prediction[0])

        return render_template('output.html', has_disease=prediction[0])
    return render_template('predictor.html')


if __name__ == '__main__':
    app.run(debug=True)
