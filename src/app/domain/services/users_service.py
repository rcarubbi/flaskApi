from injector import inject
from app.domain.abstract_users_repository import AbstractUsersRepository
from app.domain.entities.user import User

class UsersService:
    @inject
    def __init__(self, repository: AbstractUsersRepository):
        self.repository = repository

    def getAll(self):
        return self.repository.getAll()

        
    def getById(self, id):
        users = self.repository.getAll()
        user = next((user for user in users if user.id == id), None)
        return user
    
       
