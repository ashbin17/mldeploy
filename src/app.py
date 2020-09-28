from flask import Flask, request
from flask import render_template
import joblib

model = joblib.load('./model/model.pkl')
app = Flask('app')


@app.route('/')
def home_endpoint():
    return render_template('index.html', data='')


@app.route("/", methods=['GET', 'POST'])
def get_prediction():
    if request.method == 'POST':
        height = request.form['height']
        prediction = model.predict([[float(height)]])
        prediction = prediction[0][0]
        prediction = str(round(float(prediction), 2))
        result = {"Predicted Weight": prediction + "Kg"}
        return render_template('index.html', data=result)


@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404
