# Kreativ

## Installer les dépendances

Pour les dépendances :
```
pip install -r requirements.txt
```

Initialiser ses dépendences avec tailwind :
```
python3 manage.py tailwind start
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

Lancer le serveur web et tailwind :

```
python3 startProject.py
```

## Ajouter une nouvelle application

```
django-admin startapp <nomApp>
```

Après l'ajout de votre application, il faut ajouter votre app dans le fichier settings.py dans la partie "INSTALLED_APPS" à la suite sous cette forme : '<nomApp>'

## Installer les dépendences

Pour installer les dépendences, il faut vous situer dans le dossier static et exécuter cette commande : ``` npm install ```