# Usa una imagen base de Python 3.12 con la versión slim (más ligera)
FROM python:3.12-slim

# Instalar distutils y otras dependencias del sistema necesarias para compilar paquetes
RUN apt-get update && apt-get install -y \
    python3-distutils \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia todos los archivos del directorio actual en el contenedor dentro de /app
COPY . /app

# Establece el directorio de trabajo dentro del contenedor en /app
WORKDIR /app

# Instala las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar el script main.py
#CMD ["python", "main.py"]