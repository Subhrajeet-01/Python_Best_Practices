from infrastructure.logging_config import setup_logging
setup_logging()

from container.di_container import DIContainer
from domain.repositories.user_repository import UserRepository  
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from infrastructure.repositories.logging_user_repository import LoggingUserRepository
from application.use_cases.register_user import RegisterUser
from application.dto import RegisterUserRequest
from domain.exceptions import UserAlreadyExistsException

container = DIContainer()

container.register(
    UserRepository, 
    lambda: LoggingUserRepository(InMemoryUserRepository())
)

container.register(RegisterUser, lambda: RegisterUser(container.resolve(UserRepository)))

use_case = container.resolve(RegisterUser)  

try: 
    user = use_case.execute(RegisterUserRequest("Test@example.com"))
    print(user.email)  # Output:

except UserAlreadyExistsException as e:
    print(f"Error: {e}")