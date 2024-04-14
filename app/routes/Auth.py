from flask import jsonify, request
from app.controllers.Auth import AuthController
from app import app
from app.dtos.auth import AuthLoginDTO, AuthRegisterDTO


class AuthRoute:
    @app.route('/register', methods=['POST'])
    def register():
        try:
            user = AuthRegisterDTO(**request.json)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        auth = AuthController()
        user: AuthRegisterDTO = {
            "email": request.json['email'],
            "password": request.json['password'],
            "name": request.json['name'],
            "lastname": request.json['lastname'],
            "document": request.json['document'],
        }
        register = auth.register(user)
        if "err" in register:
            return jsonify(register), register["code"]
        return jsonify(register)

    @app.route("/login", methods=["POST"])
    def login():
        try:
            user = AuthLoginDTO(**request.json)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        user: AuthLoginDTO = {
            "email": request.json['email'],
            "password": request.json['password'],
        }
        auth = AuthController()
        token = auth.login(user)
        return jsonify(token)

        
        