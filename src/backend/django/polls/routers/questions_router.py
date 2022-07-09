from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/")
def get_questions():
    return "Tonne "
