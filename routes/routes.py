from flask import request, render_template, redirect, url_for
from server import app, langCountries, availableLangs, loadedTranslations
import xml.dom.minidom 

def detectVisitorCountryAndLang():
    return 0

##################################################################################

# Rotbots.txt
@app.route('/robots.txt')
async def robots():
    robotsString = """User-agent: *
Allow: /

# Sitemap location
Sitemap: https://www.hostie.me/sitemap.xml
    """
    return robotsString

# SITEMAP
@app.route('/sitemap.xml')
async def sitemap():
    blackList = ["/static/<path:filename>", "/sitemap.xml", "/robots.txt", "/"]

    urlMap = []
    for rule in app.url_map.iter_rules():
            urlMap.append(rule.rule)

    auxUrlMap = []
    for i in urlMap:
        check = True
        for x in blackList:
            if i == x:
                check = False
                break
        if check:
            auxUrlMap.append(i)
    urlMap = auxUrlMap

    sitemapString = ""
    for i in urlMap:
        sitemapString+="<url>\n"
        for x in availableLangs:
            if x == "en-EN":
                sitemapString+="<loc>https://www.hostie.me"+i.replace("<lang_country>", x)+"</loc><br>\n"
                sitemapString+='<xhtml:link rel="alternate" hreflang="'+x+'" href="https://www.hostie.me'+i.replace("<lang_country>", x)+'" /><br>\n'
            else:
                sitemapString+='<xhtml:link rel="alternate" hreflang="'+x+'" href="https://www.hostie.me'+i.replace("<lang_country>", x)+'" /><br>\n'
        sitemapString+="</url>\n"

    return sitemapString

##################################################################################

# Redirección de la raíz '/' a '/en-EN'
@app.route('/')
def root():
    return redirect('/en-EN')

# Página principal
@app.route('/<lang_country>')
async def index(lang_country):
    return render_template('index.html')

##################################################################################


# Página soluciones
@app.route('/<lang_country>/solutions')
async def solutions():
    return render_template('pricing.html')


# Página premios
@app.route('/<lang_country>/awards')
async def awards():
    return render_template('pricing.html')


# Página calidad
@app.route('/<lang_country>/quality')
async def quality():
    return render_template('pricing.html')


# Página precios
@app.route('/<lang_country>/pricing')
async def pricing():
    return render_template('pricing.html')


# Página contacto
@app.route('/<lang_country>/contact')
async def contact():
    return render_template('contact.html')


# Página próximamente
@app.route('/<lang_country>/comin-soon')
async def comin_soon():
    return render_template('comin-soon.html')


# Página política de privacidad
@app.route('/<lang_country>/privacy-policy')
async def privacy_policy():
    return render_template('comin-soon.html')


# Página política de cookies
@app.route('/<lang_country>/cookies-policy')
async def cookies_policy():
    return render_template('comin-soon.html')


# Página términos y condiciones
@app.route('/<lang_country>/terms-and-conditions')
async def terms_and_conditions():
    return render_template('comin-soon.html')


# Página aviso legal
@app.route('/<lang_country>/legal-notice')
async def legal_notice():
    return render_template('comin-soon.html')