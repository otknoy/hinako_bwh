#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, request

from hinako_api.hinako import Hinako
from measurements_api.get_bwh import get_bwh

port = '/dev/cu.usbmodemfd121'
hinako = Hinako(port, 'd:3:s', 'd:4:s', 'd:5:s')


# Hinako API
@route('/hinako', method='GET')
def index():
    query = request.query

    print query

    b = int(query.b)
    hinako.set_bust(b)

    # w = int(query.w)
    # hinako.set_waist(w)

    # h = int(query.h)
    # hinako.set_hip(h)

    return 'Hinako!'


# Measurements API
@route('/get_bwh/<name>')
def index(name):
    b, w, h = get_bwh(name)
    return '{"name": %s, "bust": %s, "waist": %s, "hip": %s}' % (name, b, w, h)


# Both
@route('/query/<name>')
def index(name):
    b, w, h = get_bwh(name)
    hinako.set_bust(b)
    return '{"name": %s, "bust": %s, "waist": %s, "hip": %s}' % (name, b, w, h)


run(host='localhost', port=8080, debug=True, reloader=True)
