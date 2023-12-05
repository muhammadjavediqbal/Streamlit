import time
# import streamlit as st
# import pandas as pd
# import numpy as np
# from phe import paillier
# import json
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler

# def train_model(dataset_path):
#     df = pd.read_csv(dataset_path)
#     y = df['salary']  # Replace with your target variable
#     X = df.drop('salary', axis=1)  # Replace with your features
#     X_processed = preprocess_data(X)
#     X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
#     model = RandomForestRegressor(random_state=42)
#     model.fit(X_train, y_train)
#     test_score = model.score(X_test, y_test)
#     st.write(f'Test Score: {test_score}')
#     time.sleep(50)
#     return model

def data():
    time.sleep(100)
