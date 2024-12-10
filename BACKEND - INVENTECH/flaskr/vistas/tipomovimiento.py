from flask import request
from flask_restful import Resource
from ..modelos import db, Tipomovimiento, TipomovimientoSchema

#TIPOS DE MOVIMIENTOS

movimiento_schema = TipomovimientoSchema()

class VistaMovimientos(Resource):
    def get(self):
        return [movimiento_schema.dump(Tipomovimiento) for Tipomovimiento in Tipomovimiento.query.all()]
    
    def post(self):
        nuevo_tipomovimiento = Tipomovimiento(descripcion=request.json['descripcion'],
                                              inventario=request.json['inventario'])
        db.session.add(nuevo_tipomovimiento)
        db.session.commit()
        return movimiento_schema.dump(nuevo_tipomovimiento)
    
    def put(self, id):
        movimiento = Tipomovimiento.query.get_or_404(id)
        movimiento.descripcion = request.json.get('descripcion', movimiento.descripcion)
        movimiento.inventario = request.json.get('inventario', movimiento.inventario)
        db.session.commit()
        return movimiento_schema.dump(movimiento)
    
    def delete(self, id):
        movimiento = Tipomovimiento.query.get_or_404(id)
        db.session.delete(movimiento)
        db.session.commit()
        return '', 204