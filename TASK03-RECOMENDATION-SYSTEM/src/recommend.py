import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_preprocessing import load_data  # Use absolute import

import pickle

# Load the model
with open('models/recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

def recommend(user_id, n_recommendations=10):
    ratings, movies = load_data()
    all_movie_ids = set(movies['movieId'])

    # Get movies already rated by the user
    user_ratings = ratings[ratings['userId'] == user_id]
    if user_ratings.empty:
        return None  # Return None if the user does not exist

    rated_movie_ids = set(user_ratings['movieId'])

    # Find movies not yet rated by the user
    unrated_movie_ids = all_movie_ids - rated_movie_ids

    # Predict ratings for unrated movies
    predictions = [model.predict(user_id, movie_id) for movie_id in unrated_movie_ids]
    predictions.sort(key=lambda x: x.est, reverse=True)

    # Get the top n recommendations
    top_n = predictions[:n_recommendations]
    top_n_movie_ids = [pred.iid for pred in top_n]
    top_n_movies = movies[movies['movieId'].isin(top_n_movie_ids)]
    
    return top_n_movies

if __name__ == "__main__":
    user_id = int(input("Enter user ID: "))
    recommendations = recommend(user_id)
    if recommendations is not None:
        print("Top movie recommendations:")
        print(recommendations)
    else:
        print("User ID does not exist.")
