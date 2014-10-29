#!flask/bin/python
#-*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
from app import app


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if '/' in path:
        pathl = path.split('/')
    else:
        pathl = [path]

    if pathl[0] == 'resources':
        if pathl[1] == 'bagfile':
            return redirect(url_for('static', filename='resources/2014-09-11-15-38-36.bag'))

    return 'You want path: %s <br> <br> %s' % (path, '')
