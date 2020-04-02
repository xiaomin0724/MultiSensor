from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
    return render_template('index.html', **templateData)
    
@app.route('/Menu')
def Menu():
    return render_template('Menu.html')

# @app.route('/hello/<name>') - the <name> part means it passes the name into the hello function as a variable called name
@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')