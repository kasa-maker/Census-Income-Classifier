from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

# 1. FastAPI ka app object banayein
app = FastAPI(title="Adult Income Prediction API")

# 2. Model ko load karein (Jo pickle se freeze kiya tha)
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# 3. Pydantic Model banayein (Yeh check karega ke frontend se data sahi aa raha hai)
# Jo columns aap ke dataset mein hain, unhi ke naam yahan honge
class IncomeInput(BaseModel):
    age: int
    workclass: str
    fnlwgt: int
    education: str
    education_num: int  # dhyan rahe columns ke naam dataset jaise hon
    marital_status: str
    occupation: str
    relationship: str
    race: str
    gender: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str

# 4. Home Route (Sirf check karne ke liye ke API chal rahi hai)
@app.get("/")
def home():
    return {"message": "Adult Income Prediction API is running successfully!"}

# 5. Prediction Route (Yahan frontend data bhejega)
@app.post("/predict")
def predict_income(data: IncomeInput):
    # JSON data ko dictionary mein badlein
    input_dict = data.model_dump()
    
    # ML Pipeline ke columns ke naam exact match karne ke liye '-' lagayein jo dataset mein thay
    # Kyunke Python variables mein '-' allow nahi karta, isliye hum yahan mapping kar rahe hain
    formatted_dict = {
        'age': input_dict['age'],
        'workclass': input_dict['workclass'],
        'fnlwgt': input_dict['fnlwgt'],
        'education': input_dict['education'],
        'educational-num': input_dict['education_num'],
        'marital-status': input_dict['marital_status'],
        'occupation': input_dict['occupation'],
        'relationship': input_dict['relationship'],
        'race': input_dict['race'],
        'gender': input_dict['gender'],
        'capital-gain': input_dict['capital_gain'],
        'capital-loss': input_dict['capital_loss'],
        'hours-per-week': input_dict['hours_per_week'],
        'native-country': input_dict['native_country']
    }
    
    # Pandas DataFrame banayein kyunke humari pipeline DataFrame leti hai
    df_input = pd.DataFrame([formatted_dict])
    
    # Prediction karein (Pipeline khud encode aur scale karegi)
    prediction = model.predict(df_input)[0]
    
    # Output return karein
    result = ">50K" if prediction == 1 else "<=50K"
    return {"prediction": result}