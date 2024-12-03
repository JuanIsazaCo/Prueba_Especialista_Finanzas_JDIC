# Usa una imagen base de Python 3.12 con la versión slim (más ligera)
FROM python:3.12-slim

# Copia todos los archivos del directorio actual en el contenedor dentro de /app
COPY . /app/

# Establece el directorio de trabajo dentro del contenedor en /app
WORKDIR /app

# Instala las dependencias desde el archivo requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Comando por defecto para ejecutar el script main.py
CMD ["python", "main.py"]

VOLUME /app

# Expón el puerto 8000, que es donde la aplicación escuchará
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]