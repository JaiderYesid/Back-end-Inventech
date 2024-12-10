from flask_restful import Resource
from flask import request
from Flaskr.modelos.modelos import db, Producto, ProductoSchema

producto_Schema = ProductoSchema() 

class VistaProducto(Resource): 
    def get(self): 
        return [producto_Schema.dump(Producto) for Producto in Producto.query.all()] 
    
    def post(self): 
        nuevo_producto= Producto(Estado = request.json['Estado'],
                                Cantidad_Disponible = request.json['Cantidad_Disponible'],
                                Stock_min = request.json['Stock_min'],
                                Stock_max = request.json['Stock_max'],
                                Color = request.json['Color'],
                                Vencimiento = request.json['Vencimiento'],
                                Proveedor_Id = request.json['Proveedor_Id'],
                                Categoria_Id = request.json['Categoria_Id'],
                                Invetario_Id = request.json['Invetario_Id'],
                                Venta_Id = request.json['Venta_Id'],
                                
                                    ) 
        db.session.add(nuevo_producto) 
        db.session.commit() 
        return producto_Schema.dump(nuevo_producto), 201 
    
    def put(self, id_Producto): 
        producto= Producto.query.get_or_404(id_Producto) 
        producto.Estado = request.json.get('Estado', producto.Estado) 
        producto.Cantidad_Disponible = request.json.get('Cantidad_Disponible', producto.Cantidad_Disponible)  
        producto.Stock_min = request.json.get('Stock_min', producto.Stock_min)  
        producto.Stock_max = request.json.get('Stock_max', producto.Stock_max)  
        producto.Color = request.json.get('Color', producto.Color)  
        producto.Vencimiento = request.json.get('Vencimiento', producto.Vencimiento)  
        producto.Proveedor_Id = request.json.get('Proveedor_Id', producto.Proveedor_Id)  
        producto.Categoria_Id = request.json.get('Categoria_Id', producto.Categoria_Id)  
        producto.Invetario_Id = request.json.get('Invetario_Id', producto.Invetario_Id)  
        producto.Venta_Id = request.json.get('Venta_Id', producto.Venta_Id)  
       
        db.session.commit()
        return producto_Schema.dump(producto) 
    
    def delete(self, id_Producto):
        producto= Producto.query.get_or_404(id_Producto)
        db.session.delete(producto) 
        db.session.commit() 
        return 'Se elimino el producto existosamente ',204