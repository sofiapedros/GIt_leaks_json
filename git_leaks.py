from git import Repo
import re  # signal
import sys
import signal
import json

# Variables globales
# Ruta del repositorio sobre el que se van a buscar commits
REPO_DIR = './skale-manager'

# Palabras clave a buscar en los commits
KEY_WORDS = ['credentials', 'password', 'key', 'username', 'private']  


def extract(repo_dir):
    '''
    Función que extrae los commits del repositorio
    '''
    repo = Repo(repo_dir)
    commits = list(repo.iter_commits('develop'))
    return commits

def transform(commits):
    '''
    Función que guarda los commits que encuentra en un diccionario
    con su id y su mensaje.
    '''
    
    # Empezamos con un diccionario vacío
    diccionario = dict()
    diccionario['commits'] = []
    
    # Por cada commits de los commits
    for commit in commits:
        # Busca cada palabra de las palabras clave
        for word in KEY_WORDS:
            # Si encuentra esa palabra, añade al diccionario el id del commit con
            # su mensaje, dentro de commits
            if re.search(word, commit.message, re.IGNORECASE):

                diccionario['commits'].append({
                'id': commit.hexsha,
                'message': commit.message,})

    return diccionario

def load(diccionario):
    ''' 
    Función que carga los datos en un json
    '''
    with open('git_leaks.json', 'w') as file:
        json.dump(diccionario, file, indent=4)


def handler_signal(signal, frame):
    '''
    Función para controlar la salida con la señal SIGINT (CTRL + C)
    '''
    print("\n\n[!] Out ............. \n")
    sys.exit(1)


if __name__ == '__main__':
    '''
    Proceso principal que llama a las tres funciones para hacer la ETL
    '''
    signal.signal(signal.SIGINT, handler_signal)
    commits = extract(REPO_DIR)
    diccionario = transform(commits)
    load(diccionario)