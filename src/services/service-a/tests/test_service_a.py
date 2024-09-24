"""
Example Unit Test
"""

from fastapi.testclient import TestClient

from service_a.app import RootResponse, app
from service_a.service_a import service_a


def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    response_json = response.json()
    validated_response = RootResponse.model_validate(response_json)
    assert validated_response.service == "service-a"


def test_service_b() -> None:
    """
    Example test for service-b
    """
    assert service_a() == 1
