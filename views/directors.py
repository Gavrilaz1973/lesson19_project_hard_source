from flask_restx import Resource, Namespace
#from flask import request
from dao.model.director import DirectorSchema
from implemented import director_service
#from utils import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    # @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    # # @admin_required
    # def post(self):
    #     user_jsn = request.json
    #     user = director_service.create(user_jsn)
    #     return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    # @auth_required
    def get(self, did):
        r = director_service.get_one(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    # # @admin_required
    # def put(self, rid):
    #     data = request.json
    #     if 'id' not in data:
    #         data['id'] = rid
    #     director_service.update(data)
    #     return "", 204
    #
    # # @admin_required
    # def delete(self, rid):
    #     director_service.delete(rid)
    #     return "", 204
