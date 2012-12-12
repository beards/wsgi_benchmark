#!/usr/bin/env python

import bjoern


def return_hello(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ('Hello world')


if __name__ == "__main__":
    bjoern.run(return_hello, '0.0.0.0', 8080)

