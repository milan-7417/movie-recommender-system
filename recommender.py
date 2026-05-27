import os
import pickle
import pandas as pd
import numpy as np
import requests


# ==========================
# BASE DIRECTORY
# ==========================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)


# ==========================
# LOAD MODELS
# ==========================

movies = pickle.load(
    open(
        os.path.join(
            DATA_DIR,
            "movies_processed.pkl"
        ),
        "rb"
    )
)

import gdown


similarity_path = os.path.join(
    DATA_DIR,
    "similarity.pkl"
)

if not os.path.exists(
    similarity_path
):

    file_id = (
        "1spa3PsYX88mI3K3A6-3o1_Uz7Hpvl63S"
    )

    url = (
        f"https://drive.google.com/uc?id={file_id}"
    )

    print(
        "Downloading similarity.pkl..."
    )

    gdown.download(
        url,
        similarity_path,
        quiet=False
    )

similarity = pickle.load(
    open(
        similarity_path,
        "rb"
    )
)

knn_model = pickle.load(
    open(
        os.path.join(
            DATA_DIR,
            "knn_model.pkl"
        ),
        "rb"
    )
)

movie_ratings = pickle.load(
    open(
        os.path.join(
            DATA_DIR,
            "movie_ratings.pkl"
        ),
        "rb"
    )
)


# ==========================
# CONTENT BASED RECOMMENDER
# ==========================

def content_based(movie_name):

    movie_name = movie_name.lower()

    movie_index = movies[
        movies["title"]
        .str.lower() == movie_name
    ].index

    if len(movie_index) == 0:
        return []

    index = movie_index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]

    recommendations = []

    for i in movie_list:

        movie = movies.iloc[i[0]]

        recommendations.append({

            "title":
            movie.title,

            "rating":
            round(
                movie.vote_average,
                1
            )
        })

    return recommendations


# ==========================
# OMDB API DETAILS
# ==========================
import os
def get_movie_details(movie_name):

    API_KEY = os.getenv("OMDB_API_KEY")

    url = (
        f"http://www.omdbapi.com/"
        f"?t={movie_name}"
        f"&apikey={API_KEY}"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()

    except Exception:

        return {
            "title": movie_name,
            "poster":
            "https://via.placeholder.com/400",

            "rating":
            "N/A",

            "genre":
            "N/A",

            "cast":
            "N/A",

            "description":
            "No description found",

            "year":
            "N/A"
        }

    if data.get("Response") == "False":

        return {

            "title":
            movie_name,

            "poster":
            "https://via.placeholder.com/400",

            "rating":
            "N/A",

            "genre":
            "N/A",

            "cast":
            "N/A",

            "description":
            "No description found",

            "year":
            "N/A"
        }

    return {

        "title":
        data.get(
            "Title",
            movie_name
        ),

        "poster":
        data.get(
            "Poster",
            "https://via.placeholder.com/400"
        ),

        "rating":
        data.get(
            "imdbRating",
            "N/A"
        ),

        "genre":
        data.get(
            "Genre",
            "N/A"
        ),

        "cast":
        data.get(
            "Actors",
            "N/A"
        ),

        "description":
        data.get(
            "Plot",
            "No description found"
        ),

        "year":
        data.get(
            "Year",
            "N/A"
        )
    }


# ==========================
# HYBRID RECOMMENDER
# ==========================

def hybrid_recommend(movie_name):

    content_results = content_based(
        movie_name
    )

    enhanced_movies = []

    for movie in content_results:

        details = get_movie_details(
            movie["title"]
        )

        enhanced_movies.append({

            "title":
            movie["title"],

            "poster":
            details["poster"],

            "genre":
            details["genre"],

            "cast":
            details["cast"],

            "description":
            details["description"],

            "rating":
            details["rating"],

            "year":
            details["year"]
        })

    return enhanced_movies


# ==========================
# AUTOSUGGESTION
# ==========================

def get_movie_suggestions(query):

    query = query.lower()

    matches = movies[
        movies["title"]
        .str.lower()
        .str.contains(
            query,
            na=False
        )
    ]

    return (
        matches["title"]
        .head(8)
        .tolist()
    )