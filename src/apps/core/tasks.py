from celery import shared_task


@shared_task
def ping():
    """
    Simple Celery health-check task.

    Used to verify that Celery worker is running and able to execute tasks.
    Returns a static string response.
    """
    return "pong"
