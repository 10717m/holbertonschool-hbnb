from flask import Flask
from flask_restx import Api
from app.api import user_ns  # استدعاء من واجهة المستخدم، لاحقاً تضيف باقي الـ namespaces

def create_app():
    app = Flask(__name__)
    api = Api(app, version="1.0", title="HBnB API", description="HBnB API with Flask-RESTx")
    
    api.add_namespace(user_ns, path="/users")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
