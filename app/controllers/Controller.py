import  base64
import os, flask
import sys

from sqlalchemy import or_
from app import app, db 

from app.models import Client
from app.models import Branch

from datetime import datetime

class Controller():
    
    def saludo(self):
        return 'hola que hace'