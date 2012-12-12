DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
uwsgi --uwsgi-socket /tmp/uwsgi.sock --umask 000 --pythonpath $DIR --module application:app --master --processes 9 --disable-logging

