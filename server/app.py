# system level import
import os
import json

from flask import Flask, request
from flask_cors import CORS, cross_origin

# instantiate the app
app = Flask(__name__)

# enable CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def helloWorld():
  return "Established cross-origin world!"


@app.route("/api/caption", methods=["POST"])
def caption_image():
    """
        POST request that takes in an image and returns a caption
    """
    image = request.get_json()['image']


if __name__ == '__main__':
    """
        if current function is executed, 
        start the web api server in debug mode
    """
    app.debug = True
    app.run()
