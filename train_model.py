import pandas as pd
import numpy as np
import ast
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors


# ==================================
# LOAD DATASETS
# ==================================

movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

ratings = pd.read_csv("data/ratings.csv")
movielens_movies = pd.read_csv("data/movies.csv")


# ==================================
# MERGE TMDB DATA
# ==================================

movies = movies.merge(credits, on="title")

print("TMDB merged successfully")


# ==================================
# HELPER FUNCTIONS
# ==================================

def convert(text):
    result = []
    try:
        for i in ast.literal_eval(text):
            result.append(i["name"])
    except:
        pass
    return result


def get_director(text):
    result = []

    try:
        for i in ast.literal_eval(text):
            if i["job"] == "Director":
                result.append(i["name"])
                break
    except:
        pass

    return result


def get_top_cast(text):
    result = []

    try:
        count = 0
        for i in ast.literal_eval(text):
            if count < 5:
                result.append(i["name"])
                count += 1
    except:
        pass

    return result


# ==================================
# SELECT FEATURES
# ==================================

movies = movies[
    [
        "movie_id",
        "title",
        "overview",
        "genres",
        "keywords",
        "cast",
        "crew",
        "vote_average"
    ]
]

movies.dropna(inplace=True)


# ==================================
# CLEAN DATA
# ==================================

movies["genres"] = movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert)
movies["cast"] = movies["cast"].apply(get_top_cast)
movies["crew"] = movies["crew"].apply(get_director)

movies["overview"] = movies["overview"].apply(
    lambda x: x.split()
)


movies["genres"] = movies["genres"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["keywords"] = movies["keywords"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["cast"] = movies["cast"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["crew"] = movies["crew"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)


# ==================================
# CREATE TAGS
# ==================================

movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"]
)

movies["tags"] = movies["tags"].apply(
    lambda x: " ".join(x)
)

new_movies = movies[
    [
        "movie_id",
        "title",
        "tags",
        "vote_average"
    ]
]

print("Tags created successfully")


# ==================================
# CONTENT BASED MODEL
# ==================================

tfidf = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

vectors = tfidf.fit_transform(
    new_movies["tags"]
)

similarity = cosine_similarity(vectors)

print("Content model created")


# SAVE CONTENT MODEL

pickle.dump(
    new_movies,
    open("data/movies_processed.pkl", "wb")
)

pickle.dump(
    similarity,
    open("data/similarity.pkl", "wb")
)

print("Content model saved")


# ==================================
# COLLABORATIVE FILTERING
# ==================================

print("Building collaborative model...")

movie_ratings = ratings.pivot_table(
    index="movieId",
    columns="userId",
    values="rating"
).fillna(0)


knn_model = NearestNeighbors(
    metric="cosine",
    algorithm="brute",
    n_neighbors=10
)

knn_model.fit(movie_ratings)

pickle.dump(
    knn_model,
    open("data/knn_model.pkl", "wb")
)

pickle.dump(
    movie_ratings,
    open("data/movie_ratings.pkl", "wb")
)

print("Collaborative model saved")

print("Everything completed successfully!")