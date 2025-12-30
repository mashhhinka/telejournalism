from fastapi import APIRouter

router = APIRouter(
    prefix="/events",
    tags=["events"]
)

# Example endpoint
@router.get("/")
def read_events():
    return {"message": "Events list will be here"}
