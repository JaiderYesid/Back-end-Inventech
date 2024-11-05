from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy 
import enum

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128))

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128))
    tipo_documento = db.Column(db.String(128))
    numero_documento = db.Column(db.Integer)
    email = db.Column(db.String(128))
    conf_email = db.Column(db.String(128))
    direccion = db.Column(db.String(128))
    telefono = db.Column(db.Integer)
    cargo = db.Column(db.String(128))
    rol = db.Column(db.Integer, db.ForeignKey("rol.id"))

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128))
    descripcion = db.Column(db.String(128))

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128))
    email = db.Column(db.String(128))
    direccion = db.Column(db.String(128))
    telefono = db.Column(db.String(128))

class Administrador(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128))
    email = db.Column(db.String(128))
    contraseña = db.Column(db.String(128))
    conf_contraseña = db.Column(db.String(128))
    telefono = db.Column(db.Integer)

class Inventario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.Date)
    stock = db.Column(db.Integer)

class Tipo_movimiento(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(128))
    inventario = db.Column(db.Integer, db.ForeignKey("inventario.id"))

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    valor_total = db.Column(db.Integer)
    iva = db.Column(db.Float)
    inventario = db.Column(db.Integer, db.ForeignKey("inventario.id"))

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(128))
    factura = db.Column(db.Integer, db.ForeignKey("factura.id"))

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(128))
    cantidad_disponible = db.Column(db.Integer)
    stock_min = db.Column(db.Integer)
    stock_max = db.Column(db.Integer)
    color = db.Column(db.String(128))
    proveedor = db.Column(db.Integer, db.ForeignKey("proveedor.id"))
    categoria = db.Column(db.Integer, db.ForeignKey("categoria.id"))
    inventario = db.Column(db.Integer, db.ForeignKey("inventario.id"))
    venta = db.Column(db.Integer, db.ForeignKey("venta.id"))


class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return{"llave": value.name, "valor": value.value}

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
    class Model:
        model = Proveedor
        include_relationships = True
        load_instance = True

class AdministradorSchema(SQLAlchemyAutoSchema):
    class Model:
        model = Administrador
        include_relationships = True
        load_instance = True

class InventarioSchema(SQLAlchemyAutoSchema):
    class Model:
        model = Inventario
        include_relationships = True
        load_instance = True

class Tipo_movimientoSchema(SQLAlchemyAutoSchema):
    class Model:
        model = Tipo_movimiento
        include_relationships = True
        load_instance = True

class FacturaSchema(SQLAlchemyAutoSchema):
    class Model:
        model = Factura
        include_relationships = True
        load_instance = True

class VentaSchema(SQLAlchemyAutoSchema):
    class Model:
        model = Venta
        include_relationships = True
        load_instance = True

class ProductoSchema(SQLAlchemyAutoSchema):
    class Model:
        model = Producto
        include_relationships = True
        load_instance = True