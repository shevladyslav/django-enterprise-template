import pytest
from rest_framework import status
from rest_framework.exceptions import APIException, ErrorDetail, ValidationError
from rest_framework.response import Response

from apps.core.exception_handler import ExceptionFormatter


class DummyView:
    pass


class CustomAPIException(APIException):
    status_code = status.HTTP_418_IM_A_TEAPOT
    default_code = "teapot"
    default_detail = "I'm a teapot"


@pytest.fixture
def handler():
    return ExceptionFormatter()


@pytest.fixture
def context():
    return {"view": DummyView()}


def test_validation_error_flattening(handler, context):
    exception = ValidationError(
        {
            "field": ["error"],
            "nested": {"inner": ["inner_error"]},
            "list": ["a", "b"],
        }
    )
    response = handler(exception, context)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data["status"] == "error"
    assert response.data["code"] == "client_error"
    assert response.data["default_code"] == "invalid"
    assert response.data["exception_type"] == "ValidationError"
    assert response.data["view"] == "DummyView"
    assert response.data["error_messages"] == {
        "field": "error",
        "nested": {"inner": "inner_error"},
        "list": ["a", "b"],
    }


def test_non_client_drf_exception(handler, context):
    exception = CustomAPIException()
    response = handler(exception, context)
    assert response.status_code == status.HTTP_418_IM_A_TEAPOT
    assert response.data["code"] == "client_error"
    assert response.data["default_code"] == "teapot"
    error = response.data["error_messages"]["detail"]
    assert isinstance(error, ErrorDetail)
    assert str(error) == "I'm a teapot"


def test_unhandled_exception(handler, context):
    exception = RuntimeError("boom", "crash")
    response = handler(exception, context)
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.data["code"] == "internal_server_error"
    assert response.data["default_code"] is None
    assert response.data["error_messages"] == ["boom", "crash"]
    assert response.data["exception_type"] == "RuntimeError"


def test_no_view_in_context(handler):
    exception = ValidationError("error")
    response = handler(exception, {})
    assert response.data["view"] is None


def test_flatten_single_primitive_list(handler):
    assert handler._flatten_errors(["error"]) == "error"


def test_flatten_multi_level_list(handler):
    assert handler._flatten_errors([["a"], ["b"]]) == ["a", "b"]


def test_flatten_non_iterable(handler):
    assert handler._flatten_errors("error") == "error"


def test_extract_from_drf_client_error(handler):
    response = Response({"field": ["error"]}, status=400)
    status_code, errors = handler._extract_from_drf(response)
    assert status_code == 400
    assert errors == {"field": "error"}


def test_extract_from_drf_non_client_error(handler):
    response = Response({"detail": "error"}, status=500)
    status_code, errors = handler._extract_from_drf(response)
    assert status_code == 500
    assert errors == "error"


def test_extract_unhandled(handler):
    exception = Exception("fail")
    status_code, errors = handler._extract_unhandled(exception)
    assert status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert errors == ["fail"]
