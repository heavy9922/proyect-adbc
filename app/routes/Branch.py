from  flask import Flask, jsonify, request
from app import app, db

from app.controllers.Branch import BranchControlles

class BranchRoute:
    @app.route('/branchs')
    def get_branch_all():
        bco = BranchControlles()
        branch = bco.get_branch_all()
        return jsonify(branch)

    @app.route('/branchs/<id>')
    def get_branchs(id):
        bco = BranchControlles()
        branchs = bco.get_branch(id)
        return jsonify(branchs)
    
    @app.route('/branchs', methods=['POST'])
    def add_branchs():
        new_branch = {
            'name_branch' : request.json['name_branch'],
            'address_branch' : request.json['address_branch'],
            'phone':request.json['phone']
        }
        print (new_branch)
        acc = BranchControlles()
        branchs = acc.add_branch(new_branch)
        return branchs