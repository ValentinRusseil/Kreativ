from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from Kreativ.settings import SENDGRID_API_KEY

# Create your views here.
def contact_page(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('number')
        entreprise = request.POST.get('entreprise')
        msg = request.POST.get('message')

        to_email="matteo.pereira@ynov.com"
        subject="Demande de contact"
        html_content=f"<div style='white-space:pre'>\n\n\Demande de contact de {nom} {prenom},\n\n    Voici son mail : {email},\n\n    Voici son contact :\n telephone : {telephone}\n    entreprise: {entreprise}\n message : {msg}\n\n</div>"
        response = send_email(to_email, subject, html_content)
        if response == 202:
            return HttpResponse('Email sent successfully!')
        else:
            return HttpResponse('Failed to send email.')    
    # Ajout d'un retour explicite pour les cas où la méthode n'est pas POST
    if request.method != 'POST':
        return render(request, 'contact.html', context={})

def send_email(to_email, subject, html_content):
    message = Mail(
        from_email="matteo.pereira@ynov.com",
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"SendGrid Response Status: {response.status_code}")
        print(f"SendGrid Response Body: {response.body}")
        print(f"SendGrid Response Headers: {response.headers}")
        return response.status_code
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")
        return str(e)