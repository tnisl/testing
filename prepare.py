import pandas as pd
import numpy as np
import os



#input
input_file = "data/big_data.csv"


#output
os.makedirs("data/processed", exist_ok=True)

outputs_X = "data/processed/X.csv"
outputs_y = "data/processed/y.csv"



#load data
print("Data is cleaning")
df = pd.read_csv(input_file)

X = df['area']
y = df['price']

X.to_csv(outputs_X, index = False)
y.to_csv(outputs_y, index = False)

print(f"Data's processed successfully!, saved at input: {outputs_X} output: {outputs_y}")







