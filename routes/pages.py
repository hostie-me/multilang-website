from flask import Flask, render_template, request, redirect, url_for, make_response
from server import app, get_preferred_language, DEFAULT_LANG, LANGUAGES


@app.route("/")
def index():
    accept_language = request.headers.get("Accept-Language", DEFAULT_LANG)
    preferred_lang = get_preferred_language(accept_language)
    return redirect(url_for("lang_index", lang=preferred_lang))


@app.route("/<lang>/")
def lang_index(lang):
    if lang not in LANGUAGES: return redirect(url_for("lang_index", lang=DEFAULT_LANG))
    return render_template("index.html", translations=app.config[lang], current_lang=lang)


@app.route("/<lang>/solutions")
def lang_solutions(lang):
    if lang not in LANGUAGES: return redirect(url_for("lang_solutions", lang=DEFAULT_LANG))

    title = app.config[lang]["title_solutions"]
    description = app.config[lang]["content_solutions"]

    return render_template("solutions.html", title=title, description=description, translations=app.config[lang], current_lang=lang)


@app.route("/<lang>/awards")
def lang_awards(lang):
    if lang not in LANGUAGES: return redirect(url_for("lang_awards", lang=DEFAULT_LANG))

    title = app.config[lang]["title_awards"]
    description = app.config[lang]["content_awards"]

    return render_template("awards.html", title=title, description=description, translations=app.config[lang], current_lang=lang)


@app.route("/<lang>/certifications")
def lang_certifications(lang):
    if lang not in LANGUAGES: return redirect(url_for("lang_coming_soon", lang=DEFAULT_LANG))
    return render_template("coming-soon.html", translations=app.config[lang], current_lang=lang)


@app.route("/<lang>/pricing")
def lang_pricing(lang):
    if lang not in LANGUAGES: return redirect(url_for("lang_pricing", lang=DEFAULT_LANG))
    
    title = app.config[lang]["title_pricing"]
    description = app.config[lang]["content_pricing"]
    data_wf_page = "6690d4fcf3709b75ac575a43"

    return render_template("pricing.html", title=title, description=description, data_wf_page=data_wf_page, translations=app.config[lang], current_lang=lang)


@app.route("/<lang>/contact")
def lang_contact(lang):
    if lang not in LANGUAGES: return redirect(url_for("lang_contact", lang=DEFAULT_LANG))

    title = app.config[lang]["title_contact"]
    description = app.config[lang]["content_contact"]
    data_wf_page = "6690d4fcf3709b75ac575a42"

    return render_template("contact.html", title=title, description=description, data_wf_page=data_wf_page, translations=app.config[lang], current_lang=lang)


@app.route("/<lang>/coming-soon")
def lang_coming_soon(lang):
    if lang not in LANGUAGES: return redirect(url_for("lang_coming_soon", lang=DEFAULT_LANG))
    return render_template("coming-soon.html", translations=app.config[lang], current_lang=lang)