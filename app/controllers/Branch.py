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