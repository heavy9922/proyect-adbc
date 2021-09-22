from  flask import Flask, jsonify, request
from app import app, db
from app.controllers.Controller import Controller

class Application:
    @app.route('/')
    def index():
        return 'Api back'

    @app.route('/roles')
    def get_roles_all():
        ct = Controller()
        roles = ct.get_rol_all()
        return jsonify({'list':roles})

    @app.route('/roles/<id>')
    def get_role(id):
        ct = Controller()
        roles = ct.get_rol(id)
        return jsonify({'list':roles})
