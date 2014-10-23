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

if __name__ == "__main__":
    app.run()

