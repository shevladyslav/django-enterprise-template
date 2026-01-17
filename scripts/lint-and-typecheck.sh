#!/usr/bin/env bash
set -e

YELLOW='\033[1;33m'
GREEN='\033[1;32m'
NC='\033[0m' # No Color

echo -e "${YELLOW}==> Running isort${NC}"
poetry run isort ./src
echo -e "${GREEN}[OK] isort passed${NC}"

echo -e "${YELLOW}==> Running black${NC}"
poetry run black ./src
echo -e "${GREEN}[OK] black passed${NC}"

echo -e "${YELLOW}==> Running ruff${NC}"
poetry run ruff check ./src
echo -e "${GREEN}[OK] ruff passed${NC}"

echo -e "${YELLOW}==> Running mypy${NC}"
poetry run mypy ./src
echo -e "${GREEN}[OK] mypy passed${NC}"

echo -e "${YELLOW}==> Running pip-audit${NC}"
poetry run pip-audit --strict
echo -e "${GREEN}[OK] pip-audit passed${NC}"

echo -e "${GREEN}==> All checks passed${NC}"
