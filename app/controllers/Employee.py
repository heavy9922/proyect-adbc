import  base64
import os, flask
import sys

from sqlalchemy import or_
from app import app, db 

from app.models.Employee import Employee
from datetime import datetime

class EmployeeController:
    def get_employee_all(self):
        employee = []
        employees = Employee.query.all()
        for row in employees:
            employee.append({
                "id":row.id,
                'name': row.name,
                'last_name': row.last_name,
                'address': row.address,
                'numbre_phone':row.numbre_phone,
                'email':row.email,
                'id_branch': row.id_branch,
                'id_employee': row.id_employee,
            })
        return employee

    def get_employee(self,id):
        employees = []
        employee = Employee.query.filter_by(id=id).first()
        if employee is not None:
            employees.append({
                "id":employee.id,
                'name': employee.name,
                'last_name': employee.last_name,
                'address': employee.address,
                'numbre_phone':employee.numbre_phone,
                'email':employee.email,
                'id_branch': employee.id_branch,
                'id_employee': employee.id_employee,
            })
        else:
            employees.append({
                    'messages':'no se encontro role',
                })
        return employees

    def add_employee(self,employee):
        address= employee['address'] 
        email= employee['email'] 
        id_branch= employee['id_branch'] 
        id_employee= employee['id_employee'] 
        last_name= employee['last_name'] 
        name= employee['name'] 
        numbre_phone= employee['numbre_phone']
        employee = Employee.query.filter_by(email=email).first()
        if employee is None:
            acco = Employee(name,last_name,address,numbre_phone,email,id_branch,id_employee)
            db.session.add(acco)
            db.session.commit()
            return 'el employee se registrao exitosamente'
        else:
            return 'el employee ya se encontro registrado'

    def update_employee(self,id,employee):
        address= employee['address'] 
        email= employee['email'] 
        id_branch= employee['id_branch'] 
        id_employee= employee['id_employee'] 
        last_name= employee['last_name'] 
        name= employee['name'] 
        numbre_phone= employee['numbre_phone']
        employee = Employee.query.filter_by(id=id).first()
        if employee is not None:
            employee_update = Employee.query.filter_by(id = id).first()
            employee_update.address = address
            employee_update.email = email
            employee_update.id_branch = id_branch
            employee_update.id_employee = id_employee
            employee_update.last_name = last_name
            employee_update.name = name
            employee_update.numbre_phone = numbre_phone
            db.session.add(employee_update)
            db.session.commit()
            return 'Actualizacion correcta'
        else:
            print('hola')
            return 'No se encontro rol registrado'
    
    def delete_employee(self,id):
        employee = Employee.query.filter_by(id=id).first()
        if employee is not None:
            employee = Employee.query.filter_by(id=id).first()
            db.session.delete(employee)
            db.session.commit()
            return 'Eliminado correcta'
        else:
            return 'No se encontro rol registrado'