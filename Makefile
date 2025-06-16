.PHONY: deps lint test build deploy commercial setup-stripe secure-repo all

deps:
	pip install -r requirements.txt

lint:
	pre-commit run --all-files

test:
	pytest --junitxml=results.xml

build:
	python cli.py init-commercial

deploy:
	npx netlify deploy --prod --dir=site

commercial: build

setup-stripe:
	python cli.py setup-stripe

secure-repo:
	python cli.py secure-repo aribromstix ForgeDG

all: deps lint test commercial setup-stripe secure-repo deploy
