from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre import GenreSchema
from implemented import genre_service
from utils import auth_required, admin_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    # @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    # # @admin_required
    # def post(self):
    #     user_jsn = request.json
    #     user = genre_service.create(user_jsn)
    #     return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    # @auth_required
    def get(self, gid):
        r = genre_service.get_one(gid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    # # @admin_required
    # def put(self, gid):
    #     data = request.json
    #     if 'id' not in data:
    #         data['id'] = gid
    #     genre_service.update(data)
    #     return "", 204
    #
    # # @admin_required
    # def delete(self, gid):
    #     genre_service.delete(gid)
    #     return "", 204
