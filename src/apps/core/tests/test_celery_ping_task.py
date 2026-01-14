import pytest

from apps.core.tasks import ping


@pytest.mark.django_db
def test_ping_task(settings):
    """
    Ensure that the Celery ping task executes successfully.

    The test runs Celery in eager mode, meaning the task is executed
    synchronously in the same process without a real broker or worker.
    This makes the test fast, deterministic, and suitable for CI.
    """

    # Force Celery to execute tasks synchronously (no Redis / worker required)
    settings.CELERY_TASK_ALWAYS_EAGER = True

    # Propagate exceptions instead of swallowing them inside Celery
    settings.CELERY_TASK_EAGER_PROPAGATES = True

    # Execute the task using the real Celery API
    result = ping.delay()

    # Validate the task result
    assert result.get() == "pong"
