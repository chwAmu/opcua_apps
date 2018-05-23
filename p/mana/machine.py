dataTypelist=[
					('Bool','Bool'),
					('Sint','Sint'),
					('Int','Int'),
					('Real','Real'),
					('Dint','Dint')
	]

import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler
# formatter=Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = RotatingFileHandler('logg.log', "a+" ,maxBytes=10000000, backupCount=5)
handler.setLevel(logging.INFO)
# handler.setFormatter(formatter)