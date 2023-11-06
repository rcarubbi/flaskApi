from injector import inject
from sqlalchemy.orm.session import Session 
from data_access.DTOs.user_dto import UserDto

class UsersRepository:
    @inject
    def __init__(self, session: Session):
        self.session = session

    def getAll(self):
        return self.session.query(UserDto).all()