#Using Bootstrap flamework 
# from flask_bootstrap import Bootstrap
from flask import Flask, render_template


app=Flask(__name__)
app.debug=True

@app.route("/")
def hello():
	return  render_template("index.html")

@app.route("/page1")
def page1():
	return  render_template("page1.html")

@app.route('/user2/<name>')
def user2(name):
	return render_template("user2.html",name=name)

@app.errorhandler(404)
def page_not_found(errorDescp):
	return render_template("404.html",errorDescp=errorDescp),404

@app.errorhandler(500)
def inter_server_error(errorDescp):
	return render_template("500.html",errorDescp=errorDescp),500

if __name__ =="__main__":
	app.run()