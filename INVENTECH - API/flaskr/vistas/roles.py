from flask import request
from flask_restful import Resource
from ..modelos import db, Rol, RolSchema

#ROLES

rol_schema = RolSchema()

class VistaRoles(Resource):
    def get(self):
        return [rol_schema.dump(Rol) for Rol in Rol.query.all()]
    
    def post(self):
        nuevo_rol = Rol(nombre=request.json['nombre'])
        db.session.add(nuevo_rol)
        db.session.commit()
        return rol_schema.dump(nuevo_rol)
    
    def put(self, id):
        rol = Rol.query.get_or_404(id)
        rol.nombre = request.json.get('nombre', rol.nombre)
        db.session.commit()
        return rol_schema.dump(rol)
    
    def delete(self, id):
        rol = Rol.query.get_or_404(id)
        db.session.delete(rol)
        db.session.commit()
        return '', 204