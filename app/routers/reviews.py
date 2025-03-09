from fastapi import APIRouter
from app.services.google_reviews import get_google_reviews
from app.services.openai_summary import summarize_reviews

router = APIRouter()


@router.get("/reviews/{place_id}")
async def get_reviews_summary(place_id: str):
    name, reviews = get_google_reviews(place_id)

    if not reviews:
        return {"message": "No reviews found"}

    summary = summarize_reviews(reviews, name)
    return {"summary": summary}