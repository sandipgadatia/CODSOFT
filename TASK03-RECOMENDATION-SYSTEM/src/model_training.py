import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pickle
from data_preprocessing import load_data

# Load data
ratings, movies = load_data()

# Convert data to Surprise format
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings, reader)

# Split the data into training and test sets
trainset, testset = train_test_split(data, test_size=0.2)

# Train the SVD algorithm on the training set
model = SVD()
model.fit(trainset)

# Save the model
with open('models/recommendation_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Evaluate the model
predictions = model.test(testset)
from surprise import accuracy
accuracy.rmse(predictions)
