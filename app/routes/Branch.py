from  flask import Flask, jsonify, request
from app import app, db

from app.controllers.Branch import BranchControlles

class BranchRoute:
    @app.route('/branchs')
    def get_branch_all():
        bco = BranchControlles()
        branch = bco.get_branch_all()
        return jsonify({'list':branch})

    @app.route('/branchs/<id>')
    def get_branchs(id):
        bco = BranchControlles()
        branchs = bco.get_branch(id)
        return jsonify({'list':branchs})
    