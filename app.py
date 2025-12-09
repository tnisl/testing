from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np


app = FastAPI()



try: 
    model = joblib.load("model.pkl")
    print("Loading model successfullly!")
except:
    print(f"Error: cannot load model! {e}")


class HouseInput(BaseModel):
    area:float


@app.post("/predict")
def predict_price(input : HouseInput):
    area_value = input.area

    feed_input = np.array([[area_value]])

    results = model.predict(feed_input)


    return {
        "input area": area_value,
        "price predicted": results[0],
    }








