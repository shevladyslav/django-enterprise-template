format:
	poetry run isort ./src
	poetry run black ./src

lint:
	poetry run ruff check ./src

fix:
	poetry run ruff check ./src --fix

test:
	docker compose -f docker/docker-compose-develop.yaml exec django poetry run pytest

test-coverage:
    docker compose -f docker/docker-compose-develop.yaml exec django poetry run pytest --cov --cov-report=term-missing