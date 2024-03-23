pip-freeze:
	fig run --rm web pip freeze > requirements.txt

resetdb:
	fig run --rm postgres psql -h postgres -U postgres -c "DROP DATABASE IF EXISTS django;"
	fig run --rm postgres psql -h postgres -U postgres -c "CREATE database django;"
	fig run --rm web python manage.py migrate
	fig run --rm web python manage.py createsuperuser

makemigrations:
	fig run --rm web python manage.py makemigrations

migrate:
	fig run --rm web python manage.py migrate

makemessages:
	fig run --rm web python manage.py makemessages -l es_AR --no-wrap

compilemessages:
	fig run --rm web python manage.py compilemessages

collectstatic:
	fig run --rm web python manage.py collectstatic --noinput

shell:
	fig run --rm web python manage.py shell_plus

build-frontend:
	fig -f fig-development.yml run --rm frontend build --production

deploy:
	git pull
	fig build
	fig up -d
	make migrate
	make build-frontend
	make collectstatic

remote-deploy:
	git pull
	fig build frontend
	docker run --rm -v "$(shell pwd)/static-compiled":/app/static-compiled construction_site_sample_frontend build --production
	rsync -arhv --progress "$(shell pwd)"/static-compiled/* honi@tomate.bek.io:/srv/www/production/construction_site_sample.com/static-compiled
	ssh honi@tomate.bek.io ' \
		cd /srv/www/production/construction_site_sample.com; \
		source venv/bin/activate; \
		git pull; \
		./manage.sh collectstatic --noinput; \
		./manage.sh migrate; \
		kill -hup `cat tmp/gunicorn.pid`'

.PHONY: resetdb makemigrations migrate makemessages compilemessages collectstatic shell build-frontend deploy
