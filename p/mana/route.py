from mana.models import Tag,Station
from mana import app,db
from flask import Flask, render_template, redirect, url_for, request,flash
from mana.forms import StationSetUpForm,TagForm

@app.route("/")
def home():
    return render_template("home.html",title='Home')

@app.route("/formtest", methods=['GET','POST'])
def formtest():
    form=StationSetUpForm()
    if form.validate_on_submit():
    	duip=Station.query.filter_by(name=form.name.data).first()
    	if duip is None:
	    	# st=station.query.filter_by()
	    	station=Station(name=form.name.data,ip=form.IP_1.data)
	    	db.session.add(station)
	    	db.session.commit()
	    	flash('data is added.','success')
	    	return redirect(url_for('formtest'))
    	else:
	    	flash('data can not added','danger')
	    	stations=Station.query.all()
    return render_template("formtest.html",form=form,title='Station',stations=stations)