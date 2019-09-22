import time

from app import app
from flask import request, abort, jsonify,redirect, url_for, session, make_response
import base64

import hmac
import hashlib

@app.route('/api/base')
def base():
    return 'Hello, world'

@app.route('/api/upload', methods=['POST'])
def uploadFile():
	file = request.files['file']
	print(request)
	print("-------------------------------")
	print(file)
	return "hello"