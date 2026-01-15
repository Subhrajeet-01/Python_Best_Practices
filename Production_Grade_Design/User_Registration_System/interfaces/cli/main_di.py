# This is a CLI interface demonstrating Dependency Injection using a DI container.

from container.di_container import DIContainer
from application.use_cases.register_user import RegisterUser
from application.dto import RegisterUserRequest
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from infrastructure.repositories.fake_user_repository import FakeUserRepository
from domain.repositories.user_repository import UserRepository

container = DIContainer()

# container.register(UserRepository, lambda: InMemoryUserRepository())
container.register(UserRepository, lambda: FakeUserRepository())
container.register(RegisterUser, lambda: RegisterUser(container.resolve(UserRepository)))

use_case = container.resolve(RegisterUser)
email = "Test@example.com"
user = use_case.execute(RegisterUserRequest(email))
print(user.email)  # Output: test@example.com