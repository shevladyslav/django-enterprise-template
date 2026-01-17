format:
	poetry run isort ./src
	poetry run black ./src

lint:
	poetry run ruff check ./src

lint-fix:
	poetry run ruff check ./src --fix

typecheck:
	poetry run mypy ./src

audit:
	poetry run pip-audit --strict

test:
	docker compose -f docker/docker-compose-develop.yaml exec django poetry run pytest

test-coverage:
    docker compose -f docker/docker-compose-develop.yaml exec django poetry run pytest --cov --cov-report=term-missing
