# test/fakes/fake_user_repository.py
# This file Replace Database interactions with an in-memory fake repository for testing purposes.

from domain.repositories.user_repository import UserRepository
from domain.entities.user import User

class FakeUserRepository(UserRepository):
    def __init__(self) -> None:
        self.users: list[User] = []
    
    def save(self, user: User) -> None:
        self.users.append(user)
    
    def exists(self, email):
        return any(u.email == email for u in self.users)