import unittest
from src.data_preprocessing import load_data

class TestDataPreprocessing(unittest.TestCase):
    def test_load_data(self):
        ratings, movies = load_data()
        self.assertFalse(ratings.empty)
        self.assertFalse(movies.empty)
        self.assertIn('user_id', ratings.columns)
        self.assertIn('movie_id', ratings.columns)
        self.assertIn('rating', ratings.columns)
        self.assertIn('title', movies.columns)

if __name__ == '__main__':
    unittest.main()
