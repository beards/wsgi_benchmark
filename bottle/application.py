#!/usr/bin/env python

import os
from bottle import Bottle

app = Bottle(__name__)

@app.route('/')
def hello():
    return "Hello World! It's Bottle!"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 7777.
    port = int(os.environ.get('PORT', 7777))
    app.run(host='0.0.0.0', port=port)
