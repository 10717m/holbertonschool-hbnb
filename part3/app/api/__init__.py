# app/api/__init__.py

from .admin_routes import admin_bp
api_bp.register_blueprint(admin_bp)

