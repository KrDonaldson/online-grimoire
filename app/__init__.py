from flask import Flask, render_template
from .site.routes import site
from .auth.routes import auth
from config import Config

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html")