# app/utils/auth_utils.py

from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from functools import wraps
from app.repositories.user_repository import user_repository

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = user_repository.get_by_id(user_id)
        if not user or not user.is_admin:
            return jsonify({"message": "Admin access required"}), 403
        return fn(*args, **kwargs)
    return wrapper

