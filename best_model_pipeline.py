import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('weather_forecast_csv/processed_weatherHistory.csv')
features = tpot_data.drop('Temperature (C)', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['Temperature (C)'], random_state=42)

# Average CV score on the training set was: -0.0009392110875172593
exported_pipeline = RandomForestRegressor(bootstrap=True, max_features=0.7500000000000001, min_samples_leaf=1, min_samples_split=9, n_estimators=100)
# Fix random state in exported estimator
if hasattr(exported_pipeline, 'random_state'):
    setattr(exported_pipeline, 'random_state', 42)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
