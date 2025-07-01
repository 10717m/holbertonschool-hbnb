# app/api/admin_routes.py

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth_utils import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard', methods=['GET'])
@jwt_required()
@admin_required
def admin_dashboard():
    return jsonify({"message": "Welcome, Admin!"})

