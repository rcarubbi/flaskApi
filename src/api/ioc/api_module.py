from injector import Module, Binder
from api.controllers.users_controller import UsersController

class ApiModule(Module):
    def configure(self, binder: Binder):
        binder.bind(UsersController)