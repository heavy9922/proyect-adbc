from app import app, db
from datetime import datetime

class Rol(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'rol'
    id = db.Column(db.Integer, primary_key=True)
    employee = db.Column(db.String(), nullable=False)
    created_at =  db.Column(db.DateTime, nullable=False)

    def __init__(self,employee):
        self.employee = employee
        self.created_at = datetime.today()
