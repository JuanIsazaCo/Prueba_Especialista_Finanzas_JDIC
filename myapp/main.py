#Este archivo será el punto de entrada para ejecutar la API. Configuraremos las rutas de la API usando FastAPI.
from fastapi import FastAPI
from pydantic import BaseModel
from .predict import predict_demand

# Definir la estructura del JSON de entrada utilizando Pydantic
class DemandRequest(BaseModel):
    SeniorCity: int
    Partner: str
    Dependents: str
    Service1: str
    Service2: str
    Security: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    Charges: float

# Crear la instancia de la app FastAPI
app = FastAPI()

@app.post("/predict/")
async def predict(request: DemandRequest):
    # Convertir el request en un diccionario
    data = request.dict()

    # Realizar la predicción utilizando el modelo
    prediction = predict_demand(data)
    
    # Devolver la predicción como respuesta
    return prediction

print('El codigo se ha corrido con exito')