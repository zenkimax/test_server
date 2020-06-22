.PYTHON: \
	ci \
	lint test build \
	all requirements docker docker-build docker-push

VERSION ?= 1.0.`date +%Y%m%d`
BASE_COMMIT_ID ?= ""

test:
	python manage.py migrate && python manage.py test rank_server.tests --settings=settings

requirements:
	pipenv run pipenv_to_requirements -f

run:
	python manage.py runserver 0:8000