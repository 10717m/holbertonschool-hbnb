from flask_restx import Namespace, Resource, fields, reqparse
from ...business.facade import Facade

api = Namespace('users', description='User operations')
facade = Facade()

user_model = api.model('User', {
    'id': fields.String(readOnly=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True)
})

@api.route('/')
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        return facade.list_users()

    @api.expect(user_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        data = api.payload
        return facade.create_user(data['first_name'], data['last_name'], data['email']), 201

@api.route('/<string:user_id>')
class UserResource(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Get user by ID"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, f"User {user_id} not found")
        return user

    def delete(self, user_id):
        """Delete a user"""
        user = facade.delete_user(user_id)
        if not user:
            api.abort(404, f"User {user_id} not found")
        return {"message": "User deleted"}, 200

