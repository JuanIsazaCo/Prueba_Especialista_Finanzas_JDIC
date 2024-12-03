import joblib
import os

# Función para cargar el modelo previamente entrenado
def load_model():
    try:
        # Obtiene la ruta del directorio donde se encuentra este archivo
        dir_actual = os.path.dirname(__file__)
        
        # Construye la ruta al archivo 'modelo_entrenado.pkl' en el mismo directorio
        modelo_path = os.path.join(dir_actual, 'modelo_entrenado.pkl')
        
        # Carga el modelo
        model = joblib.load(modelo_path)
        
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        raise
    
    return model