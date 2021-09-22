from  flask import Flask, jsonify, request
from app import app, db
from app.controllers.Controller import Controller

class Application:
    @app.route('/')
    def index():
        return 'Api back'

    @app.route('/roles')
    def get_roles_all():
        ct = Controller()
        roles = ct.saludo()
        return jsonify({'list':roles})