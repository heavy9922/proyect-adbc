from  flask import Flask, jsonify, request
from app import app, db
from app.controllers import Controller

class Application:
    @app.route('/')
    def index():
        return 'hola mundo'

    @app.route('/clients')
    def get_clients():
        return 'welcome to bussines'