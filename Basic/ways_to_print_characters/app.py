# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:59:08 2020

@author: night
"""


from flask import Flask
app = Flask(__name__)

from flask import Flask, render_template


@app.route('/')
def index():
 return render_template('index.html')
@app.route('/user/<name>')
def user(name):
 return render_template('user.html', name=name)

if __name__ == '__main__':
 app.run()
