import  base64
import os, flask
import sys

from sqlalchemy import or_
from app import app, db 

from app.models.Client import Client
from datetime import datetime

class ClientsController:

    def get_client_all(self):
        clients = Client.query.all()
        client = []
        for row in clients:
            client.append({
                'id': row.id,
                'name': row.name,
                'last_name': row.last_name,
                'address': row.address,
                'number_phone': row.numbre_phone,
                'email': row.email,
                'id_employee': row.id_employee,
            })
        return client

    def get_client(self,id):
        clients = []
        client = Client.query.filter_by(id=id).first()
        if client is not None:
            clients.append({
                'id': client.id,
                'name': client.name,
                'last_name': client.last_name,
                'address': client.address,
                'number_phone': client.numbre_phone,
                'email': client.email,
                'id_employee': client.id_employee,
            })
        else:
            clients.append({
                    'messages':'no se encontro role',
                })
        return clients

    def add_client(self,client):
        name=  client['name']
        last_name= client['last_name']
        address= client['address']
        number_phone= client['number_phone']
        email= client['email']
        id_employee= client['id_employee']
        client = Client.query.filter_by(name=name).first()
        if client is None:
            acco = Client(name, last_name,address, number_phone, email,id_employee)
            db.session.add(acco)
            db.session.commit()
            return 'el client se registrao exitosamente'
        else:
            return 'el client ya se encontro registrado'
    
    def update_client(self,id,client):
        name=  client['name']
        last_name= client['last_name']
        address= client['address']
        number_phone= client['number_phone']
        email= client['email']
        id_employee= client['id_employee']
        client = Client.query.filter_by(id=id).first()
        if client is not None:
            client_update = Client.query.filter_by(id=id).first()
            client_update.name = name
            client_update.last_name = last_name
            client_update.address = address
            client_update.number_phone = number_phone
            client_update.email = email
            client_update.id_employee = id_employee
            db.session.add(client_update)
            db.session.commit()
            return 'Actualizacion correcta'
        else:
            print('hola')
            return 'No se encontro rol registrado'

    def delete_client(self,id):
        client = Client.query.filter_by(id=id).first()
        if client is not None:
            client = Client.query.filter_by(id=id).first()
            db.session.delete(client)
            db.session.commit()
            return 'Eliminado correcta'
        else:
            return 'No se encontro rol registrado'