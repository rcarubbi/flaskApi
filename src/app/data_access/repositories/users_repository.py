from injector import inject
from sqlalchemy.orm.session import Session 
from app.data_access.DTOs.user_dto import UserDto
from app.domain.abstract_users_repository import AbstractUsersRepository
from app.domain.entities.user import User 

class UsersRepository(AbstractUsersRepository):
    @inject
    def __init__(self, session: Session):
        self.session = session

    def getAll(self):
        users_dto = self.session.query(UserDto).all()
        users = [User(user_dto.user_id, user_dto.name) for user_dto in users_dto]
        return users