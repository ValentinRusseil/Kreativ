from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import os

# Create your views here.
def contact_page(request):
    context = {}  # Initialiser le contexte
    
    if request.method == 'POST':
        # Récupération des données du formulaire
        form_data = {
            'nom': request.POST.get('nom'),
            'prenom': request.POST.get('prenom'),
            'email': request.POST.get('email'),
            'telephone': request.POST.get('number'),
            'entreprise': request.POST.get('entreprise'),
            'message': request.POST.get('message')
        }
        
        # Ajouter les données du formulaire au contexte
        context.update(form_data)

        subject="Demande de contact"
        html_content=f"""<div style='white-space:pre'>
            Demande de contact de {form_data['nom']} {form_data['prenom']},

                Voici son mail : {form_data['email']},

                Voici son contact :
                telephone : {form_data['telephone']}
                entreprise: {form_data['entreprise']}
                message : {form_data['message']}

            </div>"""
            
        response = send_email(subject, html_content)
        if response == 202:
            context['message'] = 'Votre message a été envoyé avec succès !'
            # Vider les champs du formulaire en cas de succès
            context.update({k: '' for k in form_data.keys()})
        else:
            context['message'] = f'Échec de l\'envoi du message. Erreur avec le serveur.'

    return render(request, 'contact.html', {'context': context})

def send_email(subject, html_content):
    # Liste des destinataires
    to_emails = [
        # Ajoutez d'autres destinataires si nécessaire
        # "hi.kreativmedia@gmail.com",
        "russeilvalentin6@gmail.com"
    ]

    message = Mail(
        from_email="matteo.pereira@ynov.com",
        to_emails=to_emails,
        subject=subject,
        html_content=html_content
    )
    try:
        print("success")
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        message = sg.send(message)
        return message.status_code
    except Exception as e:
        print("error")
        print(f"Erreur lors de l'envoi de l'email : {str(e)}")
        print(f"Type d'erreur : {type(e)}")
        if hasattr(e, 'body'):
            print(f"Corps de l'erreur : {e.body}")
        return str(e)