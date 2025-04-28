from django.shortcuts import render

# Create your views here.
def evenement_page(request):
    return render(request, 'evenement_page.html')
