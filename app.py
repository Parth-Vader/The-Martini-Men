import random
from random import choice
from flask import Flask, render_template,url_for
from flask import request
from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models
import os
from werkzeug.utils import secure_filename
import shutil

app = Flask(__name__,static_url_path='/static')

# For Custom Vision
training_key = "3df4462657d8403090db9cb591a7e285"
prediction_key = "3cb74b07eb924c75b11888bc64c776e4"
projectid="7fa336ce-fb4d-49b0-a44a-46fce8c90483"

predictor = prediction_endpoint.PredictionEndpoint(prediction_key)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")

def main():
    return render_template('dashboard.html')

@app.route("/dashboard")

def dashboard():
    return render_template('dashboard.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route('/uploadman', methods=['POST'])
def upload_file():
    isfile=False
    results = []
    if request.method == 'POST':
        f = request.files['photo']	
        isfile=True
        target = os.path.join(APP_ROOT,'./static')
        #print(target)
        filename = secure_filename(f.filename)
        destination = "/".join([target,filename])
        #print(destination)
        f.save(destination)

        ff = open(destination,'rb')
        results = predictor.predict_image(projectid, ff) # was 'ff'
        ff.close()
    return render_template('upload.html',isfile=isfile,predictions=results.predictions,fname=filename)

@app.route('/uploaddrone', methods=['POST'])
def getrandomdrone():
    isfile=True
    name = str(random.randint(1,35)) + '.jpg'
    temp = '/'.join(['static/drone',name])
    target = os.path.join(APP_ROOT,temp)
    print(target)
    ff = open(target,'rb')
    results = predictor.predict_image(projectid, ff) # was 'ff'
    staticpath = os.path.join(APP_ROOT,'./static/')
    shutil.copy(target,staticpath+'d'+name)
    ff.close()

    return render_template('upload.html',isfile=isfile,predictions=results.predictions,fname='d'+name)

@app.route('/uploadtweet', methods=['POST'])
def gettweetimg():
    isfile=True
    name = str(random.randint(1,33)) + '.jpg'
    temp = '/'.join(['static/twitter',name])
    target = os.path.join(APP_ROOT,temp)
    print(target)
    ff = open(target,'rb')
    results = predictor.predict_image(projectid, ff) # was 'ff'
    staticpath = os.path.join(APP_ROOT,'./static/')
    shutil.copy(target,staticpath+'t'+name)
    ff.close()

    return render_template('upload.html',isfile=isfile,predictions=results.predictions,fname='t'+name)


@app.route('/chat')
def chat():
    return render_template('template.html')

if __name__ == "__main__":
    app.run()