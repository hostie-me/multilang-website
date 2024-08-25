from flask import Flask, render_template, request, redirect, url_for, make_response
import json, os
from dotenv import load_dotenv

app = Flask(__name__)
app._static_folder = "static"

# Disable Console Logs
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

load_dotenv()
PAGES = json.loads(os.getenv("PAGES"))
DEFAULT_LANG = os.getenv("DEFAULT_LANG")
LANGUAGES = json.loads(os.getenv("LANGUAGES"))

for language in LANGUAGES.keys():
    with open(f"translations/{language}.json", "r", encoding="utf-8") as file:
        app.config[language] = json.load(file)

def get_preferred_language(accept_language):
    languages = accept_language.split(",")
    for language in languages:
        lang_code = language.split(";")[0].strip()
        if lang_code in LANGUAGES:
            return lang_code
        # Check for partial matches (e.g., "es" for "es-ES" or "es-MX")
        for supported_lang in LANGUAGES:
            if lang_code.split("-")[0] == supported_lang.split("-")[0]:
                return supported_lang
    return DEFAULT_LANG