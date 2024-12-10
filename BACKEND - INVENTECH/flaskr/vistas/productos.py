from flask import request
from flask_restful import Resource
from ..modelos import db, Producto, ProductoSchema

#PRODUCTOS

producto_schema = ProductoSchema()

class VistaProductos(Resource):
    def get(self):
        return [producto_schema.dump(Producto) for Producto in Producto.query.all()]
    
    def post(self):
        nuevo_producto = Producto(nombre=request.json['nombre'],
                                  estado=request.json['estado'],
                                  cantidad_disponible=request.json['cantidad_disponible'],
                                  stock_min=request.json['stock_min'],
                                  stock_max=request.json['stock_max'],
                                  color=request.json['color'],
                                  fecha_caducidad=request.json['fecha_caducidad'],
                                  proveedor=request.json['proveedor'],
                                  categoria=request.json['categoria'],
                                  inventario=request.json['inventario'],
                                  venta=request.json['venta'])
        db.session.add(nuevo_producto)
        db.session.commit()
        return producto_schema.dump(nuevo_producto)
    
    def put(self, id):
        producto = Producto.query.get_or_404(id)
        producto.nombre = request.json.get('nombre', producto.nombre)
        producto.estado = request.json.get('estado', producto.estado)
        producto.cantidad_disponible = request.json.get('cantidad_disponible', producto.cantidad_disponible)
        producto.stock_min = request.json.get('stock_min', producto.stock_min)
        producto.stock_max = request.json.get('stock_max', producto.stock_max)
        producto.color = request.json.get('color', producto.color)
        producto.fecha_caducidad = request.json.get('fecha_caducidad', producto.facha_caducidad)
        producto.proveedor = request.json.get('proveedor', producto.proveedor)
        producto.categoria = request.json.get('categoria', producto.categoria)
        producto.inventario = request.json.get('inventario', producto.inventario)
        producto.venta = request.json.get('venta', producto.venta)
        db.session.commit()
        return producto_schema.dump(producto)
    
    def delete(self, id):
        producto = Producto.query.get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return '', 204