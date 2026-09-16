from fastapi import FastAPI

from agent_runtime.api.jobs import router as jobs_router

app = FastAPI(
    title="Agent Runtime",
    description="A fault-tolerant runtime for executing AI agent jobs.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(jobs_router)
