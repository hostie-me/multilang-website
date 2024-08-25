from flask import Flask, render_template, request, redirect, url_for, make_response
from server import app, get_preferred_language, DEFAULT_LANG, LANGUAGES


@app.route("/<lang>/privacy-policy")
def lang_privacy_policy(lang):
    if lang not in LANGUAGES:
        return redirect(url_for("lang_privacy_policy", lang=DEFAULT_LANG))
    
    return render_template("coming-soon.html", translations=app.config[lang], current_lang=lang, languages=LANGUAGES)


@app.route("/<lang>/cookies-policy")
def lang_cookies_policy(lang):
    if lang not in LANGUAGES:
        return redirect(url_for("lang_cookies_policy", lang=DEFAULT_LANG))
    
    return render_template("coming-soon.html", translations=app.config[lang], current_lang=lang, languages=LANGUAGES)


@app.route("/<lang>/terms-and-conditions")
def lang_terms_and_conditions(lang):
    if lang not in LANGUAGES:
        return redirect(url_for("lang_terms_and_conditions", lang=DEFAULT_LANG))
    
    return render_template("coming-soon.html", translations=app.config[lang], current_lang=lang, languages=LANGUAGES)