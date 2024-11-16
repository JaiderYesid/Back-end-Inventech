from flaskr import create_app
from flaskr.modelos.modelos import db, Rol, Empleado, Categoria, Proveedor, Administrador, Inventario, TipoMovimiento, Factura, Venta, Producto
from .modelos import db
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

USER_DB = "root"
PASS_DB = ""  
URL_DB = "localhost"
NAME_DB = "tablasempresa"
FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate()
migrate.init_app(app, db)

class Rol(db.Model):
    _tablename_ = 'rol'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Empleado(db.Model):
    _tablename_ = 'empleado'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    rol = db.relationship('Rol', backref=db.backref('empleados', lazy=True))

class Categoria(db.Model):
    _tablename_ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Proveedor(db.Model):
    _tablename_ = 'proveedor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200))

class Administrador(db.Model):
    _tablename_ = 'administrador'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Inventario(db.Model):
    _tablename_ = 'inventario'
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

class TipoMovimiento(db.Model):
    _tablename_ = 'tipo_movimiento'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)
    inventario = db.relationship('Inventario', backref=db.backref('tipo_movimiento', lazy=True))

class Factura(db.Model):
    _tablename_ = 'factura'
    id = db.Column(db.Integer, primary_key=True)
    fecha_emision = db.Column(db.Date, nullable=False)
    total = db.Column(db.Float, nullable=False)
    venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'), nullable=False)
    venta = db.relationship('Venta', backref=db.backref('facturas', lazy=True))

class Venta(db.Model):
    _tablename_ = 'venta'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    total = db.Column(db.Float, nullable=False)
    factura = db.relationship('Factura', backref=db.backref('venta', lazy=True))    

class Producto(db.Model):
    _tablename_ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    categoria = db.relationship('Categoria', backref=db.backref('productos', lazy=True))

class RolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Rol
        include_relationships = False
        load_instance = True

class Empleadochema(SQLAlchemyAutoSchema):
    class Meta:
        model = Empleado
        include_relationships = True
        load_instance = True

class Categoriaschema(SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
        include_relationships = False
        load_instance = True

class Proveedorchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Proveedor
        include_relationships = False
        load_instance = True

class Administradorchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Administrador
        include_relationships = False
        load_instance = True

class inventariochema(SQLAlchemyAutoSchema):
    class Meta:
        model = Inventario
        include_relationships = False
        load_instance = True
    
class TipoMovimientochema(SQLAlchemyAutoSchema):
    class Meta:
        model = TipoMovimiento
        include_relationships = True  
        load_instance = True        

class Facturachema(SQLAlchemyAutoSchema):
    class Meta:
        model = Factura
        include_relationships = True
        load_instance = True

class Ventachema(SQLAlchemyAutoSchema):
    class Meta:
        model = Venta
        include_relationships = True
        load_instance = True

class Productochema(SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        include_relationships = True
        load_instance = True
