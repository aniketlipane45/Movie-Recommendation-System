import pandas as pd
import difflib
import pickle

# Load dataset
movies_data = pd.read_csv('movies.csv')

# Fill missing values
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Combine features
combined_features = (
    movies_data['genres'] + ' ' +
    movies_data['keywords'] + ' ' +
    movies_data['tagline'] + ' ' +
    movies_data['cast'] + ' ' +
    movies_data['director']
)

# Load vectorizer and similarity matrix from pickle files
with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# Recommendation function
def recommend_movies(movie_name):
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if not find_close_match:
        return ["No close match found. Try another movie."]

    close_match = find_close_match[0]
    index_of_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_movie]))
    sorted_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i, movie in enumerate(sorted_movies[1:31]):
        index = movie[0]
        title = movies_data.iloc[index]['title']
        recommendations.append(title)

    return recommendations
