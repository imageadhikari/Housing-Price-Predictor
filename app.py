from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('predictor.pkl','rb'))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    # HTML -> .py
    if request.method == "POST":
        name = request.form["Land Area"]

    #.py -> HTML    
    return render_template('predict.html', n = name)

if __name__=="__main__":
    app.run(debug=True)