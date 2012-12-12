#!/usr/bin/env python

import sys
import os
import multiprocessing

proc_name = 'gunicorn-meinheld_test'


def app(environ, start_response):
    data = 'Hello World - by Gunicorn[meinheld]'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]

    start_response(status, response_headers)

    return [data]


def stop_server():
    os.system('pkill -f %s' % proc_name)


def main():
    command_list = [
        'gunicorn', 'gunicorn-test:app',
        '--name', proc_name,
        '--bind', '0.0.0.0:$PORT',
        '--workers', str(multiprocessing.cpu_count() * 2 + 1),
        '--worker-class', 'meinheld.gmeinheld.MeinheldWorker',
    ]
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == 'stop':
            stop_server()
            sys.exit(1)
        elif arg in ['start', 'restart', ]:
            stop_server()
            command_list.extend(['--daemon', '--pid=pidfile'])
    command = ' '.join(command_list)
    print command
    os.system(command)


if __name__ == '__main__':
    main()

