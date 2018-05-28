#Using Bootstrap flamework 
# from flask_bootstrap import Bootstrap
from flask import Flask, render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

#define the form as class variables
#each class vairable is assigned an object with the field type
"""
optional validators- define a list of checkers that will be applied to the data 
now is ensures that the field is not submitted empty.
"""

app=Flask(__name__)
app.debug=True
app.config['SECRET_KEY']='something key'

class NameForm(FlaskForm):
	name=StringField('Value1:',validators=[Required()])
	submit=SubmitField('Submit')



@app.route('/',methods=['GET','POST'])
def index5():
	form=NameForm()

	print(form.errors)

	if form.validate_on_submit():
		session['name']=form.name.data

		flash("submited")
		return redirect(url_for('index5'))

	return render_template('index5.html',form=form,name=session.get('name'))

if __name__ =="__main__":
	app.run()
