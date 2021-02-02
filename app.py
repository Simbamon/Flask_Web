from flask import Flask, render_template
from forms import PredictionForm
from flask import json
import json
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secretkeys'

if __name__ == "__main__":
    app.run(debug=True)

headers = {"Content-Type": "application/x-www-form-urlencoded"}
api_key = ""
body = "apikey=" + api_key + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
 
request_token = requests.post("https://iam.bluemix.net/oidc/token", headers = headers, data= body )

access_token = json.loads(request_token.text)['access_token']
refresh_token = json.loads(request_token.text)['refresh_token']

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = PredictionForm()
    return render_template('index.html', form = form)

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    form = PredictionForm()
    if form.validate_on_submit():
        
        iam_header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        objects = [form.month.data, form.dayofweek.data, form.borough.data, form.min_humidity.data, form.max_humidity.data,
                         form.min_temp.data, form.max_temp.data, form.max_wind_speed.data, form.weather_description.data
        ]

        userInput = []
        userInput.append(objects)
        payload_scoring = {"input_data": [{"fields": ["month", "dayofweek", "borough", "min_humidity", "max_humidity", "min_temp",
                           "max_temp", "max_wind_speed", "weather_description"], 
                           "values": userInput }]}
        
        predict_value = requests.post("",json = payload_scoring , headers = iam_header)

        result = json.loads(predict_value.text)


        

        
        return result
    return render_template('index.html', form = form)

