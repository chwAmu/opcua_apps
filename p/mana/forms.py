
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,DecimalField,SelectField
from wtforms.validators import DataRequired,Length
from mana.machine import dataTypelist


class StationSetUpForm(FlaskForm):
    name=StringField('Station Name',validators=[DataRequired(),Length(min=2,max=20)])
    IP_1 = StringField('IPaddress:',validators=[DataRequired(),Length(min=7,max=20)])
    submit=SubmitField('Create')

class TagForm(FlaskForm):

	name=StringField('Tag Name',validators=[DataRequired(),Length(min=3,max=50)])
	address=StringField('OPCUA Node:',validators=[DataRequired(),Length(min=3,max=50)])
	dataType=SelectField(u'DataType',choices=dataTypelist)
	submit=SubmitField('Create')
	deleteSubmit=SubmitField('Delete')

class delForm(FlaskForm):
	hidden_del=StringField('hiddenArea',[DataRequired()])
	submit=SubmitField('delete')

class editForm(FlaskForm):
	hidden_edit=StringField('hiddenArea',[DataRequired()])
	submit=SubmitField('edit')