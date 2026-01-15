# This file is testing dependency injection with a fake repository.
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository

class FakeUserRepository():
    def __init__(self) -> None:
        self.users: list[User] = []
    
    def save(self, user: User) -> None:
        self.users.append(user)
    
    def exists(self, email):
        return any(u.email == email for u in self.users)