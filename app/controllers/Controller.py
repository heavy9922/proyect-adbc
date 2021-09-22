import  base64
import os, flask
import sys

from sqlalchemy import or_
from app import app, db 

from app.models import Client
from app.models import Branch
from app.models import Account
from app.models.Rol import Rol
from app.models import Employee

from datetime import datetime

class Controller():
    def get_rol_all(self):
        role = Rol.query.all()
        roles = []
        for row in role:
            roles.append({
                'id':row.id,
                'employee':row.employee,
            })
        return roles
    
    def get_rol(self,id):
        roles = []
        role = Rol.query.filter_by(id=id).first()
        if role is not None:
            roles.append({
                    'id':role.id,
                    'employee':role.employee,
                })
        else:
            roles.append({
                    'messages':'no se encontro role',
                })
        return roles
    
    def add_rol(self,rol):
        employee = rol['employee']
        role = Rol.query.filter_by(employee = employee).first()
        if role is None:
            rol = Rol(employee)
            db.session.add(rol)
            db.session.commit()
            return 'el rol se registrao exitosamente'
        else:
            return 'el rol ya se encontro registrado'
