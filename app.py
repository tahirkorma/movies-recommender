#Import libraries
import streamlit as st
import pickle
import pandas as pd
import requests

#Load data
movies_list = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity_matrics.pkl','rb'))

#Dropdown menu
st.title('Movie Recommender with Content-Based Filtering and NLP')
selected_movie_name = st.selectbox(
    'Select Movies',
    movies_list['title'].values
)

#Create function to fetch movie poster
def fetch_poster(movies_id):
   url = "https://api.themoviedb.org/3/movie/{}?api_key=19a4444420f7689fafa816b7f32183ed&language=en-US".format(movies_id)
   data = requests.get(url)
   data = data.json()
   poster_path = data['poster_path']
   full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
   return full_path

#Create function for movies recommendation
def recommend(movie):
  index = movies_list[movies_list['title'] == movie].index[0]
  distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
  recommended_movies = []
  recommended_movies_posters = []
  for i in distances [1:6]:
     movie_id = movies_list.iloc[i[0]].movie_id
     recommended_movies.append(movies_list.iloc[i[0]].title)
     recommended_movies_posters.append(fetch_poster(movie_id))
  return recommended_movies,recommended_movies_posters

#Display
if st.button('Show Recommendation'):
    recommended_movies, recommended_movies_posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range (5):
        with cols[i]:
          st.image(recommended_movies_posters[i])
          st.text(recommended_movies[i])
          
