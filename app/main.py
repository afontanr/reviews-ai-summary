from fastapi import FastAPI
from app.routers import reviews

app = FastAPI(title="Reviews Summarizer API")

app.include_router(reviews.router, prefix="/api")

@app.get("/health")
def health_check():
    return {"message": "Reviews Summarizer API is running!"}
