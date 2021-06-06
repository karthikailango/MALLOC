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
           num = result
      num=num.replace(',','')
      num=int(num)
      if (num<=200000):
      	result="Your salary is less then 2lak"
      elif (num>200000 and num<=500000):
      	result="Your salary is 2lakh - 5lakh"
      elif (num>500000 and num<=1500000):
      	result="Your salary is 5lakh - 15lakh"
      elif (num>1500000 and num<2000000):
      	result="Your salary is 15lakh - 20lakh"
      else:
          result = "Your salary is 20 lakh and above"
      return render_template("result.html",result = result)

if _name_ == '_main_':
  app.run(debug = True)
