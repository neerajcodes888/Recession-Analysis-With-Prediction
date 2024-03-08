from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('Recession_Model')

@app.route('/')

def home():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')