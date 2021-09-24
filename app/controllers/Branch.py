import  base64
import os, flask
import sys

from sqlalchemy import or_
from app import app, db 

from app.models.Branch import Branch
from datetime import datetime

class BranchControlles:
    def get_branch_all(self):
        branchs = Branch.query.all()
        branch = []
        for row in branchs:
            branch.append({
                'id': row.id,
                'name_branch' : row.name_branch,
                'address_branch' : row.address_branch,
                'phone':row.phone
            })
        return branch

    def get_branch(self,id):
        branchs = []
        branch = Branch.query.filter_by(id=id).first()
        if branch is not None:
            branchs.append({
                'id': branch.id,
                'name_branch' : branch.name_branch,
                'address_branch' : branch.address_branch,
                'phone':branch.phone
            })
        else:
            branchs.append({
                    'messages':'no se encontro sucursal',
                })
        return branchs

    def add_branch(self,branch):
        name_branch = branch['name_branch']
        address_branch = branch['address_branch']
        phone=branch['phone']
        branch = Branch.query.filter_by(name_branch=name_branch).first()
        if branch is None:
            acco = Branch(name_branch, address_branch, phone)
            db.session.add(acco)
            db.session.commit()
            return 'el branch se registrao exitosamente'
        else:
            return 'el branch ya se encontro registrado'

    def update_branch(self,id,branch):
        name_branch = branch['name_branch']
        address_branch = branch['address_branch']
        phone=branch['phone']
        branch = Branch.query.filter_by(id=id).first()
        if branch is not None:
            branch_update = Branch.query.filter_by(id = id).first()
            print(branch_update, 'yolo')
            branch_update.name_branch = name_branch
            branch_update.address_branch = address_branch
            branch_update.phone = phone
            db.session.add(branch_update)
            db.session.commit()
            return 'Actualizacion correcta'
        else:
            print('hola')
            return 'No se encontro rol registrado'

    def delete_branch(self,id):
        branch = Branch.query.filter_by(id=id).first()
        if branch is not None:
            branch = Branch.query.filter_by(id=id).first()
            db.session.delete(branch)
            db.session.commit()
            return 'Eliminado correcta'
        else:
            return 'No se encontro rol registrado'