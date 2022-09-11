from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, username='',email='', password='', g_auth_verify=False, token=''):
        self.id = self.set_id()
        self.username = username
        self.email = email
        self.password = self.set_password(password)
        self.g_auth_verify = g_auth_verify
        self.token = self.set_token(24)

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'Your new account has been created'

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    birth = db.Column(db.Date, nullable=True)
    pronouns = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=True)
    sexuality = db.Column(db.String(50), nullable=True)
    sun = db.Column(db.String(25), nullable=True)
    moon = db.Column(db.String(25), nullable=True)
    rising = db.Column(db.String(25), nullable=True)
    fb = db.Column(db.String(50), nullable=True)
    tt = db.Column(db.String(50), nullable=True)
    ig = db.Column(db.String(50), nullable=True)
    yt = db.Column(db.String(50), nullable=True)
    aspirations = db.Column(db.String(8000), nullable=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, id, name, birth, pronouns, gender, sexuality, sun, moon, rising, fb, tt, ig, yt, aspirations, user_id):
        self.id = id
        self.name = name
        self.birth = birth
        self.pronouns = pronouns
        self.gender = gender
        self.sexuality = sexuality
        self.sun = sun
        self.moon = moon
        self.rising = rising
        self.fb = fb
        self.tt = tt
        self.ig = ig
        self.yt = yt
        self.aspirations = aspirations
        self.user_id = user_id

class AboutSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'birth', 'pronouns', 'gender', 'sexuality', 'sun', 'moon', 'rising', 'fb', 'tt', 'ig', 'yt', 'aspirations', 'user_id']

about_schema = AboutSchema()

class Diety(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(8000), nullable=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,id, name, details, user_id):
        self.id = id
        self.name = name
        self.details = details
        self.user_id = user_id

    def __repr__(self):
        return f'{self.name} has been added to your list of dieties.'

class DietySchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'details', 'user_id']

diety_schema = DietySchema()
dieties_schema = DietySchema(many=True)

class Herb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(8000), nullable=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,id, name, details, user_id):
        self.id = id
        self.name = name
        self.details = details
        self.user_id = user_id

    def __repr__(self):
        return f'{self.name} has been added to your list of herbs.'

class HerbSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'details', 'user_id']

herb_schema = HerbSchema()
herbs_schema = HerbSchema(many=True)

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(8000), nullable=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,id, name, details, user_id):
        self.id = id
        self.name = name
        self.details = details
        self.user_id = user_id

    def __repr__(self):
        return f'{self.name} has been added to your list of tools.'

class ToolSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'details', 'user_id']

tool_schema = ToolSchema()
tools_schema = ToolSchema(many=True)

class Symbol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(8000), nullable=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,id, name, details, user_id):
        self.id = id
        self.name = name
        self.details = details
        self.user_id = user_id

    def __repr__(self):
        return f'{self.name} has been added to your list of symbols.'

class SymbolSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'details', 'user_id']

symbol_schema = SymbolSchema()
symbols_schema = SymbolSchema(many=True)

class Spell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(8000), nullable=True)
    instructions = db.Column(db.String(8000), nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,id, name, ingredients, instructions, date_created, user_id):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.date_created = date_created
        self.user_id = user_id

    def __repr__(self):
        return f'{self.name} has been added to your spells.'

class SpellSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'ingredients', 'instructions', 'date_created', 'user_id']

spell_schema = SpellSchema()
spells_schema = SpellSchema(many=True)

class Ceremony(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(8000), nullable=True)
    instructions = db.Column(db.String(8000), nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,id, name, ingredients, instructions, date_created, user_id):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.date_created = date_created
        self.user_id = user_id

    def __repr__(self):
        return f'{self.name} has been added to your ceremonies.'

class CeremonySchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'ingredients', 'instructions', 'date_created', 'user_id']

ceremony_schema = CeremonySchema()
ceremonies_schema = CeremonySchema(many=True)

class ImpDate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(8000), nullable=True)
    date = db.Column(db.Date, nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,id, name, details, date, date_created, user_id):
        self.id = id
        self.name = name
        self.details = details
        self.date = date
        self.date_created = date_created
        self.user_id = user_id

    def __repr__(self):
        return f'{self.name} has been added.'

class ImpDateSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'details', 'date', 'date_created', 'user_id']

imp_date_schema = ImpDateSchema()
imp_dates_schema = ImpDateSchema(many=True)

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(8000), nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,id, name, details, date_created, user_id):
        self.id = id
        self.name = name
        self.details = details
        self.date_created = date_created
        self.user_id = user_id

    def __repr__(self):
        return f'{self.name} has been added.'

class JournalSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'details', 'date_created', 'user_id']

journal_schema = JournalSchema()
journals_schema = JournalSchema(many=True)