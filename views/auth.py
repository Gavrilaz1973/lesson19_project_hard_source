from flask_restx import Resource, Namespace
from flask import request
from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def get(self):
        data = request.json
        username = data.get('username')
        password = data.get('password')
        if not all([username, password]):
            return "", 404
        tokens = auth_service.generate_tokens(username, password)
        return tokens, 201

    def put(self):
        data = request.json
        refresh_token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201
