from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/ceremonies')
def ceremonies():
    return render_template('ceremonies.html')

@site.route('/dieties')
def dieties():
    return render_template('dieties.html')

@site.route('/herbs')
def herbs():
    return render_template('herbs.html')

@site.route('/holidays')
def holidays():
    return render_template('holidays.html')

@site.route('/journal')
def journal():
    return render_template('journal.html')

@site.route('/spells')
def spells():
    return render_template('spells.html')

@site.route('/symbols')
def symbols():
    return render_template('symbols.html')

@site.route('/tools')
def tools():
    return render_template('tools.html')