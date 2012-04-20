DATABASE_NAME = officehours
DATABASE_URL = postgresql://admin@localhost/$(DATABASE_NAME)

all: virtualenv install

virtualenv:
	virtualenv --no-site-packages .

install:
	source bin/activate && pip install -r requirements.txt

serve:
	source bin/activate && foreman start -p 5000

deploy:
	git push heroku master

createdb:
	createdb $(DATABASE_NAME)

dropdb:
	dropdb $(DATABASE_NAME)

test:
	source bin/activate && python test.py

dbversion:
	source bin/activate && python migrations/manage.py db_version $(DATABASE_URL) migrations