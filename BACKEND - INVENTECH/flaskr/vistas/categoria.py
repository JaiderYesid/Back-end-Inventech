from flask import request
from flask_restful import Resource
from ..modelos import db, Categoria, CategoriaSchema

#CATEGORIAS

categoria_schema = CategoriaSchema()

class VistaCategorias(Resource):
    def get(self):
        return [categoria_schema.dump(Categoria) for Categoria in Categoria.query.all()]
    
    def post(self):
        nueva_categoria = Categoria(nombre=request.json['nombre'],
                                    descripcion=request.json['descripcion'])
        db.session.add(nueva_categoria)
        db.session.commit()
        return categoria_schema.dump(nueva_categoria)
    
    def put(self, id):
        categoria = Categoria.query.get_or_404(id)
        categoria.nombre = request.json.get('nombre', categoria.nombre)
        categoria.descripcion = request.json.get('descripcion', categoria.descripcion)
        db.session.commit()
        return categoria_schema.dump(categoria)
    
    def delete(self, id):
        categoria = Categoria.query.get_or_404(id)
        db.session.delete(categoria)
        db.session.commit()
        return '', 204