$ErrorActionPreference = "Stop"

Write-Host "==> Running isort" -ForegroundColor Yellow
poetry run isort ./src
Write-Host "[OK] isort passed" -ForegroundColor Green

Write-Host "==> Running black" -ForegroundColor Yellow
poetry run black ./src
Write-Host "[OK] black passed" -ForegroundColor Green

Write-Host "==> Running ruff" -ForegroundColor Yellow
poetry run ruff check ./src
Write-Host "[OK] ruff passed" -ForegroundColor Green

Write-Host "==> Running mypy" -ForegroundColor Yellow
poetry run mypy ./src
Write-Host "[OK] mypy passed" -ForegroundColor Green

Write-Host "==> Running pip-audit" -ForegroundColor Yellow
poetry run pip-audit --strict
Write-Host "[OK] pip-audit passed" -ForegroundColor Green

Write-Host "==> All checks passed" -ForegroundColor Green
