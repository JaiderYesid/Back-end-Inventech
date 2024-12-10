from flask_restful import Resource
from flask import request
from Flaskr.modelos.modelos import db, Categoria, CategoriaSchema

categoria_Schema = CategoriaSchema() 

class VistaCategoria(Resource): 
    def get(self): 
        return [categoria_Schema.dump(Categoria) for Categoria in Categoria.query.all()] 
    
    def post(self): 
        nueva_categoria= Categoria(Nombre = request.json['Nombre'],
                                    Descripcion = request.json['Descripcion'], 
                                    ) 
        db.session.add(nueva_categoria) 
        db.session.commit() 
        return categoria_Schema.dump(nueva_categoria), 201 
    
    def put(self, id_Categoria): 
        categoria = Categoria.query.get_or_404(id_Categoria) 
        categoria.Nombre = request.json.get('Nombre', categoria.Nombre) 
        categoria.Descripcion = request.json.get('Descripcion', categoria.Descripcion)  
        
        db.session.commit()
        return categoria_Schema.dump(categoria) 
    
    def delete(self, id_Categoria):
        categoria= Categoria.query.get_or_404(id_Categoria) 
        db.session.delete(categoria) 
        db.session.commit() 
        return 'Se elimino la categoria existosamente ',204