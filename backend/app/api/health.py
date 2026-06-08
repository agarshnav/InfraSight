from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Liveness check — confirms the application process is running.
    Does not verify database or other dependencies.
    """
    return {
        "status": "healthy",
        "service": "infrasight-backend",
        "checks": {
            "application": "ok"
        }
    }