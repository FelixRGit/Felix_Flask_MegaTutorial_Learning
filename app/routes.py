from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Felix'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful Day in Heimsheim'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)