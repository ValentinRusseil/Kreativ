# Étape 1 : construire les assets statiques (JS/CSS)
FROM node:20 AS frontend-builder

WORKDIR /app
COPY ./theme/static_src ./theme/static_src
COPY ./templates ./templates
COPY ./aPropos/templates ./aPropos/templates
COPY ./Articles/templates ./Articles/templates
COPY ./Contact/templates ./Contact/templates
COPY ./Evenements/templates ./Evenements/templates
COPY ./SousContenu/templates ./SousContenu/templates
WORKDIR /app/theme/static_src
RUN npm install && npm run build

# Étape 2 : environnement Python
FROM python:3.12-slim

# Dépendances système
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Créer un dossier pour l’app
WORKDIR /app

# Copier le code Python
COPY . .

# Copier les fichiers statiques du build Node
COPY --from=frontend-builder /app/theme/static/css/dist ./theme/static/css/dist
RUN ls -al /app/theme/static/css/dist

# Installer les dépendances Python
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Collecte des fichiers statiques et migrations
RUN python manage.py collectstatic --noinput \
    && python manage.py migrate

# Démarrer Gunicorn
CMD ["gunicorn", "Kreativ.wsgi:application", "--bind", "0.0.0.0:8000"]
