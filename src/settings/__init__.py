import importlib
import os

ENV_TO_SETTINGS = {
    "local": "settings.local",
    "production": "settings.production",
}


def load_settings():
    env = os.getenv("DJANGO_ENV", "local")
    settings_module = ENV_TO_SETTINGS.get(env)

    if not settings_module:
        raise RuntimeError(
            f"Unknown DJANGO_ENV='{env}'. "
            f"Available: {', '.join(ENV_TO_SETTINGS.keys())}"
        )

    try:
        module = importlib.import_module(settings_module)
    except ImportError as exception:
        raise RuntimeError(
            f"Settings module '{settings_module}' not found"
        ) from exception

    globals().update(
        {name: getattr(module, name) for name in dir(module) if name.isupper()}
    )


load_settings()
