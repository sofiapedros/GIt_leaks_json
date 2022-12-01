# Git_leaks_json
Buscador de palabras clave en commits para buscar posibles vulnerabilidades en el repositorio de skale. Guarda los resultados obtenidos en un json llamado "git_leaks.json"

Hay cuatro documentos:
- skale-manager
- git_leaks.py
- requirements.txt
- git_leaks.json

### skale-manager
Es un directorio que continen el repositorio de skale sobre el que se van a buscar los commits.


### git_leaks.py
git_leaks.py: al ejecutarse, guarda en un fichero json (git_leaks.json) los commits que contengan alguna de las palabras consideradas como 'sensibles' para buscar leaks ('private', 'key'...). Para ello, guarda todos los commits con alguna palabra clave en un diccionario cuya clave es el id del commit y cuyo valor es el mensaje correspondiente. Al final del programa, se guardan los valores del diccionario con sus claves correspondientes en un fichero json llamado "git_leaks.json"

### requirements.txt
requirements.txt: contiene todas las librerías usadas en el desarrollo del programa para que se puedan descargar con pip install -r requirements.txt

### git_leaks.json
Salida del programa git_leaks.py
