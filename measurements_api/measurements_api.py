#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, request, static_file
from bottle import TEMPLATE_PATH, jinja2_template as template
TEMPLATE_PATH.append('./views')

from get_bwh import get_bwh

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route('/<name>')
def index(name):
    b, w, h = get_bwh(name)
    return '{"name": %s, "bust": %s, "waist": %s, "hip": %s}' % (name, b, w, h)

@route('util')
def util():
    return template('index.j2', title="Yahoo! Japan", default_keyword=u"佐野ひなこ")

@route('/util/search', method='GET')
def search():
    query = (request.query).query

    b, w, h = get_bwh(query.encode('utf-8'))

    return template('search_result.j2', title="Search Result", name=query, b=b, w=w, h=h)


run(host='localhost', port=8080, debug=True, reloader=True)
