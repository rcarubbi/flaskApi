from injector import Module, Binder
from data_access.repositories.users_repository import UsersRepository
from data_access.repositories.abstract_users_repository import AbstractUsersRepository 

class DataAccessModule(Module):
    def configure(self, binder: Binder):
        binder.bind(AbstractUsersRepository, to=UsersRepository)