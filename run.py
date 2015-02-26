#!/usr/bin/env python3
import os, sys

from psbackend import app, config

# Start the app
if config.environment == "production":
    app.run(debug=False, host='0.0.0.0')
elif config.environment == "debug":
    app.run(debug=True)
else:
    print("Please specifiy a valid value for \'environment\' in config.py\n"
          "(\'{}\' is not valid)".format(config.environment))
    sys.exit(1)
