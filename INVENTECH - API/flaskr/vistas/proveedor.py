from flask import request
from flask_restful import Resource
from ..modelos import db, Proveedor, ProveedorSchema

#PROVEEDORES

proveedor_schema = ProveedorSchema()

class VistaProveedores(Resource):
    def get(self):
        return [proveedor_schema.dump(Proveedor) for Proveedor in Proveedor.query.all()]
    
    def post(self):
        nuevo_proveedor = Proveedor(nombre=request.json['nombre'],
                                    email=request.json['email'],
                                    direccion=request.json['direccion'],
                                    telefono=request.json['telefono'])
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return proveedor_schema.dump(nuevo_proveedor)
    
    def put(self, id):
        proveedor = Proveedor.query.get_or_404(id)
        proveedor.nombre = request.json.get('nombre', proveedor.nombre)
        proveedor.email = request.json.get('email', proveedor.email)
        proveedor.direccion = request.json.get('direccion', proveedor.direccion)
        proveedor.telefono = request.json.get('telefono', proveedor.telefono)
        db.session.commit()
        return proveedor_schema.dump(proveedor)
    
    def delete(self, id):
        proveedor = Proveedor.query.get_or_404(id)
        db.session.delete(proveedor)
        db.session.commit()
        return '', 204