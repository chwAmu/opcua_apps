#coding:utf-8
from flask import Flask, render_template

app=Flask(__name__)
app.debug=True

@app.route("/")
def hello():
	print('Page is loaded..')
	return  render_template("index.html")

@app.route("/get", methods=['GET'])
def getingData():
	print('you did it.')
	return  render_template("index.html")

@app.route("/page1")
def page1():
	from opcua import Client
	print('Module is imported')
	return  render_template("page1.html")

@app.route('/page1', methods=['POST'])
def post():
    return json.dumps({"message" : "通信成功!!"})

if __name__ =="__main__":
	app.run()

