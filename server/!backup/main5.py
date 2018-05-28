from flask import Flask, render_template

app=Flask(__name__)
app.debug=True

@app.route("/")
def hello():
	return  render_template("index.html")

@app.route("/page1")
def page1():
	return  render_template("page1.html")

@app.route('/user/<name>')
def user(name):
	return render_template("user.html",name=name)


if __name__ =="__main__":
	app.run()