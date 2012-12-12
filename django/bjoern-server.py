#!/usr/bin/env python

import os
port = int(os.environ.get('PORT', 7777))

import bjoern
from application import wsgi
bjoern.run(wsgi.application, '0.0.0.0', port)

