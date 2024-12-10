from flask import request
from flask_restful import Resource
from ..modelos import db, Empleado, EmpleadoSchema
from flask_jwt_extended import jwt_required, create_access_token
import cloudinary

#EMPLEADOS

empleado_schema = EmpleadoSchema()

class VistaEmpleados(Resource):
    def get(self):
        return [empleado_schema.dump(Empleado) for Empleado in Empleado.query.all()]
    
    def post(self):
        imagen_emp = None
        if 'imagen_emp' in request.files:
            archivo_imagen = request.files['imagen_emp']
            if archivo_imagen:
                try:
                    result = cloudinary.uploader.upload(archivo_imagen)
                    imagen_emp = result['secure_url']
                except Exception as e:
                    return {'error': 'Error al subir la imagen a Cloudinary', 'details': str(e)}, 400
        
        nuevo_empleado = Empleado(nombre=request.form['nombre'],
                                  tipo_documento=request.form['tipo_documento'],
                                  numero_documento=request.form['numero_documento'],
                                  email=request.form['email'],
                                  direccion=request.form['direccion'],
                                  telefono=request.form['telefono'],
                                  cargo=request.form['cargo'],
                                  rol=request.form['rol'],
                                  imagen_emp=imagen_emp)
        nuevo_empleado.contrasena_hash = request.form["contrasena"]
        token_de_acceso = create_access_token(identity=request.form['nombre'])
        db.session.add(nuevo_empleado)
        db.session.commit()
        return {'mensaje': 'Empleado creado exitosamente', 'token_de_acceso': token_de_acceso}
    
    def put(self, id):
        empleado = Empleado.query.get_or_404(id)
        empleado.nombre = request.json.get('nombre', empleado.nombre)
        empleado.tipo_documento = request.json.get('tipo_documento', empleado.tipo_documento)
        empleado.numero_documento = request.json.get('numero_documento', empleado.numero_documento)
        empleado.email = request.json.get('email', empleado.email)
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