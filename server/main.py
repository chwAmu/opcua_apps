#coding:utf-8
from flask import Flask,render_template,jsonify
from opcua import Client
import sys
import signal
import logging,logging.config

from multiprocessing import Process
from time import sleep as timer
from config import xmlConfigRead

c=Client('opc.tcp://192.168.0.1:4840')
loggingconfig=xmlConfigRead.XMLConfiger()


app=Flask(__name__)



def handler(signal,frame):
	exitserver()

def exitserver():
	try:
		c.disconnect()
	except Exception as e:
		p1.terminate()
		p2.terminate()
	sys.exit(0)

def start2runserver():
	c.connect()
	signal.signal(signal.SIGINT,handler)
	opendefaultbrowser('http://127.0.0.1:5000/')
	app.run()

def opendefaultbrowser(url):
	import webbrowser
	webbrowser.open(url)

def getdata():
	#config the loogger
	c.connect()
	signal.signal(signal.SIGINT,handler)
	logging.config.fileConfig('logging.conf')
	gtlogger=logging.getLogger('GeneratorTemperature')
	mtlogger=logging.getLogger('MotorTemperature')
	hpglogger=logging.getLogger('HelpingGearBox')
	splogger=logging.getLogger('Spare')
	while True:
		x=len(loggingconfig.getNameList())

		for i in range(x):
			y=len(loggingconfig.getNodeNamelist()[i])
			for k in range(y):					
				naa=c.get_node(loggingconfig.getNodeNamelist()[i][k])
				nodename=loggingconfig.getNodeList()[i][k]
				nodevalue=round(naa.get_data_value().Value.Value,2)
				msg=nodename+'/'+str(nodevalue)
				if i==0:
					gtlogger.info(msg)
				elif i==1:
					mtlogger.info(msg)
				elif i==2:
					hpglogger.info(msg)
				elif i==3:
					splogger.info(msg)
		timer(1)

@app.route("/")
def hello():
	return  render_template("index5.html")

@app.route("/get",methods=['GET'])
def hello2():
	return jsonify(getvalue1(c))

def getvalue1(client):
	x=len(loggingconfig.getNameList())
	y=len(loggingconfig.getNodeNamelist()[0])	
	count=0
	retunrlist1=[0 for x in  range(32)]
	for i in range(x):
		for k in range(y):					
			naa=client.get_node(loggingconfig.getNodeNamelist()[i][k])
			nodename=loggingconfig.getNodeList()[i][k]
			nodevalue=round(naa.get_data_value().Value.Value,1)
			retunrlist1[count]=nodevalue
			count=count+1
	return retunrlist1	

@app.route("/tes2")
def test2():
	items = []
	for i in range(1, 11):
	    i = str(i)

	    # dict == {}
	    # you just don't have to quote the keys
	    an_item = dict(date="2012-02-" + i, id=i, position="here", status="waiting")
	    items.append(an_item)

		# ... your code here ...
	return  render_template("index.html",items=items)


if __name__ =="__main__":
	p1=Process(target=start2runserver)
	p1.start()
	p2=Process(target=getdata)
	p2.start()
	p1.join()
	p2.join()

