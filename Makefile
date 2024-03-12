#!/bin/bash
.PHONY: default
.SILENT:


default:

migrate:
	docker-compose run --rm analysis_system_web python manage.py makemigrations
	docker-compose run --rm analysis_system_web python manage.py migrate

setup:
	docker-compose up -d postgres
	sleep 10
	make migrate
	make populate-initial-data
	make start

start:
	docker-compose up -d
	make migrate
	docker-compose up -d mongo-express

stop:
	docker-compose down

logs:
	docker-compose logs -f

test:
	make test-sensor-receiver-api
	make test-consultive-api
	make test-analysis-system-web

test-sensor-receiver-api:
	docker-compose up -d
	docker-compose stop sensor_receiver_api
	docker-compose run --rm sensor_receiver_api pytest sensor_receiver_api/tests
	docker-compose start sensor_receiver_api

test-consultive-api:
	docker-compose up -d
	docker-compose stop consultive_api
	docker-compose run --rm consultive_api pytest consultive_api/tests
	docker-compose start consultive_api

test-analysis-system-web:
	docker-compose up -d
	docker-compose stop analysis_system_web
	docker-compose run --rm analysis_system_web python manage.py test
	docker-compose start analysis_system_web

populate-initial-data:
	docker-compose run --rm analysis_system_web python manage.py register_monitors
	docker-compose run --rm analysis_system_web python manage.py register_persons
	docker-compose run --rm analysis_system_web python manage.py createsuperuser
