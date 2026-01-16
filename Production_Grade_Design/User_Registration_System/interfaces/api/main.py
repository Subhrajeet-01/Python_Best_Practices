from fastapi import FastAPI
from container.di_container import DIContainer

from domain.repositories.user_repository import UserRepository
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from application.use_cases.register_user import RegisterUser
from interfaces.api.user_controller import register_routes

container = DIContainer()

container.register(UserRepository, lambda: InMemoryUserRepository())
container.register(RegisterUser, lambda: RegisterUser(container.resolve(UserRepository)))

app = FastAPI()

router = register_routes(container.resolve(RegisterUser))
app.include_router(router)