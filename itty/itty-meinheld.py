#!/usr/bin/env python

import itty

@itty.get('/')
def hello(request):
    return 'hello world'


def meinheld_adapter(host, port):
    import meinheld
    meinheld.server.listen((host, port))
    meinheld.server.run(itty.handle_request)


if __name__ == '__main__':
    itty.WSGI_ADAPTERS['meinheld'] = meinheld_adapter
    itty.run_itty(server='meinheld', host='0.0.0.0', port=8080)


