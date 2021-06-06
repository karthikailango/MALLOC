# -- coding: utf-8 --
"""
Spyder Editor
Created on Sat Jun  5 15:00:04 2021
@authour Kokila Manogar
This is a temporary script file.
"""
from flask import Flask, render_template, request
app = Flask(_name_)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      string = result
      string=string.upper()
      print(string)
      result = 'You have '
      myList=['DIABETES', 'THYROID', 'CANCER', 'NO']
      if 'DIABETES' in string:
      	result+=' Diabetes'
      if "THYROID" in string:
      	result+=' Thyroid'
      if 'CANCER' in string:
      	result+=' Cancer'
      if "NO" in string:
      	result=" No disease"
      if [True for x in myList if x in string]:
      	result+=' Others'
      return render_template("result.html",result = result)

if _name_ == '_main_':
   app.run(debug = True)
