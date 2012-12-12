DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
uwsgi --socket 127.0.0.1:3031 --pythonpath $DIR --module application:app --master --processes 9 --disable-logging
