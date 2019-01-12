from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FREEZER_RELATIVE_URLS = True

app = Flask(__name__)
app.config.from_object(__name__)

# return une liste avec les fichiers plats
pages = FlatPages(app)

freezer = Freezer(app)

#dictionnaire URL externe (liens sociaux)
ext_urls= {
	'youtube' : "https://www.youtube.com/channel/UCwJfS8Tbh1Pw7FUWVlSOh3A",
	'instagram' : "https://www.instagram.com/marcypolis"
}

@app.route('/')
def index():
    latest = sorted(pages, reverse=True,
                    key=lambda page: page.meta['date'])
    return render_template('index.html', pages=latest, ext_urls=ext_urls)

@app.route('/contact/')
def contact():
    return render_template('contact.html', ext_urls=ext_urls)

@app.route('/je-suifemmes-multitachess/')
def je_suis():
    return render_template('je-suis.html', ext_urls=ext_urls)

@app.route('/<path:chemin>/')
#chemin = 'hello/'
def page(chemin):
    ret = pages.get_or_404(chemin)
    print("building : ", ret['titre'])
    if chemin == 'HTMLonly':
        return ret.html
    else:
        return render_template('page.html', page=ret, ext_urls=ext_urls)

if __name__ == '__main__':
    app.run(port=8000)
    #freezer.freeze()
