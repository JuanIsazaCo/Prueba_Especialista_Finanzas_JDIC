# Usa una imagen base de Python 3.12 con la versión slim (más ligera)
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor en /app
WORKDIR /app

# Copia los archivos del proyecto en el contenedor
COPY . /app/
# Copiar el archivo del modelo entrenado
COPY modelo_entrenado.pkl /app/

# Instala las dependencias desde el archivo requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expon el puerto para que FastAPI pueda funcionar
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]