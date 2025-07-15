
```markdown
# 🎬 Movie Recommendation System

This project is a **Content-Based Movie Recommendation System** built using **Python**, **Flask**, and **scikit-learn**. It recommends movies similar to a user’s favorite movie using **TF-IDF vectorization** and **cosine similarity** on movie metadata (genres, cast, director, keywords, and tagline).


## 🧠 How It Works

The model is trained using:
- **TF-IDF Vectorizer**: Converts movie metadata into numerical feature vectors
- **Cosine Similarity**: Measures similarity between movies based on content

It uses a **Content-Based Filtering** approach (no user ratings required).



## 📁 Project Structure
<pre>

movie-recommender/
│
├── app.py                   # Flask backend to handle user requests
├── model.py                 # Core ML logic (loads pickled model)
├── train\_model.py           # (Optional) Script to retrain model and regenerate .pkl files
├── movies.csv               # Movie metadata dataset
├── train_model.py           #train_model and create .pkl files
│
├── templates/
│   ├── index.html           # Input form (homepage)
│   └── result.html          # Shows top 30 recommended movies
│
├── static/
│   └── style.css            # Frontend styling
│
└── README.md                # Project documentation (this file)

</pre>



## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Create one with: `pip freeze > requirements.txt`

### 3. Run the Flask App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)


## 🧪 Train the Model (Optional)

If you want to retrain using an updated `movies.csv`:

```bash
python train_model.py
```

This will regenerate:

* `tfidf_vectorizer.pkl`
* `similarity.pkl`



## 📊 Sample Input

```
Enter your favorite movie: Avatar
```

### 📤 Output

```
Top 30 movies similar to Avatar:
1. Guardians of the Galaxy
2. John Carter
3. Star Trek Into Darkness
...
```


## ✅ Features

* Content-based filtering using metadata
* Clean HTML/CSS UI with Flask backend
* Pickle files for fast loading (no need to retrain every time)
* Easy to retrain and extend



## 📌 Requirements

* Python 3.7+
* Flask
* scikit-learn
* pandas



## 📚 Dataset

Uses a `movies.csv` file with columns:

* `title`, `genres`, `keywords`, `tagline`, `cast`, `director`, `index`


## 📄 License

This project is open source and available under the [MIT License](LICENSE).



## 💡 Future Improvements

* Add user-based collaborative filtering (ratings)
* Hybrid model (content + collaborative)
* Deploy to Heroku/Render



