#Este archivo manejará la lógica para predecir utilizando el modelo cargado.
import pandas as pd
from .myModel import load_model

# Función para predecir la demanda
def predict_demand(data: dict) -> dict:
    # Convertir los datos de entrada (dict) en un DataFrame
    df = pd.DataFrame([data])

    # Cargar el modelo
    model = load_model()

    # Realizar la predicción
    prediction = model.predict(df)

    # Devolver el resultado como un diccionario
    return {"Predicted_Demand": prediction[0]}