#!/usr/bin/env flask

import datetime
import os
import random
import socket
import sys

data = {}
data['hostname'] = 'unknown-host'
data['ip_address'] = 'unknown-ip'

try:
  data['hostname'] = socket.gethostname()
  data['ip_address'] = socket.gethostbyname(data['hostname'])
except Exception as e:
  print('Error: Unable to decipher hostname/ip_address', e)

data['container_name'] = os.environ.get('NAME', 'unknown')
data['now'] = str(datetime.datetime.now())

from flask import Flask, render_template, jsonify


app = Flask(data['container_name'])

def get_random_color():
  return random.choice(['#E0BBE4', '#FFDFD3', '#A0D7D9', '#F4CBA1', '#D6FFC7', '#C3BCCF', '#bbbcc2', '#def3fd'])

data['bg_color'] = get_random_color()

@app.route('/')
def get_root():
  return render_template('index.html', data=data)

@app.route('/ping')
def do_ping():
  return jsonify({'message': 'pong', 'time': data['now'] })

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
