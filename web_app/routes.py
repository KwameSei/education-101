from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/home')
def home():
    return render_template('home.html')

@routes.route('/about')
def about():
    return render_template('home.html')