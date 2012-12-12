#!/usr/bin/env python

import sys
import os
import multiprocessing

PROC_NAME = 'gunicorn-test'


def stop_server():
    os.system('pkill -f %s' % PROC_NAME)


def main():
    port = int(os.environ.get('PORT', 7777))
    command_list = [
        'gunicorn', 'application:app',
        '--name', PROC_NAME,
        '--bind', '0.0.0.0:%d' % port,
        '--workers', str(multiprocessing.cpu_count() * 2 + 1),
        '--error-logfile', 'errlog',
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

