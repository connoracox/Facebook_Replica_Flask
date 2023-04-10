from . import bp as main_bp
from flask import render_template

@main_bp.route('/')
def index():
    cdn = {
        'instructors': ('lucas', 'dylan'),
        'students' : ['blane', 'ashmika', 'abe', 'zion', 'connor', 'martin', 'noah', 'erm']
    }
    return render_template('index.jinja', cdn=cdn, title='Home')

@main_bp.route('/about')
def about():
    return render_template('about.jinja')


