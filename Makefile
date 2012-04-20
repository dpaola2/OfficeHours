DATABASE_NAME = officehours
DATABASE_URL = postgresql://admin@localhost/$(DATABASE_NAME)
MIGRATE_PATH = officehours/migrations/manage.py
ENV = DATABASE_URL=$(DATABASE_URL)
ACTIVATE = source bin/activate

all: virtualenv install createdb add_version_control migrate

virtualenv:
	virtualenv --no-site-packages .

install:
	source bin/activate && pip install -r requirements.txt

clean: dropdb
	rm -rf bin lib include man share build .Python

serve:
	$(ACTIVATE) && foreman start -p 5000

shell:
	$(ACTIVATE) && DATABASE_URL=$(DATABASE_URL) ipython

deploy:
	git push heroku master

createdb:
	createdb $(DATABASE_NAME)

dropdb:
	dropdb $(DATABASE_NAME)

migrate:
	$(ACTIVATE) && $(ENV) $(MIGRATE_PATH) upgrade

add_version_control:
	$(ACTIVATE) && $(ENV) $(MIGRATE_PATH) version_control

version:
	$(ACTIVATE) && $(ENV) $(MIGRATE_PATH) version

testmigrate:
	$(ACTIVATE) && $(ENV) $(MIGRATE_PATH) test

dbversion:
	$(ACTIVATE) && $(ENV) $(MIGRATE_PATH) db_version