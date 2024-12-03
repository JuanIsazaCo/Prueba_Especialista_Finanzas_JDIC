# API para Predecir la Demanda

Este proyecto contiene una API para predecir la demanda de clientes utilizando un modelo previamente entrenado con **scikit-learn**.

## Requisitos

Instalar las dependencias con `pip`:

```bash
pip install -r requirements.txt

## Correr API

1. Ejecuta en la terminal el siguiente codigo que utiliza Uvicorn como servidor con el siguiente comando:
docker run -d -p 8000:8000 prueba_especialista

py -m uvicorn myapp.main:app --reload

2. ingresar a http://127.0.0.1:8000/docs#/ para testar el proyecto
