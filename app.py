from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('Recession_Model')

@app.route('/')

def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        year=int(request.form['year'])
        gdp=float(request.form['gdp'])
        inflation=
        
    
    
    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')