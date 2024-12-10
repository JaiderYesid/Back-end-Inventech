
from marshmallow import Schema, fields
from flask_sqlalchemy import SQLAlchemy
import enum

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(50))
    
class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(50))
    Tipo_Documento = db.Column(db.String(128))
    Numero_Documento = db.Column(db.Integer)
    Email = db.Column(db.String(128))
    C_Email = db.Column(db.String(128))
    Direccion = db.Column(db.String(128))
    Telefono = db.Column(db.Integer)
    Cargo = db.Column(db.String(50))
    Rol_id = db.Column(db.Integer, db.ForeignKey("rol.id"))
    
class Categoria(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Descripcion = db.Column(db.String(512))

class Proveedor(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Email = db.Column(db.String(128))
    Direccion = db.Column(db.String(128))
    Telefono = db.Column(db.Integer)

class Administrador(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Email = db.Column(db.String(128))
    Contrasena = db.Column(db.String(12))
    Rep_Cotrasena = db.Column(db.String(12))
    Telefono = db.Column(db.Integer)
    
class Inventario(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    Fecha = db.Column(db.Date)
    Stock = db.Column(db.Integer)
    
class Tipo_Movimiento(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    Descripción = db.Column(db.String(512))
    Inventario_Id = db.Column(db.Integer, db.ForeignKey("inventario.id"))

class Factura(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    Fecha = db.Column(db.Date)
    Valor = db.Column(db.Integer)
    Iva = db.Column(db.Integer)
    Inventario_Id = db.Column(db.Integer, db.ForeignKey("inventario.id"))
    
class Venta(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    Estado = db.Column(db.String(512))
    Fecha = db.Column(db.Integer)
    Factura_Id = db.Column(db.Integer, db.ForeignKey("factura.id"))

class Producto(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Estado = db.Column(db.String(512))
    Cantidad_Disponible = db.Column(db.Integer)
    Stock_min = db.Column(db.Integer)
    Stock_max = db.Column(db.Integer)
    Color = db.Column(db.String(50))
    Vencimiento = db.Column(db.Date)
    Proveedor_Id = db.Column(db.Integer, db.ForeignKey("proveedor.id"))
    Categoria_Id = db.Column(db.Integer, db.ForeignKey("categoria.id"))
    Invetario_Id = db.Column(db.Integer, db.ForeignKey("inventario.id"))
    Venta_Id = db.Column(db.Integer, db.ForeignKey("venta.id"))

##Serialización

class RolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Rol
        include_relationships = True
        load_instance = True

class EmpleadoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Empleado
        include_relationships = True
        load_instance = True

class CategoriaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
        include_relationships = True
        load_instance = True

class ProveedorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Proveedor
        include_relationships = True
        load_instance = True

class AdministradorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Administrador
        include_relationships = True
        load_instance = True

class InventarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Inventario
        include_relationships = True
        load_instance = True

class Tipo_MovimientoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tipo_Movimiento
        include_relationships = True
        load_instance = True

class FacturaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Factura
        include_relationships = True
        load_instance = True

class VentaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Venta
        include_relationships = True
        load_instance = True

class ProductoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        include_relationships = True
        load_instance = True