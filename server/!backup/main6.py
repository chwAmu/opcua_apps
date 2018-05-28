#Using Bootstrap flamework 
from flask_bootstrap import Bootstrap
from flask import Flask, render_template


app=Flask(__name__)
app.debug=True
bootstrap=Bootstrap(app)

@app.route("/")
def hello():
	return  render_template("index.html")

@app.route("/page1")
def page1():
	return  render_template("page1.html")

@app.route('/user1/<name>')
def user1(name):
	return render_template("user1.html",name=name)


if __name__ =="__main__":
	app.run()