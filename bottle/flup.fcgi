#!/usr/bin/env python

from flup.server.fcgi import WSGIServer
from application import app

if __name__ == '__main__':
    WSGIServer(
        app, bindAddress='/tmp/fcgi.sock', umask=000,
        maxSpare=300, minSpare=2, maxThreads=650
    ).run()
