import sys
import os
# Agregar el directorio 'myapp' al sys.path de forma relativa
current_dir = os.path.dirname(__file__)  # Obtiene el directorio del script actual
myapp_dir = os.path.join(current_dir)  # Crea la ruta relativa a 'myapp'

sys.path.append(myapp_dir)
# Este archivo será el punto de entrada para ejecutar la API. Configuraremos las rutas de la API usando FastAPI.
from fastapi import FastAPI
from pydantic import BaseModel
<<<<<<< HEAD
from myapp.generator_predictions import predict_demand
=======
from generator_predictions import predict_demand  # Asume que esta función ya está definida
>>>>>>> pruebas

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

@app.post("/generator_predictions/")
async def generate_predictions(request: DemandRequest):
    # Convertir el request en un diccionario
    data = request.dict()

    # Realizar la predicción utilizando el modelo
    prediction = predict_demand(data)
    
    # Devolver la predicción como respuesta
    return prediction

print('El código se ha corrido con éxito')