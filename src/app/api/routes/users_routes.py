from flask import Blueprint
from injector import inject
from app.api.controllers.users_controller import UsersController

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods=['GET'])
@inject
def getAll(controller: UsersController):
    return controller.getAll() 
