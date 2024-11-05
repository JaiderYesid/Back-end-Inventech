from flaskr import create_app
from flaskr.modelos.modelos import Rol, Empleado, Categoria, Proveedor, Administrador, Inventario, Tipo_movimiento, Factura, Venta, Producto
from .modelos import db
from flask_restful import Api
from .vistas import VistaProveedor

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()
api = Api(app)
api.add_resource(VistaProveedor, '/proveedores')

#with app.app_context():
#    r = Rol(nombre='Adminitrador')
#    e = Empleado(nombre='Yesid', tipo_documento='CC', numero_documento=123456789, email='yesid@gmail.com', conf_email='yesid@gmail.com', direccion='carrera 45b #25-63', telefono=3104862815, cargo='almacenista')
#    c = Categoria(nombre='Facial', descripcion='Productos faciales')
#    p = Proveedor(nombre='Aloefarma', email='aloefarma@gmail.com', direccion='calle 25 #34-56', telefono=7173585)
#    a = Administrador(nombre='Jaider', email='jaider@gmail.com', contraseña='jr1234', conf_contraseña='jr1234')
#    i = Inventario(fecha='2024-06-23', stock=50)
#    t = Tipo_movimiento(descripcion='Entrada')
#    f = Factura(valor_total=25000, iva=0.19)
#    v = Venta(estado='pagado')
#    pr = Producto(estado='Disponible', cantidad_disponible=42, stock_min=12, stock_max=50, color='azul')