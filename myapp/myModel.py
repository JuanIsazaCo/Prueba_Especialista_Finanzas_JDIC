#Este archivo se encargará de cargar el modelo entrenado.
import joblib

# Función para cargar el modelo previamente entrenado
def load_model():
    try:
        model = joblib.load(r'C:\Users\jisaza53\Especialista_Finanzas_JDIC\modelo_entrenado.pkl')
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        raise
    return model