from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """
    Health check endpoint.

    Used to verify that the application is running and able to respond to requests.
    Does not require authentication or permissions.
    """

    authentication_classes = []
    permission_classes = []

    @extend_schema(
        summary="Health check",
        description="Returns application health status",
        responses={
            200: OpenApiResponse(
                response={
                    "type": "object",
                    "properties": {"status": {"type": "string"}},
                    "example": {"status": "ok"},
                }
            )
        },
        tags=["Utils"],
    )






    def get(self, request):
        """
        Return application health status.

        Returns HTTP 200 with a simple status payload.
        """
        return Response(
            {"status": "ok"},
            status=status.HTTP_200_OK,
        )
