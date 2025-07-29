# 🎬 Movie Recommender with Content-Based Filtering and NLP

This is a simple movie recommendation system that suggests **5 similar movies** based on a movie selected by the user. It uses **content-based filtering** and **genre-based similarity**, along with natural language processing techniques, to compute recommendations.

Built using Python and Streamlit, the app is interactive and easy to use — just select a movie and get recommendations instantly.

---

## 🚀 Features

- 🔍 **Content-Based Filtering** using movie metadata like title, overview, keywords, cast, and genres
- 🎭 **Genre-Based Similarity** scoring
- 🧠 NLP Techniques like **lemmatization** for text preprocessing
- 🧰 Uses **cosine similarity** for vectorizing and comparing movie descriptions
- 🖥️ **Streamlit UI** for an interactive web app
- 💾 Preprocessed data and model serialized with `pickle` for fast deployment

---

## 🛠 Tech Stack

- Python
- Streamlit
- scikit-learn
- pandas
- NLTK (for lemmatization)
- Jupyter Notebook (for preprocessing and model building)

---

## 📁 Datasets Used

- [TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## ▶️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/movie-recommender.git
   cd movie-recommender

2. **Install the required packages**
   ```bash
   pip install -r requirements.txt

3. **Run the app**
   ```bash
   streamlit run app.py

## 🌐 Live Demo   
   -  [Click here](https://moviesrecommenderbytahirkorma.streamlit.app)

##   📸 Screenshots
##   🙌 Credits
   -    [TMDb](https://www.themoviedb.org/) for metadata
