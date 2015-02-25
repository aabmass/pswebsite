#!/usr/bin/env python3
import os
from psbackend import app

# Start the app
if ('PRODUCTION' in os.environ and
        os.environ['PRODUCTION'] == 'TRUE'):
    app.run(debug=False, host='0.0.0.0')
else:
    app.run(debug=True)

