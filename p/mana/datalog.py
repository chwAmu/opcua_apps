from mana import app
import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler
format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='error.log',level=logging.INFO,format=format)


def writelog(message):
	app.logger.info(message)