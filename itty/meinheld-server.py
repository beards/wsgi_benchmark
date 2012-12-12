#!/usr/bin/env python

import os
port = int(os.environ.get('PORT', 7777))

from meinheld import server
from application import app 
server.listen(("0.0.0.0", port))
server.set_access_logger(None)
server.run(app)

