#Este archivo se encargará de cargar el modelo entrenado.
import joblib

# Función para cargar el modelo previamente entrenado
def load_model():
    model = joblib.load('../modelo_entrenado.pkl')  # Ruta del archivo del modelo
    return model