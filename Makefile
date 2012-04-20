DATABASE_NAME = officehours
DATABASE_URL = postgresql://admin@localhost/$(DATABASE_NAME)
MIGRATE_PATH = migrations/manage.py
ENV = DATABASE_URL=$(DATABASE_URL)

all: virtualenv install createdb add_version_control migrate

virtualenv:
	virtualenv --no-site-packages .

install:
	source bin/activate && pip install -r requirements.txt

clean: dropdb
	rm -rf bin lib include man share .Python

serve:
	source bin/activate && foreman start -p 5000

shell:
	source bin/activate && DATABASE_URL=$(DATABASE_URL) ipython

deploy:
	git push heroku master

createdb:
	createdb $(DATABASE_NAME)

dropdb:
	dropdb $(DATABASE_NAME)

migrate:
	source bin/activate && $(ENV) python $(MIGRATE_PATH) upgrade

add_version_control:
	source bin/activate && $(ENV) python $(MIGRATE_PATH) version_control

version:
	source bin/activate && $(ENV) python $(MIGRATE_PATH) version

testmigrate:
	source bin/activate && $(ENV) python $(MIGRATE_PATH) test

dbversion:
	source bin/activate && $(ENV) python $(MIGRATE_PATH) db_version