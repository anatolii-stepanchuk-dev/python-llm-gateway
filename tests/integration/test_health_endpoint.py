from fastapi.testclient import TestClient

from python_llm_gateway.main import create_app


def test_health_endpoint_returns_ok() -> None:
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "app_name": "python-llm-gateway",
        "status": "ok",
        "environment": "local",
    }

def test_openapi_schema_is_available() -> None:
    client = TestClient(create_app())

    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert response.json()["info"]["title"] == "python-llm-gateway"