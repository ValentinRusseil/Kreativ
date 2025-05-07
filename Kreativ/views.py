from django.shortcuts import render
from .instagram_fetcher import get_recent_posts
from django.http import JsonResponse

def get_instagram_posts():
    posts = get_recent_posts()
    print(posts)
    return JsonResponse(posts, safe=False)
    

def contenu_posts():
    # Récupérer les posts Instagram
    instagram_posts = get_instagram_posts()
    
    # Posts statiques par défaut
    default_posts = [
        {"title": "Titre", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": "images/wallpaper/fond_contenu.png"},
        {"title": "Titre 1", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": "images/wallpaper/fond_contenu.png"},
        {"title": "Titre 2", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": "images/wallpaper/fond_contenu.png"},
        {"title": "Titre 3", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": None},
        {"title": "Titre 4", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": None},
    ]
    
    if instagram_posts:
        return instagram_posts
    else:
        return default_posts

def home_page(request):
    contenus = contenu_posts()
    
    return render(request, template_name="home_page.html", context={'contenus': contenus})