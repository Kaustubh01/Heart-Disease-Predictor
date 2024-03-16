from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open('clf.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict_disease():
    if request.method == "POST":
        age = int(request.args.get('age'))
        gender = int(request.args.get('gender'))
        cp = int(request.args.get('cp'))
        trestbps = int(request.args.get('trestbps'))
        chol = int(request.args.get('chol'))
        fasting_blood_sugar = int(request.args.get('fasting_blood_sugar'))
        ecg = int(request.args.get('ecg'))
        thalach = int(request.args.get('thalach'))
        exang = int(request.args.get('exang'))
        oldpeak = float(request.args.get('oldpeak'))
        slope = int(request.args.get('slope'))
        ca = int(request.args.get('ca'))
        thal = int(request.args.get('thal'))

        data = [age, gender, cp, trestbps, chol, fasting_blood_sugar, ecg, thalach, exang, oldpeak, slope, ca, thal]
        print(data)
        predict(np.array([data]).reshape(-1, 13))
    return render_template('predictor.html')


def predict(data):
    return loaded_model.predict(data)


if __name__ == '__main__':
    app.run(debug=True)
