from django.shortcuts import render
import requests
import os
from django.conf import settings

def get_instagram_posts():
    # Récupérer le token d'accès depuis les variables d'environnement
    access_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
    instagram_account_id = os.getenv('INSTAGRAM_ACCOUNT_ID')
    
    if not access_token or not instagram_account_id:
        return []
    
    # URL de l'API Instagram Graph
    url = f'https://graph.instagram.com/v12.0/{instagram_account_id}/media'
    params = {
        'access_token': access_token,
        'fields': 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        posts = []
        for post in data.get('data', []):
            posts.append({
                'title': post.get('caption', '')[:50] + '...' if post.get('caption') else 'Post Instagram',
                'description': post.get('caption', ''),
                'image': post.get('media_url'),
                'link': post.get('permalink'),
                'type': post.get('media_type')
            })
        return posts
    except Exception as e:
        print(f"Erreur lors de la récupération des posts Instagram: {str(e)}")
        return []

def contenu_posts():
    # Récupérer les posts Instagram
    instagram_posts = get_instagram_posts()
    
    # Posts statiques par défaut
    default_posts = [
        {"title": "Titre", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": "images/wallpaper/fond_contenu.png"},
        {"title": "Titre 1", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": None},
        {"title": "Titre 2", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": None},
        {"title": "Titre 3", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": None},
        {"title": "Titre 4", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": None},
        {"title": "Titre 5", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": None},
        {"title": "Titre 6", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": None},
    ]
    
    if instagram_posts:
        return instagram_posts
    else:
        return default_posts

def home_page(request):
    contenus = contenu_posts()
    
    return render(request, template_name="home_page.html", context={'contenus': contenus})

def confidentiality_page(request):
    return render(request, template_name="confidentiality_page.html")