import unittest
from src.recommend import recommend_movies
from src.data_preprocessing import load_data
from src.model_training import train_model

class TestRecommend(unittest.TestCase):
    def test_recommend_movies(self):
        ratings, _ = load_data()
        train_model(ratings)
        recommendations = recommend_movies(user_id=1, n=10)
        self.assertEqual(len(recommendations), 10)

if __name__ == '__main__':
    unittest.main()
