from  flask import Flask, jsonify, request
from app import app, db

from app.controllers.Employee import EmployeeController

class EmployeeRoutes:
    @app.route('/employees')
    def get_employee_all():
        acc = EmployeeController()
        employee = acc.get_employee_all()
        return jsonify(employee)

    @app.route('/employees/<id>')
    def get_employees(id):
        acc = EmployeeController()
        employee = acc.get_employee(id)
        return jsonify(employee)

    @app.route('/employees', methods=['POST'])
    def add_employees():
        new_employee = {
            "address": request.json['address'] ,
            "email": request.json['email'] ,
            "id_branch": request.json['id_branch'] ,
            "id_employee": request.json['id_employee'] ,
            "last_name": request.json['last_name'] ,
            "name": request.json['name'] ,
            "numbre_phone": request.json['numbre_phone'] 
        }
        print (new_employee)
        acc = EmployeeController()
        employees = acc.add_employee(new_employee)
        return employees
    
    @app.route('/employees/<id>', methods=['PUT'])
    def update_employees(id):
        new_employee = {
            "address": request.json['address'] ,
            "email": request.json['email'] ,
            "id_branch": request.json['id_branch'] ,
            "id_employee": request.json['id_employee'] ,
            "last_name": request.json['last_name'] ,
            "name": request.json['name'] ,
            "numbre_phone": request.json['numbre_phone'] 
        }
        print (new_employee)
        acc = EmployeeController()
        employees = acc.update_employee(id,new_employee)
        return employees

    @app.route('/employees/<id>', methods=['DELETE'])
    def delete_employees(id):
        acc = EmployeeController()
        employees = acc.delete_employee(id)
        return employees