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






@app.route('/')
def index():
    return render_template('index.html', pages=pages)


@app.route('/<path:chemin>/')
#chemin = 'hello/'
def page(chemin):
    ret = pages.get_or_404(chemin)
    print("titre", ret['titre'])
    if chemin == 'hello':
        return ret.html
    else:
        return render_template('page.html', page=ret)







if __name__ == '__main__':
    #app.run(port=8000)
    freezer.freeze()
