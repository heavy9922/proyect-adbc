import  base64
import os, flask
import sys

from sqlalchemy import or_
from app import app, db 

from app.models.Account import Account
from datetime import datetime

class AccountControlles:

    def get_account_all(self):
        accounts = Account.query.all()
        account = []
        for row in accounts:
            account.append({
                'id': row.id,
                'type_account': row.type_account,
                'id_client': row.id_client,
                'n_card': row.n_card,
                'cvv': row.cvv,
                'date_due': row.date_due,
            })
        return account

    def get_account(self,id):
        accounts = []
        account = Account.query.filter_by(id=id).first()
        if account is not None:
            accounts.append({
                'id': account.id,
                'type_account': account.type_account,
                'id_client': account.id_client,
                'n_card': account.n_card,
                'cvv': account.cvv,
                'date_due': account.date_due,
            })
        else:
            accounts.append({
                    'messages':'no se encontro role',
                })
        return accounts

    def add_account(self,account):
        cvv=  account['cvv'],
        date_due=  acvv=  account['date_due'],
        id_client=  acvv=  account['id_client'],
        n_card=  acvv=  account['n_card'],
        type_account=  acvv=  account['type_account']
        account = Account.query.filter_by(n_card=n_card).first()
        if account is None:
            acco = Account(type_account, id_client, n_card,cvv,date_due)
            db.session.add(acco)
            db.session.commit()
            return 'el account se registrao exitosamente'
        else:
            return 'el account ya se encontro registrado'

    def update_account(self,id,account):
        cvv=  account['cvv'],
        date_due=  acvv=  account['date_due'],
        id_client=  acvv=  account['id_client'],
        n_card=  acvv=  account['n_card'],
        type_account=  acvv=  account['type_account']
        account = Account.query.filter_by(id=id).first()
        if account is not None:
            account_update = Account.query.filter_by(id = id).first()
            print(account_update, 'yolo')
            account_update.cvv = cvv
            account_update.date_due = date_due
            account_update.id_client = id_client
            account_update.n_card = n_card
            account_update.type_account = type_account
            db.session.add(account_update)
            db.session.commit()
            return 'Actualizacion correcta'
        else:
            print('hola')
            return 'No se encontro rol registrado'
    
    def delete_account(self,id):
        account = Account.query.filter_by(id=id).first()
        if account is not None:
            account = Account.query.filter_by(id=id).first()
            db.session.delete(account)
            db.session.commit()
            return 'Eliminado correcta'
        else:
            return 'No se encontro rol registrado'
