#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, request

from hinako import Hinako

port = '/dev/cu.usbmodemfa131'
hinako = Hinako(port, 'd:3:s', 'd:4:s', 'd:5:s')


# Hinako API
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
