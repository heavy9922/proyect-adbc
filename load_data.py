from app import db
from app.models import Client
from app.models import Branch
from app.models import Employee
from app.models import Rol
from app.models import Account

if __name__ == '__main__':
    db.create_all()
    db.session.commit()