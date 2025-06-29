#!/usr/bin/env python
# coding: utf-8

year = 2023
month = 5

import os



import pickle

import numpy as np
import pandas as pd





with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)




categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)

    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')

    return df




df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:02d}-{month:02d}.parquet')




dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)




stg_pred = np.std(y_pred)
print(stg_pred)
print(f'Mean predicted duration: {np.mean(y_pred):.2f} minutes')




df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
df['predicted_duration'] = y_pred




df_result = df[["ride_id", "predicted_duration"]]




# df_result.to_parquet(
#     f'hw_yellow_tripdata_{year}-{month}',
#     engine='pyarrow',
#     compression=None,
#     index=False
# )




