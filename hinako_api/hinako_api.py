#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, request

from hinako import Hinako

port = '/dev/cu.usbmodemfd121'
hinako = Hinako(port, 'd:3:s', 'd:4:s', 'd:5:s')

# Hinako API
@route('/hinako', method='GET')
def index():
    query = request.query

    print query

    b = int(query.b)
    w = int(query.w)
    h = int(query.h)

    hinako.set_bust(b)
    hinako.set_waist(w)
    hinako.set_hip(h)

    return 'hinako!'


@route('/bust/<size:int>')
def bust(size):
    hinako.set_bust(size)

@route('/waist/<size:int>')
def waist(size):
    hinako.set_waist(size)

@route('/hip/<size:int>')
def hip(size):
    hinako.set_hip(size)

run(host='localhost', port=8080, debug=True, reloader=True)
