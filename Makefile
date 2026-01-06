format:
	poetry run isort ./src
	poetry run black ./src

lint:
	poetry run ruff check ./src

fix:
	poetry run ruff check ./src --fix