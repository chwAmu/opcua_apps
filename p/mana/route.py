from mana.models import Tag,Station
from mana import app,db
from flask import Flask, render_template, redirect, url_for, request,flash
from mana.forms import StationSetUpForm,TagForm,delForm,editForm

@app.route("/")
def home():
    return render_template("home.html",title='Home')

# station
@app.route("/formtest", methods=['GET','POST'])
def formtest():
    form=StationSetUpForm()
    stations=Station.query.all()
    if form.validate_on_submit():
    	duip=Station.query.filter_by(name=form.name.data).first()
    	if duip is None:
	    	station=Station(name=form.name.data,ip=form.IP_1.data)
	    	db.session.add(station)
	    	db.session.commit()
	    	flash('data is added.','success')
	    	return redirect(url_for('formtest'))
    	else:
	    	flash('data can not added','danger')
    return render_template("formtest.html",form=form,title='Station',stations=stations)

# tag
@app.route("/tagOper",methods=['GET','POST'])
def tagOper():

    form=TagForm()
    dform=delForm()
    eform=editForm()

    tags=Tag.query.all()

    if eform.validate_on_submit():
        print('edit')
        return render_template()
        return redirect(url_for('tagOper'))

    if dform.validate_on_submit():
        print('go')
        dup=Tag.query.filter_by(name=dform.hidden_del.data).all()
        for d in dup:
            db.session.delete(d)
        db.session.commit()
        flash('tag is delected!','danger')
        return redirect(url_for('tagOper'))

    elif form.validate_on_submit():
        duip=Tag.query.filter_by(name=form.name.data).first()
        if duip is None:
            tag=Tag(name=form.name.data,datatype=form.dataType.data,address=form.address.data)
            db.session.add(tag)
            db.session.commit()
            flash('tag is added','success')
            return redirect(url_for('tagOper'))
        else:
            flash('tag can not added','danger')

    elif eform.validate_on_submit():
        pass


    return render_template("tagOper.html",form=form,title='Tag',tags=tags,dform=dform,eform=eform)


@app.route('/tagEdit/<int:tag_id>/edit',methods=['GET','POST'])
def tagEdit(tag_id):
    form=TagForm()
    tag=Tag.query.get_or_404(tag_id)

    if request.method=='GET':
        form.name.data=tag.name
        form.address.data=tag.address
        form.dataType.data=tag.datatype


    return render_template('tagEdit.html',title='edit tag',form=form)








