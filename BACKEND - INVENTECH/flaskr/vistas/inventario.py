from flask import request
from flask_restful import Resource
from ..modelos import db, Inventario, InventarioSchema

#INVENTARIO

inventario_schema = InventarioSchema()

class VistaInventario(Resource):
    def get(self):
        return [inventario_schema.dump(Inventario) for Inventario in Inventario.query.all()]
    
    def post(self):
        nuevo_inventario = Inventario(fecha=request.json['fecha'],
                                      stock=request.json['stock'])
        db.session.add(nuevo_inventario)
        db.session.commit()
        return inventario_schema.dump(nuevo_inventario)
    
    def put(self, id):
        inventario = Inventario.query.get_or_404(id)
        inventario.fecha = request.json.get('fecha', inventario.fecha)
        inventario.stock = request.json.get('stock', inventario.stock)
        db.session.commit()
        return inventario_schema.dump(inventario)
    
    def delete(self, id):
        inventario = Inventario.query.get_or_404(id)
        db.session.delete(inventario)
        db.session.commit()
        return '', 204