from flask import request
from flask_restful import Resource
from ..modelos import db, Venta, VentaSchema

#VENTAS

venta_schema = VentaSchema()

class VistaVentas(Resource):
    def get(self):
        return [venta_schema.dump(Venta) for Venta in Venta.query.all()]
    
    def post(self):
        nueva_venta = Venta(estado=request.json['estado'],
                            fecha=request.json['fecha'],
                            factura=request.json['factura'])
        db.session.add(nueva_venta)
        db.session.commit()
        return venta_schema.dump(nueva_venta)
    
    def put(self, id):
        venta = Venta.query.get_or_404(id)
        venta.estado = request.json.get('estado', venta.estado)
        venta.fecha = request.json.get('fecha', venta.fecha)
        venta.factura = request.json.get('factura', venta.factura)
        db.session.commit()
        return venta_schema.dump(venta)
    
    def delete(self, id):
        venta = Venta.query.get_or_404(id)
        db.session.delete(venta)
        db.session.commit()
        return '', 204