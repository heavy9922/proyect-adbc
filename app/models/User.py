from app import db

class User(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    name =  db.Column(db.String(15),nullable=False)
    lastname =  db.Column(db.String(15),nullable=False)
    document = db.Column(db.Integer,nullable=False)

    
    def __init__(self, email:str, password:str ,name:str, lastname:str, document:float):
        self.email = email
        self.password = password
        self.name = name
        self.lastname = lastname
        self.document = document

