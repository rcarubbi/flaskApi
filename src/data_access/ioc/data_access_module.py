from injector import Module, Binder
from data_access.repositories.users_repository import UsersRepository

class DataAccessModule(Module):
    def configure(self, binder: Binder):
        binder.bind(UsersRepository)