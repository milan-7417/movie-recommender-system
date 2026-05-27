import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OMDB_API_KEY")


def get_movie_details(movie_name):

    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"

    response = requests.get(url)

    data = response.json()

    if data.get("Response") == "True":

        return {
            "poster": data.get("Poster"),
            "genre": data.get("Genre"),
            "cast": data.get("Actors"),
            "description": data.get("Plot"),
            "rating": data.get("imdbRating"),
            "year": data.get("Year")
        }

    return {
        "poster": "",
        "genre": "N/A",
        "cast": "N/A",
        "description": "No description available",
        "rating": "N/A",
        "year": ""
    }