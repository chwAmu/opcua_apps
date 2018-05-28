#coding:utf-8
from flask import Flask

app=Flask(__name__)
app.debug=True

@app.route("/")
def hello():
	return  "<html><head><title> hi title</title></head><body>Hi Body</body></html>",200

if __name__ =="__main__":
	app.run()

