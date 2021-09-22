from app import app, db
from datetime import datetime

class Account(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    type_account = db.Column(db.String(), nullable=False)
    id_client = db.Column(db.Integer,db.ForeignKey('public.client.id'), nullable=False)
    n_card = db.Column(db.Integer(), nullable=False)
    cvv = db.Column(db.Integer(), nullable=False)
    date_due = db.Column(db.Date(), nullable=False)
    created_at =  db.Column(db.DateTime, nullable=False)

    def __init__(self,type_account,id_client,n_card,cvv,date_due):
        self.type_account = type_account
        self.id_client = id_client
        self.n_card = n_card
        self.cvv = cvv
        self.date_due = date_due
        self.created_at = datetime.today()
