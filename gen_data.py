import pandas as pd
import numpy as np
import os
import sys


path = 'data/big_data.csv'



def gen_norm():
    X = np.linspace(50, 200, 100)
    noise = np.random.normal(0,1,100) 

    y = 0.05 * X + noise

    df = pd.DataFrame({
        'area': X,
        'price': y
    })


    df.to_csv(path, index = False)

    print(f"Generate normal data at {path}")


def gen_anomaly():
    X = np.linspace(50, 200, 100)
    noise = np.random.normal(0, 1, 100)

    y = 0.05 * X + noise

    y[0] = y[0] + 100
    y[0] = y[0] + 200

    df = pd.DataFrame({
        'area': X,
        'price': y
    })

    df.to_csv(path, index = False)

    print(f"Generate anomaly data at {path}")




gen_anomaly()

    





    
