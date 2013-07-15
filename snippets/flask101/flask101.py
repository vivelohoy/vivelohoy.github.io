from flask import Flask, render_template
from flask.ext.cache import Cache
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE':'simple'})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'

db = SQLAlchemy(app)

# Models 
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    date_born = db.Column(db.DateTime)
    employed = db.Column(db.Boolean)
    about = db.Column(db.Text)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<Person %r>' % self.first_name

# application routes
@app.route('/')
@cache.cached(timeout=50)
def show_home():
    return render_template('base.html', message='Wow this is so cool.')

@app.route('/about')
def show_post():
    return render_template('about.html')

@app.route('/calc')
@cache.cached(timeout=10)
def do_math():
    total = 0
    for x in range(1000000):
        total += x

    return str(total)
        
if __name__ == '__main__':
    app.run(debug=True)
