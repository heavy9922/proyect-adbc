from app import app, db
from datetime import datetime

class Branch(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'branch'
    id = db.Column(db.Integer, primary_key=True)
    name_branch = db.Column(db.String(), nullable=False)
    address_branch = db.Column(db.String(), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    created_at =  db.Column(db.DateTime, nullable=False)

    def __init__(self,name_branch,address_branch,phone ):
        self.name_branch = name_branch
        self.address_branch= address_branch
        self.phone = phone
        self.created_at = datetime.today()
