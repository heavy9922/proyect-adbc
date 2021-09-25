from  flask import Flask, jsonify, request
from app import app, db
from app.controllers.Controller import Controller
from app.controllers.Account import AccountControlles

class Application:
    @app.route('/')
    def index():
        return 'Api back'

    @app.route('/roles')
    def get_roles_all():
        ct = Controller()
        roles = ct.get_rol_all()
        return jsonify(roles)

    @app.route('/roles/<id>')
    def get_role(id):
        ct = Controller()
        roles = ct.get_rol(id)
        return jsonify(roles)

    @app.route('/roles', methods=['POST'])
    def add_roles():
        new_rol = {
            'employee': request.json['employee']
        }
        print (new_rol)
        ct = Controller()
        add_rol = ct.add_rol(new_rol)
        return add_rol

    @app.route('/roles/<id>', methods=['PUT'])
    def update_roles(id):
        new_rol = {
            'employee': request.json['employee']
        }
        ct = Controller()
        add_rol = ct.update_rol(id,new_rol)
        return add_rol
    
    @app.route('/roles/<id>', methods=['DELETE'])
    def delete_roles(id):
        ct = Controller()
        delete_rol = ct.delete_rol(id)
        return delete_rol
