#Authors: Abrahim and Max

from flask import Flask, render_template
import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import os
 
app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

 
GPIO.setmode(GPIO.BCM)
DHT11_pin = 4
 
@app.route("/")
def main():
   return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/project.html")
def project():
    return render_template('project.html')

@app.route("/countries.html")
def countries():
    return render_template('countries.html')
 
# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<pin>/<action>")
def action(pin, action):
   temperature = ''
   humidity = ''
 
   if pin == "dhtpin" and action == "get":
      humi, temp = dht.read_retry(dht.DHT11, DHT11_pin)  # Reading humidity and temperature
      humi = '{0:0.1f}' .format(humi)
      temp = '{0:0.1f}' .format(temp)
      temperature = 'Temperature: ' + temp 
      humidity =  'Humidity: ' + humi
 
   templateData = {
   'temperature' : temperature,
   'humidity' : humidity
   }
 
   return render_template('sensor.html', **templateData)
 
if __name__ == ("__main__"):
   app.run(host='0.0.0.0', port=80, debug=True)



