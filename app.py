from flask import Flask, render_template
import os
import random

app = Flask(__name__,static_url_path='/static')

@app.route("/")

def main():
    return render_template('dashboard.html')

@app.route("/dashboard")

def dashboard():
    return render_template('dashboard.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/chat')
def chat():
    return render_template('template.html')

@app.route('/broadcast')
def broadcast():
    return render_template('template.html')

def getrandomimg():
    path = os.getcwd() + "/static/drone"
    print(path)
    random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
    return random_filename

if __name__ == "__main__":
    app.run()