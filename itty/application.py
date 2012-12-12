#!/usr/bin/env python

import itty

@itty.get('/')
def hello(request):
    return "Hello World! It's itty!"

app = itty.handle_request


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 7777.
    import os
    port = int(os.environ.get('PORT', 7777))
    itty.run_itty(host='0.0.0.0', port=port)
