from flask_restx import Resource, Namespace
from flask import request
from dao.model.user import UserSchema
from implemented import user_service, auth_service

user_ns = Namespace('users')


@user_ns.route('/password')
class UserView(Resource):
    def put(self):
        data = request.json
        return auth_service.approve_new_tokens(data)

@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        r = user_service.get_one(uid)
        sm_d = UserSchema().dump(r)
        return sm_d, 200

    def patch(self, uid):
        data = request.json
        user_service.update(data)
        return "", 204



