from flask_restx import Resource, Namespace
from flask import request
from implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        data = request.json
        user_service.create(data)
        return '', 201


@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        data = request.json
        return auth_service.checking_user(data)

    def put(self):
        data = request.json
        return auth_service.approve_new_tokens(data)

