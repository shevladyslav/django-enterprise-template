# django-enterprise-template

## To run local server:
`docker compose -f docker/docker-compose-develop.yaml up --build`

## To run pytests:
`docker compose -f docker/docker-compose-develop.yaml exec django poetry run pytest`

## To run coverage:
`docker compose -f docker/docker-compose-develop.yaml exec django poetry run pytest --cov --cov-report=term-missing`

### TODO:
- 404, 500 pages?
- docker-compose files refactoring