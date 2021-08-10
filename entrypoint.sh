#!/bin/sh
flask db migrate
flask db upgrade
# gunicorn wsgi:app -w 1 -b 0.0.0.0:80 --capture-output --log-level debug
if ["$FLASK_ENV" = "development"]
then 
	echo "Running Flask Development Server"
	flask run --host=0.0.0.0 --port=80
else
	gunicorn -w 1 --bind 0.0.0.0:80 wsgi:app --capture-output --log-level debug
fi