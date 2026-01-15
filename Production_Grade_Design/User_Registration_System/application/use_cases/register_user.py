from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from domain.exceptions import InvalidEmailException, UserAlreadyExistsException
from application.dto import RegisterUserRequest

class RegisterUser:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, request: RegisterUserRequest) -> User:

        email = request.email.strip().lower()

        if "@" not in email:
            raise InvalidEmailException("The provided email is invalid.")
        
        if self.repository.exists(email):
            raise UserAlreadyExistsException(f"User with email {email} already exists.")

        user = User(0, email)
        self.repository.save(user)
        return user
    
    # def execute(self, email: str) -> User:
    #     if "@" not in email:
    #         raise InvalidEmailException("The provided email is invalid.")
    #
    #     user = User(0, email)
    #     self.repository.save(user)
    #     print(f"User with email {user.email} registered successfully.")