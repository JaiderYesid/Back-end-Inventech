from flask import request
from flask_restful import Resource
from ..modelos import db, Administrador, AdministradorSchema
from flask_jwt_extended import jwt_required, create_access_token

#ADMINISRADOR

administrador_schema = AdministradorSchema()

class VistaAdministrador(Resource):
    def get(self):
        return [administrador_schema.dump(Administrador) for Administrador in Administrador.query.all()]
    
    def post(self):
        nuevo_administrador = Administrador(nombre=request.json['nombre'],
                                            email=request.json['email'],
                                            contrasena_hash=request.json['contrasena_hash'],
                                            telefono=request.json['telefono'])
        token_de_acceso = create_access_token(identity=request.json['nombre'])
        db.session.add(nuevo_administrador)
        db.session.commit()
        return {'mensaje': 'Administrador creado exitosamente', 'token_de_acceso': token_de_acceso}
    
    def put(self, id):
        administrador = Administrador.query.get_or_404(id)
        administrador.nombre = request.json.get('nombre', administrador.nombre)
        administrador.email = request.json.get('email', administrador.email)
        administrador.contraseña = request.json.get('contraseña', administrador.contraseña)
        administrador.rep_contraseña = request.json.get('rep_contraseña', administrador.rep_contraseña)
        administrador.telefono = request.json.get('telefono', administrador.telefono)
        db.session.commit()
        return administrador_schema.dump(administrador)
    
    def delete(self, id):
        administrador = Administrador.query.get_or_404(id)
        db.session.delete(administrador)
        db.session.commit()
        return '', 204