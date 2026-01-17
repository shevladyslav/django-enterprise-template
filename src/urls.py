from typing import List, Union

from django.conf import settings
from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.core.urls")),
]

if settings.DEBUG:
    # DRF Spectacular: OpenAPI schema endpoint
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        # DRF Spectacular: Swagger UI for interactive API documentation
        path(
            "api/docs/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        # DRF Spectacular: ReDoc UI for API documentation
        path(
            "api/redoc/",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ]

    # Django Silk: request and SQL query profiler (development only)
    urlpatterns += [
        path("silk/", include("silk.urls", namespace="silk")),
    ]
