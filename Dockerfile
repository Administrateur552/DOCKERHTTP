# Utiliser une image Python officielle
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /

# Copier les fichiers nécessaires pour l'application
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r docker-https/requirements.txt

# Exposer le port utilisé par l'application
EXPOSE 8000

# Démarrer l'application
CMD ["python", "main.py"]
