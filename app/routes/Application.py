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
        return jsonify({'list':roles})

    @app.route('/roles/<id>')
    def get_role(id):
        ct = Controller()
        roles = ct.get_rol(id)
        return jsonify({'list':roles})

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

# para las tabla de account 
    @app.route('/accounts')
    def get_account_all():
        acc = AccountControlles()
        account = acc.get_account_all()
        return jsonify({'list':account})
    
    @app.route('/accounts/<id>')
    def get_accounts(id):
        acc = AccountControlles()
        accounts = acc.get_account(id)
        return jsonify({'list':accounts})

    @app.route('/accounts', methods=['POST'])
    def add_accounts():
        new_account = {
            "cvv": request.json['cvv'],
            "date_due": request.json['date_due'],
            "id_client": request.json['id_client'],
            "n_card": request.json['n_card'],
            "type_account": request.json['type_account']
        }
        print (new_account)
        acc = AccountControlles()
        accounts = acc.add_account(new_account)
        return accounts

    @app.route('/accounts/<id>', methods=['PUT'])
    def update_account(id):
        new_account = {
            "cvv": request.json['cvv'],
            "date_due": request.json['date_due'],
            "id_client": request.json['id_client'],
            "n_card": request.json['n_card'],
            "type_account": request.json['type_account']
        }
        acc = AccountControlles()
        accounts = acc.update_account(id,new_account)
        return accounts

    @app.route('/accounts/<id>', methods=['DELETE'])
    def delete_accounts(id):
        acc = AccountControlles()
        accounts = acc.delete_account(id)
        return accounts