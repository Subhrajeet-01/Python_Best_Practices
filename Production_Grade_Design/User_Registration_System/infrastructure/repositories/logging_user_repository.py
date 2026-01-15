from domain.repositories.user_repository import UserRepository
from domain.entities.user import User

class LoggingUserRepository(UserRepository):
    def __init__(self, wrapped: UserRepository) -> None:
        self._wapped = wrapped

    def save(self, user: User) -> None:
        print(f"[LOG] Saving user with email: {user.email}")
        self._wapped.save(user)
        print(f"[LOG] User with email {user.email} saved successfully.")
    
    def exists(self, email: str) -> bool:
        print(f"[LOG] Checking existence of user with email: {email}")
        return self._wapped.exists(email)