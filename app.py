from flask import Flask, render_template
import pickle
import numpy as np

model = pickle.load(open('predictor.pkl','rb'))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)