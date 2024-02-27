from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_disease():
    age = int(request.form.get('age'))
    sex = int(request.form.get('sex'))
    blood_pressure = int(request.form.get('blood-pressure'))
    cholestrol = int(request.form.get('cholestrol'))
    blood_sugar = int(request.form.get('blood-sugar'))
    ecg = int(request.form.get('ecg'))
    print(age, sex, blood_pressure, blood_sugar, cholestrol, ecg)
    result = model.predict(np.array([age, sex, blood_pressure, cholestrol, blood_sugar, ecg]).reshape(1, -1))
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
