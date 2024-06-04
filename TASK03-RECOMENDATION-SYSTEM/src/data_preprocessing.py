import pandas as pd

def load_data(data_path='data/ml-latest-small/ratings.csv', item_path='data/ml-latest-small/movies.csv'):
    ratings = pd.read_csv(data_path)
    movies = pd.read_csv(item_path)
    return ratings[['userId', 'movieId', 'rating']], movies[['movieId', 'title']]

if __name__ == "__main__":
    ratings, movies = load_data()
    print("Ratings Data")
    print(ratings.head())
    print("\nMovies Data")
    print(movies.head())
