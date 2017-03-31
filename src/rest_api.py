import flask
from flask import Flask, request, redirect, make_response
from flask_cors import CORS
import json
import sys
import codecs
import logging
import urllib
import config

# Python2.x: Make default encoding as UTF-8
if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('UTF8')


logging.basicConfig(filename='error.log', level=logging.DEBUG)
app = Flask(__name__)
app.config.from_object('config')
CORS(app)


@app.route('/')
def heart_beat():
    return flask.jsonify({"PurposeOfLife": config.PURPOSE_OF_LIFE})


if __name__ == "__main__":
    app.run()
