from  flask import Flask, jsonify, request
from app import app, db

from app.controllers.Clients import ClientsController

class ClientsRoute:
    @app.route('/clients')
    def get_client_all():
        acc = ClientsController()
        client = acc.get_client_all()
        return jsonify(client)
    
    @app.route('/clients/<id>')
    def get_clients(id):
        acc = ClientsController()
        clients = acc.get_client(id)
        return jsonify(clients)
    
    @app.route('/clients', methods=['POST'])
    def add_clients():
        new_client = {
            'name': request.json['name'],
            'last_name': request.json['last_name'] ,
            'address': request.json['address'] ,
            'number_phone': request.json['number_phone'] ,
            'email': request.json['email'] ,
            'id_employee': request.json['id_employee']
        }
        print (new_client, 'XDD')
        acc = ClientsController()
        clients = acc.add_client(new_client)
        return clients

    @app.route('/clients/<id>', methods=['PUT'])
    def update_client(id):
        new_client = {
            'name': request.json['name'],
            'last_name': request.json['last_name'] ,
            'address': request.json['address'] ,
            'number_phone': request.json['number_phone'] ,
            'email': request.json['email'] ,
            'id_employee': request.json['id_employee']
        }
        acc = ClientsController()
        clients = acc.update_client(id,new_client)
        return clients

    @app.route('/clients/<id>', methods=['DELETE'])
    def delete_clients(id):
        acc = ClientsController()
        clients = acc.delete_client(id)
        return clients