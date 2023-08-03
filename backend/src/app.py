# python .\app.py -i localhost -o 8000\

from flask import Flask
from flask_cors import CORS

from controllers.visionAnalysis.detectObject import detect_motion

import routes.routes
import routes.routesVideoLayer
import routes.routesParametersFilter
import routes.routesFunctionDb

import threading
import time

import cv2

app = Flask(__name__)
CORS(app)

time.sleep(2.0)

def nothing(x):
    pass

#
#Routes
#
routes.routes.init_app(app)
routes.routesVideoLayer.init_app(app)
routes.routesParametersFilter.init_app(app)
routes.routesFunctionDb.init_app(app)

#
#Threading
#
t = threading.Thread(target=detect_motion, args=())
t.daemon = True
t.start()

#
#Main
#
#check to see if this is the main thread of execution
if __name__ == '__main__':

	# start the flask app
	app.run(host="localhost", port=8000,
         	debug=True,
			threaded=True, 
            use_reloader=False
            )

cv2.destroyAllWindows()





