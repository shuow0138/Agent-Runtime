from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from agent_runtime.models.job import Job, JobCreate

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"],
)


jobs: dict[UUID, Job] = {}


@router.post(
    "",
    response_model=Job,
    status_code=status.HTTP_201_CREATED,
)
def create_job(job_create: JobCreate) -> Job:
    job = Job(prompt=job_create.prompt)

    jobs[job.id] = job

    return job


@router.get(
    "/{job_id}",
    response_model=Job,
)
def get_job(job_id: UUID) -> Job:
    job = jobs.get(job_id)

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )

    return job
