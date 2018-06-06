from flask import Flask, render_template
from data import emotions, movies

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', emotions=emotions)


@app.route('/search')
def search():
    return render_template('search.html', movies=movies)


if __name__ == '__main__':
    app.run()