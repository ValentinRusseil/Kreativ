from django.shortcuts import render
from Kreativ.views import contenu_posts
# Create your views here.
def contenu_page(request):
    contenus = contenu_posts()
    return render(request, 'contenu.html', {'contenus': contenus})
