from mana.models import Tag,Station,writedb,deldb
from mana import app,db
from flask import Flask, render_template, redirect, url_for, request,flash
from mana.forms import StationSetUpForm,TagForm,delForm
from mana.datalog import writelog

currentStation=''

@app.route("/")
def home():
    return render_template("home.html",title='Home')

# station
@app.route("/formtest", methods=['GET','POST'])
def formtest():
    dform=delForm()
    form=StationSetUpForm()
    stations=Station.query.all()
    if form.validate_on_submit():
        duip=Station.query.filter_by(name=form.name.data).first()
        if duip is None:
            station=Station(name=form.name.data,ip=form.IP_1.data)
            writedb(station)
            flash('data is added.','success')
            writelog('station: '+form.name.data+' is added.')
            return redirect(url_for('formtest'))

        else:
            writelog('station: '+form.name.data+' can not be added because the stationName is existed.')
            flash('data can not added','danger')
    elif dform.validate_on_submit():
        sts=Station.query.filter_by(name=dform.hidden_del.data).first()
        deldb(sts)
        writelog('station: '+dform.hidden_del.data+' is deleted')
        flash('station is deleted..','danger')
        return redirect('formtest')
    return render_template("formtest.html",form=form,title='Station',stations=stations,dform=dform)

@app.route('/stationEdit/<int:station_id>',methods=['GET','POST'])
def stationEdit(station_id):
    form=StationSetUpForm()
    station=Station.query.get_or_404(station_id)

    if request.method=='GET':
        form.name.data=station.name
        form.IP_1.data=station.ip
    elif request.method=='POST':
        station.name=form.name.data
        station.ip=form.IP_1.data
        writedb(station)
        return redirect(url_for('formtest'))

    return render_template('stationEdit.html',title='station edit',form=form,station_id=station.id,station=station)

# tag
@app.route("/tagOper",methods=['GET','POST'])
def tagOper():

    form=TagForm()
    dform=delForm()
    tags=Tag.query.all()

    if dform.validate_on_submit():
        dup=Tag.query.filter_by(name=dform.hidden_del.data).first()
        if dup:
            deldb(dup)
            writelog('node:'+dform.hidden_del.data+' is deleted.')
            flash('tag is deleted!','danger')
            return redirect(url_for('tagOper'))

    elif form.validate_on_submit():
        duip=Tag.query.filter_by(name=form.name.data).first()
        if duip is None:
            tag=Tag(name=form.name.data,datatype=form.dataType.data,address=form.address.data)
            writedb(tag)
            flash('tag is added','success')
            return redirect(url_for('tagOper'))
        else:
            flash('tag can not added','danger')

    return render_template("tagOper.html",form=form,title='Tag',tags=tags,dform=dform)


@app.route('/tagEdit/<int:tag_id>',methods=['GET','POST'])
def tagEdit(tag_id):
    form=TagForm()
    tag=Tag.query.get_or_404(tag_id)

    if request.method=='GET':
        form.name.data=tag.name
        form.address.data=tag.address
        form.dataType.data=tag.datatype
    elif request.method=="POST":
        tag.name=form.name.data
        tag.datatype=form.dataType.data
        tag.address=form.address.data
        writedb(tag)
        return redirect(url_for('tagOper'))

    return render_template('tagEdit.html',title='edit tag',form=form,tag_id=tag.id,tag=tag)


@app.route('/tagView')
def tagView():


    return render_template('tagView.html',title='tag View')






