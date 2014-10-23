#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 van <van@vanleno>
#
# Distributed under terms of the MIT license.

"""
test flask
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")

def hello_world():
    return "Hello, World!"

@app.route("/test/<search_query>")
def search(search_query):
    return search_query

#@app.route("/integer/<int:v>")
#@app.route("/integer/<int:value>")
#def int_type(value):
    #print value+1
    ##print v*v
    #return "ok"
@app.route("/integer/<int:value>")
def int_type(value):
    r = value ** 3
    return 'v %d' % r

@app.route("/float/<float:value>")
def float_type(value):
    r = value ** 3
    return 'v %f' % r

@app.route("/path/<path:value>")
def path_type(value):
    return 'v %s' % value 

@app.route("/name/<name>")
def index(name):
    if name.lower() == 'mike':
        return "Hello, {}".format(name), 200
    else :
        return "нет ничего", 404
    

    return search_query
if __name__ == "__main__":
    app.debug = True
    app.run()

