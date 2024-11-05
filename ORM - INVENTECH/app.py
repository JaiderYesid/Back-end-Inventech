from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

USER_DB = 'root'
PASS_DB = ''
URL_DB = 'localhost'
NAME_DB = 'inventech'
FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate()
migrate.init_app(app, db)
#Configuracion de la migracion, Comando:
#    flask db init

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128)) 

    def _init_(self, id):
        self.id = id
        self.nombre = nombre
        
    def json(self):
        return{'id': self.id, 'nombre': self.nombre}
    
    def str(self):
        return str(self._classs) + ": " + str(self.dict_)

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

    def _init_(self, id, nombre, tipo_documento, numero_documento, email, conf_email, direccion, telefono, cargo, rol):
        self.id = id
        self.nombre = nombre
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.email = email
        self.conf_email = conf_email
        self.direccion = direccion
        self.telefono = telefono
        self.cargo = cargo
        self.rol = rol
        
    def json(self):
        return{'id': self.id, 'nombre': self.nombre, 'tipo_documento': self.tipo_documento, 'numero_documento': self.numero_documento, 'email': self.email, 'conf_email': self.conf_email, 'direccion': self.direccion, 'telefono': self.telefono, 'cargo': self.cargo, 'rol': self.rol}
    
    def str(self):
        return str(self._classs) + ": " + str(self.dict_)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128))
    descripcion = db.Column(db.String(128))

    def _init_(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        
    def json(self):
        return{'id': self.id, 'nombre': self.nombre, 'descripcion': self.descripcion}
    
    def str(self):
        return str(self._classs) + ": " + str(self.dict_)

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128))
    email = db.Column(db.String(128))
    direccion = db.Column(db.String(128))
    telefono = db.Column(db.String(128))

    def _init_(self, id, nombre, email, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        
    def json(self):
        return{'id': self.id, 'nombre': self.nombre, 'email': self.email, 'direccion': self.direccion, 'telefono': self.telefono}
    
    def str(self):
        return str(self._classs) + ": " + str(self.dict_)

class Administrador(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128))
    email = db.Column(db.String(128))
    contraseña = db.Column(db.String(128))
    conf_contraseña = db.Column(db.String(128))
    telefono = db.Column(db.Integer)

    def _init_(self, id, nombre, email, contraseña, conf_contraseña, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.conf_contraseña = conf_contraseña
        self.telefono = telefono
        
    def json(self):
        return{'id': self.id, 'nombre': self.nombre, 'email': self.email, 'contraseña': self.contraseña, 'conf_contraseña': self.conf_contraseña, 'telefono': self.telefono}
    
    def str(self):
        return str(self._classs) + ": " + str(self.dict_)

class Inventario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.Date)
    stock = db.Column(db.Integer)

    def _init_(self, id, fecha, stock):
        self.id = id
        self.fecha = fecha
        self.stock = stock
        
    def json(self):
        return{'id': self.id, 'fecha': self.fecha, 'stock': self.stock}
    
    def str(self):
        return str(self._classs) + ": " + str(self.dict_)

class Tipo_movimiento(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(128))
    inventario = db.Column(db.Integer, db.ForeignKey("inventario.id"))

    def _init_(self, id, descripcion, inventario):
        self.id = id
        self.descripcion = descripcion
        self.inventario = inventario
        
    def json(self):
        return{'id': self.id, 'descripcion': self.descripcion, 'inventario': self.inventario}
    
    def str(self):
        return str(self._classs) + ": " + str(self.dict_)

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    valor_total = db.Column(db.Integer)
    iva = db.Column(db.Float)
    inventario = db.Column(db.Integer, db.ForeignKey("inventario.id"))

    def _init_(self, valor_total, iva, inventario):
        self.id = id
        self.valor_total = valor_total
        self.iva = iva
        self.inventario = inventario
        
    def json(self):
        return{'id': self.id, 'valor_total': self.valor_total, 'iva': self.iva, 'inventario': self.inventario}
    
    def str(self):
        return str(self._classs) + ": " + str(self.dict_)

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(128))
    factura = db.Column(db.Integer, db.ForeignKey("factura.id"))

    def _init_(self, id, estado, factura):
        self.id = id
        self.estado = estado
        self.factura = factura
        
    def json(self):
        return{'id': self.id, 'estado': self.estado, 'factura': self. factura}
    
    def str(self):
        return str(self._classs) + ": " + str(self.dict_)

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

    def _init_(self, id, estado, cantidad_disponible, stock_min, stock_max, color, proveedor, categoria, inventario, venta):
        self.id = id
        self.estado = estado
        self.cantidad_disponible = cantidad_disponible
        self.stock_min = stock_min
        self.stock_max = stock_max
        self.color = color
        self.proveedor = proveedor
        self.categoria = categoria
        self.inventario = inventario
        self.venta = venta
        
    def json(self):
        return{'id': self.id, 'estado': self.estado, 'cantidad_disponible': self.cantidad_disponible, 'stock_min': self.stock_min, 'stock_max': self.stock_max, 'color': self.color, 'proveedor': self.proveedor, 'categoria': self.categoria, 'inventario': self.inventario, 'venta': self.venta}
    
    def str(self):
        return str(self._classs) + ": " + str(self.dict_)

    #Mapearlo el modelo person en la bd, comando:
    #flask db migrate