from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import IntegerField, SubmitField

class PredictionForm(FlaskForm):
    month = IntegerField('Month')
    dayofweek = IntegerField('Day of Week')
    borough = IntegerField('borough')
    min_humidity = IntegerField('min_humidity')
    max_humidity = IntegerField('max_humidity')
    min_temp = IntegerField('min_temp')
    max_temp = IntegerField('max_temp')
    max_wind_speed = IntegerField('max_wind_speed')
    weather_description = IntegerField('weather_description')
    Submit = SubmitField('Predict')
    result = ''
