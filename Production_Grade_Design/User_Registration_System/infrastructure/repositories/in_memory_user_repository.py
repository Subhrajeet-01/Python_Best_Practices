from domain.entities.user import User
from domain.repositories.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self.users: list[User] = []

    def save(self, user: User) -> None:
        self.users.append(user)
    
    def exists(self, email: str) -> bool:
        return any(u.email == email for u in self.users)


    # def save(self, user: User) -> None:
    #     if self.exists(user.email):
    #         raise UserAlreadyExistsException(f"User with email {user.email} already exists.")
    #     self.users.append(user)
    #     print(f"User with email {user.email} saved in memory repository.")

    # def exists(self, email: str) -> bool:
    #     return any(user.email == email for user in self.users)
        