# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os
from flask import Flask, request, abort
import sys
from argparse import ArgumentParser

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    stream = request.files['file'].stream
    img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)
    if(len(img.shape) == 3):
        height, width, channels = img.shape[:3]
    else:
        height, width = img.shape[:2]
        channels = 1
    return str(width) + "x" + str(height) + " " + str(channels) + "channels"

if __name__ == "__main__":
    #arg_parser = ArgumentParser(
    #    usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    #)
    #arg_parser.add_argument('-p', '--port', default=8000, help='port')
    #arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    #options = arg_parser.parse_args()
    #app.run(debug=options.debug, port=options.port)
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


