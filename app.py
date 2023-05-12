from flask import Flask, request, render_template
import pickle

import numpy

app = Flask(__name__)

model_file = open('cd.pkl','rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def home():
    return render_template('index.html', ump=0)

@app.route('/home')
def city():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():


    tahun = [x for x in request.form.values()]

    b = [float(s) for s in tahun[0].split("*")]

    prediction = model.predict([b])
    output = round(float(prediction[0]),2)
    return render_template('index.html', ump=output, tahun=tahun)

@app.route('/planner', methods=['POST'])
def planner():

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)