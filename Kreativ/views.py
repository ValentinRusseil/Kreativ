from django.shortcuts import render

def home_page(request):
    contenus = [
        {"title": "Titre", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": "image1.jpg"},
        {"title": "Titre", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": None},
        {"title": "Titre", "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "image": None},
    ]
    return render(request, template_name="home_page.html", context={'contenus': contenus})