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
    def saludo(self):
        role = Rol.query.all()
        roles = []
        for row in role:
            roles.append({
                'id':row.id,
                'employee':row.employee,
            })
        return roles