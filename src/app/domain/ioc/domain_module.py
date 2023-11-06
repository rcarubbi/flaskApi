from injector import Module, Binder
from app.domain.services.users_service import UsersService

class DomainModule(Module):
    def configure(self, binder: Binder):
        binder.bind(UsersService)