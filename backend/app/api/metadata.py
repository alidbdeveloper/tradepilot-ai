from fastapi import APIRouter

from app.services.metadata_service import fetch_tables

router = APIRouter(
    prefix="/metadata",
    tags=["Metadata"]
)


@router.get("/tables")
def get_tables():
    return fetch_tables()