from .base import *  # noqa: F403

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [  # noqa: F405
    "silk",
]

MIDDLEWARE = [
    "silk.middleware.SilkyMiddleware",
    *MIDDLEWARE,  # noqa: F405
]

SILKY_PYTHON_PROFILER = True
