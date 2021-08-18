from http.client import responses
from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import User as UserDto
from src.main.adapters import flask_adapter

from src.main.compose import create_user_composer

user_namespace = Namespace('users')
user = user_namespace.model('User', UserDto)


@user_namespace.route('/')
class ListUsers(Resource):

    @user_namespace.expect(user)
    @user_namespace.doc(responses={201: 'Created',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def post(self):
        response = flask_adapter(request, create_user_composer())
        return make_response(jsonify(response), int(response["status"]))