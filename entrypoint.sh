#! /bin/sh
FLASK_APP=app
ENV1=production
pipenv shell
pipenv run flask run --host=0.0.0.0