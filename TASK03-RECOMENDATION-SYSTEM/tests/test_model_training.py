import unittest
from src.model_training import train_model
from src.data_preprocessing import load_data

class TestModelTraining(unittest.TestCase):
    def test_train_model(self):
        ratings, _ = load_data()
        model = train_model(ratings)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
