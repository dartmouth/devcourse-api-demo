"""A tiny health‑check endpoint – great for demos and Kubernetes liveness probes."""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health", summary="Simple health check")
async def health_check() -> dict:
    return {"status": "ok"}