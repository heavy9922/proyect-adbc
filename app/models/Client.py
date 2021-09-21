from app import app, db
from datetime import datetime

class Client(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    id_account = db.Column(db.Integer,db.ForeignKey('public.branch.id'), nullable=False)
    name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    numbre_phone = db.Column(db.Integer())
    email = db.Column(db.String())
    method = db.Column(db.String)
    created_at =  db.Column(db.DateTime, nullable=False)

    def __init__(self,id_account,name,last_name,address,numbre_phone,email,method):
        self.id_account = id_account
        self.name = name
        self.last_name = last_name
        self.address = address
        self.numbre_phone =numbre_phone
        self.email=email
        self.method = method
        self.created_at = datetime.today()
