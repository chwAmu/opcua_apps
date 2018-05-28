#Using Bootstrap flamework 
# from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

#define the form as class variables
#each class vairable is assigned an object with the field type
"""
optional validators- define a list of checkers that will be applied to the data 
now is ensures that the field is not submitted empty.
"""
class NameForm(Form):
	name=StringField('Value1:',validators=[Required()])
	submit=SubmitField('Submit')

app=Flask(__name__)
app.debug=True
app.config['SECRET_KEY']='something key'

@app.route('/',methods=['GET','POST'])
def index():
	name=None

	form=NameForm()
	if form.validate_on_submit():
		name=form.name.data
		form.name.data=''
	return render_template('index5.html',form=form,name=form.name.data)

if __name__ =="__main__":
	app.run()
