from sqlalchemy import Column, Integer, String
from app.data_access.ioc.sql_module import Base

class UserDto(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String)

