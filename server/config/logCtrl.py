

def writelog(mes):
	workinglogs=open('Result/log.txt','a')
	workinglogs.write(getCurrentTime()+'/'+mes+'\n')
	workinglogs.close()

def getCurrentTime():
	from datetime import datetime as t
	return str(t.now())

def printTerminalMessage(mes,*args):
	print('>>>'+getCurrentTime()+'/'+mes)
	if len(args) > 0:
		if args[0]==True:
			writelog(mes)
	

import logging 
import logging.config
try :
	logging.config.fileConfig('config/logging.conf')
	logger=logging.getLogger('GeneratorTemperature')
	logger2=logging.getLogger('MotorTemperature')
except(KeyError):
	print('KeyError')
	exit()
