from app import app, db
from datetime import datetime

class Client(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    numbre_phone = db.Column(db.Float())
    email = db.Column(db.String())
    id_employee = db.Column(db.Integer,db.ForeignKey('public.employee.id'), nullable=False)
    created_at =  db.Column(db.DateTime, nullable=False)

    def __init__(self,name,last_name,address,numbre_phone,email,id_employee):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.numbre_phone =numbre_phone
        self.email=email
        self.id_employee=id_employee
        self.created_at = datetime.today()
