DATABASE_NAME = officehours
DATABASE_URL = postgresql://admin@localhost/$(DATABASE_NAME)
MIGRATIONS_REPO = migrations
MIGRATE_PATH = migrations/manage.py

all: virtualenv install createdb migrate

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
	source bin/activate && python $(MIGRATE_PATH) upgrade $(DATABASE_URL) $(MIGRATIONS_REPO)

version:
	source bin/activate && python $(MIGRATE_PATH) version $(MIGRATIONS_REPO)

testmigrate:
	source bin/activate && python $(MIGRATE_PATH) test $(DATABASE_URL) $(MIGRATIONS_REPO)

dbversion:
	source bin/activate && python $(MIGRATE_PATH) db_version $(DATABASE_URL) $(MIGRATIONS_REPO)