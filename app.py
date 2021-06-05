# -*- coding: utf-8 -*-
"""
Spyder Editor
Created on Sat Jun  5 15:00:04 2021
@authour Kokila Manogar
This is a temporary script file.
"""
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
