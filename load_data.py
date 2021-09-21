from app import db
from app.models import Client
from app.models import Branch

if __name__ == '__main__':
    db.create_all()
    db.session.commit()