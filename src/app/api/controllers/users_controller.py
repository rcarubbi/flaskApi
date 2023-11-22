from injector import inject
from app.domain.services.users_service import UsersService
from flask import jsonify, make_response

class UsersController:
    @inject
    def __init__(self, service: UsersService):
        self.service = service

    def getAll(self):
        return jsonify(self.service.getAll())
    
    def getById(self, id):
        user = self.service.getById(id)
        if user is None:
            response = make_response(f"User not found for id {id}.", 404)
            response.headers['Content-Type'] = 'text/plain'
            return response
        else:
            return jsonify(user)