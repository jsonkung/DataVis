#!/usr/bin/env python
from datavis import app

# Constants
# ------------------------------------------------------------------------------
PORT = 3000            # Port to run local webserver
THREADED = True        # Use threading  (True/False)
DEBUG = True           # Use debug mode (True/False)

if __name__ == "__main__":
    # tf.logging.set_verbosity(tf.logging.INFO)
    # tf.app.run()
    print("Starting webserver")
    app.config['APPLICATION_ROOT'] = "static"
    app.run(host='0.0.0.0', debug=DEBUG, port=PORT, threaded=THREADED)
