# Usamos una imagen oficial de Python
FROM python:3.10

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos necesarios
COPY main.py test_main.py ./

# Comando por defecto al ejecutar el contenedor
CMD ["python", "main.py"]