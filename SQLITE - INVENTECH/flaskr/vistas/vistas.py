from flask import request
from flask_restful import Resource
from ..modelos import db, Proveedor, ProveedorSchema

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