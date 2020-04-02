"""
With hello-gpio.py running, when you point your web browser to your Raspberry Pi's IP address, 
you should see the standard "Hello World!" page we created before. But add /readPin/24 to the 
end of the URL, so that it looks something like http://10.0.1.103/readPin/24. A page should 
display showing that the pin is being read as low. Now hold down the button connected to pin 
24 and refresh the page; it should now show up as high!
"""
from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('gpio-main.html', **templateData)

@app.route("/readPin/<pin>")
def readPin(pin):
   try:
      GPIO.setup(int(pin), GPIO.IN)
      if GPIO.input(int(pin)) == True:
         response = "Pin number " + pin + " is high!"
      else:
         response = "Pin number " + pin + " is low!"
   except:
      response = "There was an error reading pin " + pin + "."

   templateData = {
      'title' : 'Status of Pin' + pin,
      'response' : response
      }

   return render_template('pin.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)