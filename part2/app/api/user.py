from flask_restx import Namespace, Resource

user_ns = Namespace("users", description="User operations")

@user_ns.route("/")
class UserList(Resource):
    def get(self):
        return {"message": "List of users"}

    def post(self):
        return {"message": "Create user"}, 201
