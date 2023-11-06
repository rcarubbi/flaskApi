from injector import inject
from sqlalchemy.orm.session import Session 
from app.data_access.DTOs.user_dto import UserDto
from app.data_access.repositories.abstract_users_repository import AbstractUsersRepository

class UsersRepository(AbstractUsersRepository):
    @inject
    def __init__(self, session: Session):
        self.session = session

    def getAll(self):
        return self.session.query(UserDto).all()