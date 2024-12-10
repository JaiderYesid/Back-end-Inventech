from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import cloudinary
import cloudinary.uploader
import cloudinary.api

def create_app(config_name):
    app = Flask(__name__)
    cloudinary.config(
        cloud_name = 'dz6c95uv6',
        api_key = '827636139563183',
        api_secret = 'pR_UNAWeUsijnZnS_7weISDue0Y'
    )
    
    app.config['SECRET_KEY'] = 'jaider2310'
    app.config['JWT_SECRET_KEY'] = 'jaider2310'
    
    USER_DB = 'root'
    PASS_DB = ''
    URL_DB = 'localhost'
    NAME_DB = 'inventech'
    FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_RUN_PORT'] = 5001
    return app