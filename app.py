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
        inflation=float(request.form['inflation'])
        ip=float(request.form['ip'])
        job=int(request.form['job'])
        quarter = request.form['quarter']
        if (quarter=='First Quarter'):
            quarter=1
        elif(quarter=='Second Quarter'):
            quarter=2
        elif(quarter=='Third Quarter'):
            quarter=3
        else:
            quarter=4
            
        prediction = model.predict([[year,quarter,gdp,inflation,ip,job]])
        
        if(prediction == 1):
            prediction="Recession will  happen by your given circumstances"
        else:
            prediction="Recession won't  happen by your given circumstances"
        
        return render_template("prediction.html", prediction_text="{}".format(prediction))
    
    
    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')