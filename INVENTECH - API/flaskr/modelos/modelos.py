from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import enum

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    tipo_documento = db.Column(db.String(50))
    numero_documento = db.Column(db.String(50))
    email = db.Column(db.String(50))
    contrasena_hash = db.Column(db.String(250))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    cargo = db.Column(db.String(50))
    rol = db.Column(db.Integer, db.ForeignKey("rol.id"))
    
    @property
    def contrasena(self):
        raise AttributeError("La contraseña no es un atributo legible")
    
    @contrasena.setter
    def contrasena(self, password):
        self.contrasena_hash= generate_password_hash(password)
        
    def verificar_contrasena(self, password):
        return check_password_hash(self.contrasena_hash, password)
    
class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(50))
    
class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    
class Administrador(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(50))
    contrasena_hash = db.Column(db.String(255))
    telefono = db.Column(db.String(50))
    
    @property
    def contrasena(self):
        raise AttributeError("La contraseña no es un atributo legible")
    
    @contrasena.setter
    def contrasena(self, password):
        self.contrasena_hash= generate_password_hash(password)
        
    def verificar_contrasena(self, password):
        return check_password_hash(self.contrasena_hash, password)
    
class Inventario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(50))
    stock = db.Column(db.Integer)
    
class Tipomovimiento(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(50))
    inventario = db.Column(db.Integer, db.ForeignKey("inventario.id"))
    
class Factura(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(50))
    valor_total = db.Column(db.Integer)
    iva = db.Column(db.Integer)
    inventario = db.Column(db.Integer)
    
class Venta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(50))
    fecha = db.Column(db.String(50))
    factura = db.Column(db.Integer, db.ForeignKey("factura.id"))
    
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(50))
    cantidad_disponible = db.Column(db.Integer)
    stock_min = db.Column(db.Integer)
    stock_max = db.Column(db.Integer)
    color = db.Column(db.String(50))
    facha_caducidad = db.Column(db.String(50))
    proveedor = db.Column(db.Integer, db.ForeignKey("proveedor.id"))
    categoria = db.Column(db.Integer, db.ForeignKey("categoria.id"))
    inventario = db.Column(db.Integer, db.ForeignKey("inventario.id"))
    venta = db.Column(db.Integer, db.ForeignKey("venta.id"))
    

#SERIALIZACION

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
    
class TipomovimientoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tipomovimiento
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