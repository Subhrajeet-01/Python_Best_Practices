# This main file demonstrates dependency injection to switch between InMemory and SQL repositories.

from container.di_container import DIContainer
from application.use_cases.register_user import RegisterUser
from application.dto import RegisterUserRequest

from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from infrastructure.repositories.sql_user_repository import SqlUserRepository

from domain.repositories.user_repository import UserRepository

container = DIContainer()

USE_SQL = True  # Toggle this flag to switch repositories

if USE_SQL:
    container.register(UserRepository, lambda: SqlUserRepository())
else:
    container.register(UserRepository, lambda: InMemoryUserRepository())

container.register(RegisterUser, lambda: RegisterUser(container.resolve(UserRepository)))

use_case = container.resolve(RegisterUser)
email = "TEst@example.com"
use_case = container.resolve(RegisterUser)
user = use_case.execute(RegisterUserRequest(email))

print(user.email)  