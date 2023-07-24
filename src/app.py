# python .\app.py -i localhost -o 8000\

from flask import Flask

from controllers.detectMotion import detect_motion

import routes.routes

import threading
import argparse
import time

import cv2

app = Flask(__name__)
 
time.sleep(2.0)

def nothing(x):
    pass

routes.routes.init_app(app)

t = threading.Thread(target=detect_motion, args=())
t.daemon = True
t.start()

    # check to see if this is the main thread of execution
if __name__ == '__main__':
	# # construct the argument parser and parse command line arguments
	# ap = argparse.ArgumentParser()
	# ap.add_argument("-i", "--ip", type=str, required=True,
	# 	help="ip address of the device")
	# ap.add_argument("-o", "--port", type=int, required=True,
	# 	help="ephemeral port number of the server (1024 to 65535)")
	# ap.add_argument("-f", "--frame-count", type=int, default=32,
	# 	help="# of frames used to construct the background model")
	# args = vars(ap.parse_args())
	
	# # start the flask app
	# app.run(host=args["ip"], port=args["port"], debug=True,
	# 	threaded=True, use_reloader=False)
        
		# start the flask app
	app.run(host="localhost", port=8000,
		threaded=True, use_reloader=False)

cv2.destroyAllWindows()








