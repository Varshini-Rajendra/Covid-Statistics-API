
from flask import Flask, render_template   
from flask import request
import requests
import http.client
import os
import sys
import json
app = Flask(__name__)#to define app as flask app

@app.route('/getpositive')
def form_submit():
	url="https://covidtracking.com/api/states"
	payload = ''
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload)
	print(type(response.text))
	pos_res=response.text
	y=json.loads(pos_res)
	print(type(y))
	z=len(y)
	print(z)
	count1=0
	for x in range(0,z):
		count1=count1+y[x]["positive"]
	res1=str(count1)
	return res1

@app.route('/getnegative')
def form_submitt():
	url="https://covidtracking.com/api/states"
	payload = ''
	headers = {}
	response2 = requests.request("GET", url, headers=headers, data=payload)
	print(type(response2.text))
	neg_res=response2.text
	yy=json.loads(neg_res)
	print(type(yy))
	zz=len(yy)
	print(zz)
	count2=0
	for cc in range(0,zz):
		count2=count2+yy[cc]["negative"]
	res2=str(count2)
	return res2

if __name__ == "__main__":#main function
	app.run(debug=True)#To start server