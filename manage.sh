#!/bin/bash
set -e

export DJANGO_SETTINGS_MODULE=settings_prod
export DJANGO_SECRET=2O41D6S8G0%si7IE2B11p3Z39M4DuN726Wl0qAOp6~186765V
export DATABASE_NAME=dbcjmnjzfrvk10
export DATABASE_USER=ueaqktcgzefgy
export DATABASE_PASSWORD=!ExamplePass!
export EMAIL_HOST_USER=no-reply@construction_site_sample.com
export MANDRILL_API_KEY=5Asnwtx61J8K6KE4Dm4Q8w

exec python manage.py $@
