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

def getdroneimg():
    path = os.getcwd() + "/static/drone"
    name = str(random.randint(1,35)) + '.jpg'

    return os.path.join(path,name)

def gettweetimg():
    path = os.getcwd() + "/static/twitter"
    name = str(random.randint(1,33)) + '.jpg'

    return os.path.join(path,name)

def getlatlon():
    lat1 = 20.5
    lat2 = 22.5
    lon1 = 82.5
    lon2 = 87.5
    lat = random.uniform(lat1,lat2)
    lon = random.uniform(lon1,lon2)
    
    return [round(lat,1),round(lon,1)]


if __name__ == "__main__":
    app.run()