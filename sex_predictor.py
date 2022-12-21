#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Regular EDA and plotting libraries
import numpy as np # np is short for numpy
import pandas as pd # pandas is so commonly used, it's shortened to pd
import matplotlib.pyplot as plt
import pickle



## Models
from sklearn.linear_model import LogisticRegression




# Load a saved model and make a prediction
loaded_model = pickle.load(open("sex_predictor.pkl", "rb"))


# Import new data to make predictions
df2 = pd.read_csv("newsample.csv")
df2.drop('index', axis=1, inplace=True)
df2

# Load the trained model
with open('sex_predictor.pkl', 'rb') as f:
    model = pickle.load(f)

# Preprocess the input data
input_data = df2

# Make predictions
predictions = model.predict(input_data)

# Create DataFrame
df_preds = pd.DataFrame()
df_preds["Sex"] = predictions
df_preds

# Export to csv...
df_preds.to_csv("newsample_PREDICTIONS_Igor_Barbosa_Lima.csv", index=False)



