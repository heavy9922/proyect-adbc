from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:Skills2020@localhost/pythondb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

print(datetime.today())

from app.routes.Rol import Application
from app.routes.Acounts import AccountRoute
from app.routes.Branch import BranchRoute
from app.routes.Employee import EmployeeRoutes
from app.routes.Clients import ClientsRoute