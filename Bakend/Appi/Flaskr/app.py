from Flaskr import create_app
from flask_migrate import Migrate
from .modelos.modelos import db
from flask_restful import Api
from .vistas.vista_categoria import VistaCategoria
from .vistas.vista_producto import VistaProducto


app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = (Api(app))

api.add_resource(VistaCategoria, '/Categorias')
api.add_resource(VistaProducto, '/Productos')


migrate = Migrate(app,db)
migrate.init_app(app, db)

