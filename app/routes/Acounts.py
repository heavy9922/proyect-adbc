from  flask import Flask, jsonify, request
from app import app, db

from app.controllers.Account import AccountControlles

class AccountRoute:
    @app.route('/accounts')
    def get_account_all():
        acc = AccountControlles()
        account = acc.get_account_all()
        return jsonify(account)
    
    @app.route('/accounts/<id>')
    def get_accounts(id):
        acc = AccountControlles()
        accounts = acc.get_account(id)
        return jsonify(accounts)

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