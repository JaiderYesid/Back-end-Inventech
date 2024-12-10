from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '000speed'
    app.config['JWT_SECRET_KEY'] = 'spedd_max00'
    USER_DB = 'root'
    PASS_DB = 'herrera'
    URL_DB = 'localhost'
    NAME_DB = 'appi'
    FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_RUN_PORT'] = 5001
    return app            