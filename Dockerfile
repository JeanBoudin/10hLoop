# Utiliser une image Python officielle
FROM python:3.12-slim

# Installer ffmpeg et autres dépendances
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libavcodec-extra \
    libavformat-dev \
    libavfilter-dev \
    libavdevice-dev \
    && rm -rf /var/lib/apt/lists/*


# Copier le fichier requirements.txt dans l'image
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code Python dans l'image
COPY . .

# Exécuter le script Python
CMD ["python", "script.py"]
