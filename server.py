from flask import Flask
from os import walk
import json

# Inicializar Flask
app = Flask(__name__)
app._static_folder = "static"

# Deshabilitar Console Logs
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Cargar JSON de idiomas y paises
langCountries = []

availableLangs = []
for (dirpath, dirnames, filenames) in walk("languages"):
    for i in filenames:
        availableLangs.append(i.replace(".json",""))
    break
print("\n\033[36mAvailable languages: "+str(availableLangs)+"\033[0m")

# Cargar traducciones
loadedTranslations = {}

# Importar rutas
print("\033[92m",end="")
import routes
print("\033[0m",end="")
