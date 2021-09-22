from  flask import Flask, jsonify, request
from app import app, db
from app.controllers.Controller import Controller

class Application:
    ct = Controller()
    @app.route('/')
    def index():
        return 'Api back'

    @app.route('/roles')
    def get_roles_all():
        roles = self.ct.get_rol_all()
        return jsonify({'list':roles})

    @app.route('/roles/<id>')
    def get_role(id):
        roles = self.ct.get_rol(id)
        return jsonify({'list':roles})

    @app.route('/roles', methods=['POST'])
    def add_roles():
        roles = self.ct.get_rol(id)
        return jsonify({'list':roles})
