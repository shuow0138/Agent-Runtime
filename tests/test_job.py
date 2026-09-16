from fastapi.testclient import TestClient

from agent_runtime.main import app

client = TestClient(app)


def test_create_job() -> None:
    response = client.post(
        "/jobs",
        json={"prompt": "Summarize this document"},
    )

    assert response.status_code == 201

    body = response.json()

    assert body["prompt"] == "Summarize this document"
    assert body["status"] == "queued"
    assert "id" in body
    assert "created_at" in body


def test_get_job() -> None:
    create_response = client.post(
        "/jobs",
        json={"prompt": "Test job"},
    )

    job = create_response.json()
    job_id = job["id"]

    response = client.get(f"/jobs/{job_id}")

    assert response.status_code == 200
    assert response.json()["id"] == job_id
    assert response.json()["prompt"] == "Test job"


def test_get_unknown_job_returns_404() -> None:
    response = client.get("/jobs/00000000-0000-0000-0000-000000000000")

    assert response.status_code == 404
    assert response.json() == {"detail": "Job not found"}


def test_create_job_rejects_empty_prompt() -> None:
    response = client.post(
        "/jobs",
        json={"prompt": ""},
    )

    assert response.status_code == 422
