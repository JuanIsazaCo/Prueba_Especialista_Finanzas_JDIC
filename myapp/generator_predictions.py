import sys
import os

# Agregar el directorio 'myapp' al sys.path de forma relativa
current_dir = os.path.dirname(__file__)  # Obtiene el directorio del script actual
myapp_dir = os.path.join(current_dir, 'myapp')  # Crea la ruta relativa a 'myapp'

sys.path.append(myapp_dir)

#Este archivo manejará la lógica para predecir utilizando el modelo cargado.
import pandas as pd
from myModel import load_model

# En generator_predictions.py
def predict_demand(data: dict) -> dict:
    # Convertir los datos de entrada (dict) en un DataFrame
    df = pd.DataFrame([data])

    # Cargar el modelo
    model = load_model()

    # Acceder a los modelos de clase y demanda
    class_model = model['class_model']
    demand_model = model['demand_model']

    # Realizar la predicción de la clase
    class_prediction = class_model.predict(df)

    # Realizar la predicción de la demanda
    demand_prediction = demand_model.predict(df)

    # Devolver ambos resultados como un diccionario
    return {
        "Predicted_Class": class_prediction[0],
        "Predicted_Demand": demand_prediction[0]
    }
print('Se ha corrido con exito')