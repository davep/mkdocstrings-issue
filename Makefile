all:
	pipenv run mkdocs serve

setup:
	pipenv sync
