#! /usr/bin/env python

import os
from flask import Flask, flash, render_template
from models import Day

app = Flask(__name__)

PORT = int(os.environ.get("PORT", '5000'))

@app.route('/')
def index():
    days = Day.days_ahead(7)
    return render_template('index.html', days=days)

app.run(host='0.0.0.0', port=PORT)
