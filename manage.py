#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Kreativ.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    subprocess.Popen(["bash", "-c", "npm run dev"], cwd="theme/static_src", stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
