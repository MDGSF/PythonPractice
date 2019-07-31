#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hello World!"


@app.route('/uploadfile', methods=['POST'])
def autoAnnotation():
    f = request.files['upload']
    content = f.read()
    print(len(content))

    print(request.form['username'], request.form['password'])

    return jsonify({"ok": "ok"}), 200


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5001)
