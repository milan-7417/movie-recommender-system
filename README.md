# 🎬 MovieVerse - Movie Recommendation System
<img width="1889" height="872" alt="Screenshot (155)" src="https://github.com/user-attachments/assets/3c2faa8d-6ac3-4507-81d7-ca771404f297" />


MovieVerse is an intelligent movie recommendation web application built using **Flask**, **Machine Learning**, and **OMDb API**. It provides personalized movie recommendations using a **hybrid recommendation system** and allows users to manage their watchlist.

---

## 🚀 Features

### 🔐 Authentication System
- User Signup
- User Login
- Secure Password Hashing
- Session Management
- Logout Functionality

### 🎥 Movie Recommendation System
- Content-Based Recommendation
- Hybrid Recommendation Model
- Similar Movie Suggestions
- Movie Search with Auto-Suggestions

### 📄 Movie Details Page
- Movie Poster
- IMDb Rating
- Genre
- Cast Information
- Release Year
- Full Movie Description

### ❤️ Watchlist Feature
- Add Movies to Watchlist
- Delete Movies from Watchlist
- Click Movie → Open Movie Details Page

### 🎨 Modern UI
- Responsive Design
- Sidebar Navigation
- Clean Movie Cards
- Custom Styling with CSS

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Flask (Python)

### Database
- SQLite

### Machine Learning
- Scikit-Learn
- KNN Model
- Cosine Similarity

### API
- OMDb API

---

## 📂 Project Structure

```bash
movie_recommender/
│
├── app.py
├── recommender.py
├── database.py
├── omdb_api.py
├── requirements.txt
├── runtime.txt
├── render.yaml
├── procfile
│
├── data/
│   ├── knn_model.pkl
│   ├── movie_ratings.pkl
│   ├── movies_processed.pkl
│   ├── movies.csv
│   ├── ratings.csv
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── database/
│   └── movie.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── app.js
│   │
│   └── images/
│       └── movie_bg.jpg
│
└── templates/
    ├── base.html
    ├── dashboard.html
    ├── login.html
    ├── signup.html
    ├── movie_details.html
    └── watchlist.html
```

---

## 🧠 Machine Learning Approach

This project uses a **Hybrid Recommendation System**:

### 1. Content-Based Filtering
Movies are recommended based on:
- Genre
- Keywords
- Overview
- Cast
- Tags Similarity

Cosine Similarity is used to find similar movies.

### 2. KNN Model
A **K-Nearest Neighbors (KNN)** model improves recommendation quality.

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/milan-7417/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Application

```bash
python app.py
```

---

## 🌐 Open in Browser

Go to:

```bash
http://127.0.0.1:5000
```

---

## 🔑 OMDb API Setup

This project uses **OMDb API** to fetch real-time movie details.

Get API Key:

https://www.omdbapi.com/apikey.aspx

Add your API key inside:

```python
omdb_api.py
```

Example:

```python
API_KEY = "your_api_key"
```

---

## 🚀 Deployment on Render

### Step 1: Push Code to GitHub

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

---

### Step 2: Create Web Service on Render

1. Login to Render  
2. Click **New +**
3. Select **Web Service**
4. Connect GitHub Repository
5. Choose your repo

---

### Step 3: Configure Render

#### Build Command

```bash
pip install -r requirements.txt
```

#### Start Command

```bash
gunicorn app:app
```

---

## 📸 Screenshots

### Dashboard
- Search Movies
- Get Recommendations
  <img width="1920" height="1080" alt="Screenshot (157)" src="https://github.com/user-attachments/assets/ade0e522-8e65-4ff3-9989-2bac4cf482fd" />


### Watchlist
- Save Favorite Movies
- Delete Movies
  <img width="1920" height="1080" alt="Screenshot (158)" src="https://github.com/user-attachments/assets/71e868d9-a388-4206-83d7-0a13e15ef71f" />


### Movie Details
- View Complete Movie Information
  <img width="1920" height="1080" alt="Screenshot (159)" src="https://github.com/user-attachments/assets/bfab4105-be43-4039-906d-267b9bda5674" />


---

## 🔥 Future Improvements

- Collaborative Filtering
- User Rating System
- Trending Movies Section
- Dark Mode
- Recommendation Accuracy Improvement
- Pagination

---

## 👨‍💻 Author

**Milan Kumar**

Built with ❤️ using Flask & Machine Learning

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub.
