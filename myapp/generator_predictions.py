# import sys
# sys.path.append(r'C:\Users\jisaza53\Especialista_Finanzas_JDIC\myapp')

#Este archivo manejará la lógica para predecir utilizando el modelo cargado.
import pandas as pd
from myapp.myModel import load_model

# En generator_predictions.py
def predict_demand(data: dict) -> dict:
    # Convertir los datos de entrada (dict) en un DataFrame
    df = pd.DataFrame([data])

    # Cargar el modelo
    model = load_model()

    # Acceder al modelo de demanda
    demand_model = model['demand_model']

    # Realizar la predicción de la demanda
    prediction = demand_model.predict(df)

    # Devolver el resultado como un diccionario
    return {"Predicted_Demand": prediction[0]}
print('Se ha corrido con exito')