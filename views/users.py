import jwt
from flask_restx import Resource, Namespace
from flask import request
from dao.model.user import UserSchema
from implemented import user_service, auth_service
from utils import auth_required, secret, algo

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        email = jwt.decode(token, secret, algorithms=algo).get('email')
        r = user_service.get_by_email(email)
        sm_d = UserSchema().dump(r)
        return sm_d, 200

    @auth_required
    def patch(self):
        data = request.json
        user_service.update(data)
        return "", 204


@user_ns.route('/password')
class UserView(Resource):
    @auth_required
    def put(self):
        data = request.json
        return auth_service.approve_new_tokens(data)

