from flask_restx import Api
from flask import Blueprint
from .routes.user_routes import api as user_ns

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp, title='HBnB API', version='1.0', description='API for the HBnB Application')

# Register Namespaces
api.add_namespace(user_ns)

def init_app(app):
    app.register_blueprint(api_bp)
