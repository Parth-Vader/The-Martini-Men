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

@app.route('/icons')
def icons():
    return render_template('icons.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/template')
def template():
    return render_template('template.html')

@app.route('/typography')
def typography():
    return render_template('typography.html')

@app.route('/upgrade')
def upgrade():
    return render_template('upgrade.html')

@app.route('/user')
def user():
    return render_template('user.html')

def getrandomimg():
    path = os.getcwd() + "/static/drone"
    print(path)
    random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
    return random_filename

if __name__ == "__main__":
    app.run()