from django.shortcuts import render

def a_propos_page(request):
    return render(request, template_name="a_propos.html", context={})