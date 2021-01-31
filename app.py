from flask import Flask, render_template
from forms import PredictionForm

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
        python_object = [form.month.data, form.dayofweek.data]
        userInput = []
        userInput.append(python_object)
        payload_scoring = {"input_data": [{"fields": ["month", "dayofweek", "d"], 
        "values": userInput }]}
        output = payload_scoring

        return output
    return render_template('index.html', form = form)

