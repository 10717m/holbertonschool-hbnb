# app/api/auth_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.repositories.user_repository import user_repository  # your repo for fetching users

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = user_repository.get_by_email(email)

    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

