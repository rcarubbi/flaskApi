from injector import inject
from domain.services.users_service import UsersService
from flask import jsonify

class UsersController:
    @inject
    def __init__(self, service: UsersService):
        self.service = service

    def getAll(self):
        return jsonify(self.service.getAll())