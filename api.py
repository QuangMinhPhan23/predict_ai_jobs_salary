# FastAPI Deployment Example
from fastapi import FastAPI, Request
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('model.joblib')

@app.post('/predict')
async def predict(request: Request):
    data = await request.json()
    # Expecting: {'job_title_encoded': int, 'years_experience': float, 'salary_scaled': float}
    features = np.array([[data['job_title_encoded'], data['years_experience'], data['salary_scaled']]])
    prediction = model.predict(features)[0]
    return {'predicted_salary_usd': float(prediction)}