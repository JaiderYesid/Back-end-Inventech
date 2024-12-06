from flask import request
from flask_restful import Resource
from ..modelos import db, Factura, FacturaSchema

#FACTURAS

factura_schema = FacturaSchema()

class VistaFacturas(Resource):
    def get(self):
        return [factura_schema.dump(Factura) for Factura in Factura.query.all()]
    
    def post(self):
        nueva_factura = Factura(fecha=request.json['fecha'],
                                valor_total=request.json['valor_total'],
                                iva=request.json['iva'],
                                inventario=request.json['inventario'])
        db.session.add(nueva_factura)
        db.session.commit()
        return factura_schema.dump(nueva_factura)
    
    def put(self, id):
        factura = Factura.query.get_or_404(id)
        factura.fecha = request.json.get('fecha', factura.fecha)
        factura.valor_total = request.json.get('valor_total', factura.valor_total)
        db.session.commit()
        return factura_schema.dump(factura)
    
    def delete(self, id):
        factura = Factura.query.get_or_404(id)
        db.session.delete(factura)
        db.session.commit()
        return '', 204