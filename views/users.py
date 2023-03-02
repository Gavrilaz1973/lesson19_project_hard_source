from flask_restx import Resource, Namespace
from flask import request
from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        rs = user_service.get_all()
        res = UserSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        user_jsn = request.json
        user = user_service.create(user_jsn)
        return "", 201


@user_ns.route('/<int:rid>')
class UserView(Resource):
    def get(self, rid):
        r = user_service.get_one(rid)
        sm_d = UserSchema().dump(r)
        return sm_d, 200

    def put(self, rid):
        data = request.json
        if 'id' not in data:
            data['id'] = rid
        user_service.update(data)
        return "", 204

    def delete(self, rid):
        user_service.delete(rid)
        return "", 204


