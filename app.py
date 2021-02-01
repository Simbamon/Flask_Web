from flask import Flask, render_template
from forms import PredictionForm
from flask import json
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secretkeys'

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = PredictionForm()
    return render_template('index.html', form = form)

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    form = PredictionForm()
    if form.validate_on_submit():
        objects = [form.month.data, form.dayofweek.data, form.borough.data, form.min_humidity.data, form.max_humidity.data,
                         form.min_temp.data, form.max_temp.data, form.max_wind_speed.data, form.weather_description.data
        ]

        userInput = []
        userInput.append(objects)
        payload_scoring = {"input_data": [{"fields": ["month", "dayofweek", "borough", "min_humidity", "max_humidity", "min_temp",
                           "max_temp", "max_wind_speed", "weather_description"], 
                           "values": userInput }]}
        
        response_scoring = requests.post("", json=payload_scoring, headers=header)

        output = json.loads(response_scoring.text)

        

        
        return output
    return render_template('index.html', form = form)

