import subprocess
 
# Commandes à exécuter
commands = [
["python3", "manage.py", "runserver"],
["python3", "manage.py", "tailwind", "start"]
]
 
processes = []
for command in commands:
    processes.append(subprocess.Popen(command))
 
# Attend que tous les processus se terminent
for process in processes:
    process.wait()