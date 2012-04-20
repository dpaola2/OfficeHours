#! /usr/bin/env python

import os
from flask import Flask, flash, render_template, request
from models import Day, Slot, Session

app = Flask(__name__)

PORT = int(os.environ.get("PORT", '5000'))

@app.route('/')
def index():
    days = Day.days_ahead(7)
    return render_template('index.html', days=days)

@app.route('/reserve/<int:slot_id>', methods=['POST'])
def reserve(slot_id):
    attrs = {
        'name': None,
        'email': None,
        'skype': None
    }
    
    for key in attrs.keys():
        attrs[key] = request.form.get(key, None)
        if attrs[key] == "":
            return "Missing: %s" % key

    sess = Session()
    slot = sess.query(Slot).filter_by(id=slot_id).scalar()
    if slot is None:
        return "Invalid slot"

    slot.reserve(attrs)
    sess.add(slot)
    sess.commit()
    return "yep"

app.debug = True
app.run(host='0.0.0.0', port=PORT)
