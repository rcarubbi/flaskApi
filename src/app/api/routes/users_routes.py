from flask import Blueprint
from injector import inject
from app.api.controllers.users_controller import UsersController

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods=['GET'])
@inject
def getAll(controller: UsersController):
    """
    Endpoint to get all users

    ---
    tags:
      - users
    responses:
      200:
        description: List of all users
    """
    return controller.getAll() 


@users_blueprint.route('/users/<int:id>', methods=['GET'])
@inject
def getById(controller: UsersController, id):
    """
    Endpoint to get a user by id

    ---
    tags:
      - users
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: user id
    responses:
      200:
        description: A specific user
      404:
        description: user not found
    """
    return controller.getById(id) 