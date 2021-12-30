# import packages
from flask import Flask, request, render_template
# import requests
import ml


#Create app object
app = Flask(__name__, static_folder='static')

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("index.html")
            
@app.route('/predict', methods=['POST'])
def predict():
    
    try:
        city = str(request.form.get('city1'))
        ac = float(request.form.get('ac'))
        mc = float(request.form.get('mc'))
    except:
        ac = 0.0
        mc = 0.0
        
    x1 = ml.scaler.transform([[ac,mc,city]])
    y1 = round(ml.model.predict(x1)[0])
    return render_template('result.html', prediction_value=' {}'.format(y1))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)