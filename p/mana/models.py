# import the SQL library
from mana import db,app
from datetime import datetime
from mana.datalog import writelog

#db structure

class Tag(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(50),unique=True,nullable=False)
	address=db.Column(db.String(50),nullable=False)
	datatype=db.Column(db.String(20),nullable=False)

class Station(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(15),unique=True,nullable=False)
	ip=db.Column(db.String(15))


def writedb(col):
	db.session.add(col)
	db.session.commit()

def deldb(col):
	db.session.delete(col)
	db.session.commit()

