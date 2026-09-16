from fastapi.testclient import TestClient

from agent_runtime.main import app

client = TestClient(app)


def test_create_job() -> None:
    response = client.post(
        "/jobs",
        json={"task": "Summarize this document"},
    )

    assert response.status_code == 201

    body = response.json()

    assert body["task"] == "Summarize this document"
    assert body["status"] == "queued"
    assert "id" in body
