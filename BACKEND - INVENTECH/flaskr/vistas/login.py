from flask import request
from flask_restful import Resource
from ..modelos import Administrador

class Login_emp(Resource):
    def post(self):
        nombre_emp = request.json["nombre"]
        contrasena_emp = request.json["contrasena"]
        administrador = Administrador.query.filter_by(nombre=nombre_emp).first()
        if administrador and administrador.verificar_contrasena(contrasena_emp):
            return {'mensaje': 'Inicio de sesion exitoso'}, 200
        else:
            return {'mensaje': 'Nombre de usuario o contraseña incorrectos'}, 401      
        
        
class Loginadmin(Resource):
    def post(self):
        nombre_adm = request.json["nombre"]
        contrasena_adm = request.json["contrasena"]
        administrador = Administrador.query.filter_by(nombre=nombre_adm).first()
        if administrador and administrador.verificar_contrasena(contrasena_adm):
            return {'mensaje': 'Inicio de sesion exitoso'}, 200
        else:
            return {'mensaje': 'Nombre de usuario o contraseña incorrectos'}, 401        