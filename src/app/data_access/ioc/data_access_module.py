from injector import Module, Binder
from app.data_access.repositories.users_repository import UsersRepository
from app.domain.abstract_users_repository import AbstractUsersRepository 

class DataAccessModule(Module):
    def configure(self, binder: Binder):
        binder.bind(AbstractUsersRepository, to=UsersRepository)