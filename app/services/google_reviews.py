import requests
from app.config import GOOGLE_API_KEY

def get_google_reviews(place_id: str):
    url = f"https://places.googleapis.com/v1/places/{place_id}"
    params = {
        "key": GOOGLE_API_KEY,
        "fields": "displayName,reviews"
    }
    response = requests.get(url, params=params)
    data = response.json()

    return data.get("displayName", "No results"), data.get("reviews", [])