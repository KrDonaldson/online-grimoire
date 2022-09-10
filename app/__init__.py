from flask import Flask, render_template
from .site.routes import site
from config import Config

app = Flask(__name__)

app.register_blueprint(site)
app.config.from_object(Config)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html")