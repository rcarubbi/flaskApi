from injector import inject
from data_access.repositories.users_repository import UsersRepository
from domain.entities.user import User

class UsersService:
    @inject
    def __init__(self, repository: UsersRepository):
        self.repository = repository

    def getAll(self):
        users_dto = self.repository.getAll()
        users = [User(user_dto.user_id, user_dto.name) for user_dto in users_dto]
        return users
