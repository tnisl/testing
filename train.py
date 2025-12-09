import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

#this stuffs for exp tracking
import mlflow
import mlflow.sklearn




print("Getting processed data...")



X = pd.read_csv('data/processed/X.csv')
y = pd.read_csv('data/processed/y.csv')


print("Training process..")



with mlflow.start_run():
    model_type = "LinearRegression"

    mlflow.log_param("model_type: ", model_type)


    

    #training process
    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)

    mse = mean_squared_error(y, predictions)
    mae = mean_absolute_error(y, predictions)

    print(f"  MSE: {mse}")
    print(f"  MAE: {mae}")

    mlflow.log_metric("mse", mse)
    mlflow.log_metric("mae", mae)



    mlflow.sklearn.log_model(model, "model")




    
    checkpoint_name = "model.pkl"

    
    joblib.dump(model, checkpoint_name)
    
print("Training success!")
print(f"Model saved as {checkpoint_name}")


with open("metric.txt", "w") as f:
    f.write(f"MSE: {mse}")
    f.write(f"MAE: {mae}")


import matplotlib.pyplot as plt

plt.figure()
plt.scatter(y, predictions)
plt.xlabel('Thực tế')
plt.ylabel('Dự đoán')
plt.savefig('residual.png')


