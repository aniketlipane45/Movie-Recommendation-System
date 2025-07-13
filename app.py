from flask import Flask, render_template, request
from model import recommend_movies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie']
    recommendations = recommend_movies(movie_name)
    return render_template('result.html', movie=movie_name, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
