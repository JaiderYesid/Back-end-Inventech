from flask import request
from flask_restful import Resource
from ..modelos import db, Empleado, EmpleadoSchema
from flask_jwt_extended import jwt_required, create_access_token

#EMPLEADOS

empleado_schema = EmpleadoSchema()

class VistaEmpleados(Resource):
    def get(self):
        return [empleado_schema.dump(Empleado) for Empleado in Empleado.query.all()]
    
    def post(self):
        nuevo_empleado = Empleado(nombre=request.json['nombre'],
                                  tipo_documento=request.json['tipo_documento'],
                                  numero_documento=request.json['numero_documento'],
                                  email=request.json['email'],
                                  contrasena_hash=request.json['contrasena_hash'],
                                  direccion=request.json['direccion'],
                                  telefono=request.json['telefono'],
                                  cargo=request.json['cargo'],
                                  rol=request.json['rol'])
        token_de_acceso = create_access_token(identity=request.json['nombre'])
        db.session.add(nuevo_empleado)
        db.session.commit()
        return {'mensaje': 'Empleado creado exitosamente', 'token_de_acceso': token_de_acceso}
    
    def put(self, id):
        empleado = Empleado.query.get_or_404(id)
        empleado.nombre = request.json.get('nombre', empleado.nombre)
        empleado.tipo_documento = request.json.get('tipo_documento', empleado.tipo_documento)
        empleado.numero_documento = request.json.get('numero_documento', empleado.numero_documento)
        empleado.email = request.json.get('email', empleado.email)
        empleado.conf_email = request.json.get('conf_email', empleado.conf_email)
        empleado.direccion = request.json.get('direccion', empleado.direccion)
        empleado.telefono = request.json.get('telefono', empleado.telefono)
        empleado.cargo = request.json.get('cargo', empleado.cargo)
        empleado.rol = request.json.get('rol', empleado.rol)
        db.session.commit()
        return empleado_schema.dump(empleado)
    
    def delete(self, id):
        empleado = Empleado.query.get_or_404(id)
        db.session.delete(empleado)
        db.session.commit()
        return '', 204