from uuid import uuid4

from fastapi import FastAPI, status

from agent_runtime.models import JobCreate, JobResponse, JobStatus

app = FastAPI(
    title="Agent Runtime",
    description="A fault-tolerant runtime for executing AI agent jobs.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/jobs",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_job(job: JobCreate) -> JobResponse:
    return JobResponse(
        id=str(uuid4()),
        task=job.task,
        status=JobStatus.QUEUED,
    )
