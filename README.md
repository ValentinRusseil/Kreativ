# Kreativ

## Installer les dépendances

Pour les dépendances :
```
pip install -r requirements.txt
```

## Migrations et accès à la base de données

Pour faire les migrations suite à des changements de la base de données :
```
python3 manage.py makemigrations <nomApp>
```

Pour choisir le numéro de migration pour la base de données :
```
python3 manage.py sqlmigrate <nomApp> <version>
```

Pour faire la migration sur l'application :
```
python3 manage.py migrate
```

Pour accéder à la base de données via le shell :
```
python manage.py shell
```

## Lancer le serveur

```
./manage.py runserver
```

```
python3 ./manage.py runserver
```
