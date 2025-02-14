import subprocess
import sys
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Lance le serveur Tailwind avec npm'

    def handle(self, *args, **kwargs):
        # Éviter le rechargement multiple
        if 'runserver' in sys.argv and os.environ.get('RUN_MAIN') != 'true':
            self.stdout.write(self.style.WARNING('Auto-reloader détecté, Tailwind ne sera pas lancé.'))
            return
        
        try:
            self.stdout.write(self.style.SUCCESS('Démarrage de Tailwind...'))
            subprocess.run(["bash", "-c", "npm run dev"], cwd="theme/static_src")
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Erreur : {e}'))
