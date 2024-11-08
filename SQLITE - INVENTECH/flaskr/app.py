from flaskr import create_app
from flaskr.modelos.modelos import Rol, Empleado, Categoria, Proveedor, Administrador, Inventario, Tipomovimiento, Factura, Venta, Producto
from .modelos import db
from flask_restful import Api
from .vistas.vistas import VistaProveedores

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaProveedores, '/proveedores')