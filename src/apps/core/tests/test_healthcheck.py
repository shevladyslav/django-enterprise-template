import pytest
from django.conf import settings


@pytest.mark.django_db
def test_healthcheck_returns_ok(client):
    """
    Ensures the healthcheck endpoint is reachable and returns OK status.
    """
    response = client.get(f"{settings.API_PREFIX}/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
