from flask import Flask, render_template, request, redirect, url_for, make_response
from server import app, DEFAULT_LANG, LANGUAGES, PAGES
from datetime import datetime

@app.route("/sitemap.xml")
def sitemap():
    host_base = request.host_url.rstrip("/")
    pages = []
    
    # Add static pages
    for page in PAGES:
        url_set = []
        for lang in LANGUAGES.keys():
            url = f"{host_base}/{lang}/{'' if page == 'index' else page}"
            url_set.append({
                "loc": url,
                "hreflang": lang
            })
        pages.append({
            "urls": url_set,
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "weekly"
        })
    
    sitemap_xml = render_template("sitemap.xml", pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    
    return response

@app.route("/robots.txt")
def robots_txt():
    return """
User-agent: *
Allow: /
Sitemap: {}sitemap.xml
""".format(request.url_root), 200, {"Content-Type": "text/plain"}