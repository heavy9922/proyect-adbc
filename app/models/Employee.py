from app import app, db
from datetime import datetime

class Employee(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    numbre_phone = db.Column(db.Integer())
    email = db.Column(db.String())
    id_branch = db.Column(db.Integer,db.ForeignKey('public.branch.id'), nullable=False)
    id_employee = db.Column(db.Integer,db.ForeignKey('public.rol.id'), nullable=False)
    created_at =  db.Column(db.DateTime, nullable=False)

    def __init__(self,id_account,name,last_name,address,numbre_phone,email,id_branch,id_employee):
        self.id_account = id_account
        self.name = name
        self.last_name = last_name
        self.address = address
        self.numbre_phone =numbre_phone
        self.email=email
        self.id_branch = id_branch
        self.id_employee = id_employee
        self.created_at = datetime.today()
