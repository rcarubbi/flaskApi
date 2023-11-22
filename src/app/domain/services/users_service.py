from injector import inject
from app.domain.abstract_users_repository import AbstractUsersRepository
from app.domain.entities.user import User

class UsersService:
    @inject
    def __init__(self, repository: AbstractUsersRepository):
        self.repository = repository

    def getAll(self):
        users_dto = self.repository.getAll()
        users = [User(user_dto.user_id, user_dto.name) for user_dto in users_dto]
        return users
