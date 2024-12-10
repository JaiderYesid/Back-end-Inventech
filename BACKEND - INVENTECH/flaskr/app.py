from flaskr import create_app
from flaskr.modelos.modelos import Rol, Empleado, Categoria, Proveedor, Administrador, Inventario, Tipomovimiento, Factura, Venta, Producto
from .modelos import db
from flask_restful import Api
from flask_migrate import Migrate
from .vistas.proveedor import VistaProveedores
from .vistas.roles import VistaRoles
from .vistas.empleados import VistaEmpleados
from .vistas.categoria import VistaCategorias
from .vistas.administrador import VistaAdministrador
from .vistas.inventario import VistaInventario
from .vistas.tipomovimiento import VistaMovimientos
from .vistas.factura import VistaFacturas
from .vistas.venta import VistaVentas
from .vistas.productos import VistaProductos
from .vistas.login import Login_emp

from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

CORS(app)

api = Api(app)
api.add_resource(VistaProveedores, '/proveedores')
api.add_resource(VistaRoles, '/roles')
api.add_resource(VistaEmpleados, '/empleados')
api.add_resource(VistaCategorias, '/categorias')
api.add_resource(VistaAdministrador, '/admin')
api.add_resource(VistaInventario, '/inventario')
api.add_resource(VistaMovimientos, '/tipomov')
api.add_resource(VistaFacturas, '/facturas')
api.add_resource(VistaVentas, '/ventas')
api.add_resource(Login_emp, '/loginemp')
api.add_resource(VistaProductos, '/productos')

jwt = JWTManager(app)

migrate = Migrate()
migrate.init_app(app, db)
