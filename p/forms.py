
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,DecimalField
from wtforms.validators import DataRequired,Length


class StationSetUpForm(FlaskForm):
    stationName=StringField('Station Name',validators=[DataRequired(),Length(min=2,max=20)])
    IP_1 = StringField('IPaddress:',validators=[DataRequired(),Length(min=2,max=20)])
    IP_2 = StringField('', validators=[DataRequired(),Length(min=1,max=3)])
    IP_3 = StringField('', validators=[DataRequired(),Length(min=1,max=3)])
    IP_4 = StringField('', validators=[DataRequired(),Length(min=1,max=3)])
    submit=SubmitField('Create')

