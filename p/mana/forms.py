
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,DecimalField
from wtforms.validators import DataRequired,Length


class StationSetUpForm(FlaskForm):
    name=StringField('Station Name',validators=[DataRequired(),Length(min=2,max=20)])
    IP_1 = StringField('IPaddress:',validators=[DataRequired(),Length(min=7,max=20)])
    submit=SubmitField('Create')

class TagForm(FlaskForm):
	name=StringField('Tag Name',validators=[DataRequired(),Length(min=3,max=50)])
	submit=SubmitField('Create')