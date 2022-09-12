from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Entry, entry_schema, entries_schema
from flask_login import current_user

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/entries', methods=['POST'])
@token_required
def create_entry(current_user):
    name = request.json['name']
    details = request.json['details']
    user_id = current_user.id

    print(f'create journal entry test: {current_user.id}')

    entry = Entry(name=name, details=details, user_id=user_id)

    db.session.add(entry)
    db.session.commit()

    response = entry_schema.dump(entry)
    return jsonify(response)

@api.route('/entries', methods = ['GET'])
@token_required
def getJournalEntries(current_user):
    a_user = current_user.id
    entry = Entry.query.filter_by(user_id = a_user).all()
    response = entries_schema.dump(entry)
    return jsonify(response)