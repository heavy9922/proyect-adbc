from  flask import Flask, jsonify, request
from app import app, db
from app.controllers.Controller import Controller

class Application:
    @app.route('/')
    def index():
        return 'Api back'

    @app.route('/clients')
    def get_clients():
        ct = Controller()
        return ct.saludo()