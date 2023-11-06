from flask import Flask
from flask_injector import FlaskInjector

from injector import Injector

from app.api.ioc.api_module import ApiModule
from app.api.routes.users_routes import users_blueprint

from app.domain.ioc.domain_module import DomainModule
from app.data_access.ioc.data_access_module import DataAccessModule
from app.data_access.ioc.sql_module import SqlModule

def create_app():
    app = Flask(__name__)
    app.json.ensure_ascii = False
    app.register_blueprint(users_blueprint, url_prefix='/api/v1')
    
    injector = Injector(modules=[ApiModule(), DomainModule(), DataAccessModule(), SqlModule()])

    FlaskInjector(app=app, injector=injector)

    return app