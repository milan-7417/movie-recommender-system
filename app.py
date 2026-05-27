from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    jsonify,
    flash
)

from database import (
    init_db,
    create_user,
    login_user,
    add_to_watchlist,
    get_watchlist,
    delete_from_watchlist
)

from recommender import (
    hybrid_recommend,
    get_movie_suggestions,
    get_movie_details
)

app = Flask(__name__)

app.secret_key = "movie_secret_123"

init_db()


# ==========================
# HOME
# ==========================

@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        recommendations=None
    )


# ==========================
# SIGNUP
# ==========================

@app.route(
    "/signup",
    methods=["GET", "POST"]
)
def signup():

    if request.method == "POST":

        username = request.form[
            "username"
        ]

        email = request.form[
            "email"
        ]

        password = request.form[
            "password"
        ]

        success = create_user(
            username,
            email,
            password
        )

        if success:

            flash(
                "Signup successful! Login now."
            )

            return redirect(
                "/login"
            )

        flash(
            "Email already exists"
        )

    return render_template(
        "signup.html"
    )


# ==========================
# LOGIN
# ==========================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        email = request.form[
            "email"
        ]

        password = request.form[
            "password"
        ]

        user = login_user(
            email,
            password
        )

        if user:

            session["user"] = (
                user["username"]
            )

            session["user_id"] = (
                user["id"]
            )

            return redirect("/")

        flash(
            "Invalid credentials"
        )

    return render_template(
        "login.html"
    )


# ==========================
# LOGOUT
# ==========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        "/login"
    )


# ==========================
# WATCHLIST
# ==========================

@app.route("/watchlist")
def watchlist():

    user_id = session.get(
        "user_id"
    )

    movies = get_watchlist(
        user_id
    )

    return render_template(
        "watchlist.html",
        movies=movies
    )


# ==========================
# RECOMMENDATION
# ==========================

@app.route(
    "/recommend",
    methods=["POST"]
)
def recommend():

    movie_name = request.form[
        "movie_name"
    ]

    recommendations = (
        hybrid_recommend(
            movie_name
        )
    )

    return render_template(
        "dashboard.html",
        recommendations=
        recommendations
    )


# ==========================
# SAVE MOVIE
# ==========================

@app.route(
    "/save_movie",
    methods=["POST"]
)
def save_movie():

    movie_name = request.form[
        "movie_name"
    ]

    user_id = session.get(
        "user_id"
    )

    add_to_watchlist(
        user_id,
        movie_name
    )

    return redirect("/")


# ==========================
# AUTOCOMPLETE
# ==========================

@app.route("/suggest")
def suggest():

    query = request.args.get(
        "query",
        ""
    )

    suggestions = (
        get_movie_suggestions(
            query
        )
    )

    return jsonify({
        "movies": suggestions
    })

@app.route("/movie/<path:movie_name>")
def movie_details(movie_name):

    movie = get_movie_details(
        movie_name
    )

    return render_template(
        "movie_details.html",
        movie=movie
    )

@app.route(
    "/delete_watchlist",
    methods=["POST"]
)
def delete_watchlist():

    user_id = session.get(
        "user_id"
    )

    movie_name = request.form[
        "movie_name"
    ]

    delete_from_watchlist(
        user_id,
        movie_name
    )

    return redirect(
        "/watchlist"
    )


# ==========================
# RUN APP
# ==========================

if __name__ == "__main__":
    app.run(debug=True)