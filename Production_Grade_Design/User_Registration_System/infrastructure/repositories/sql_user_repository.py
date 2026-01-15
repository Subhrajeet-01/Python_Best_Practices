from domain.repositories.user_repository import UserRepository
from domain.entities.user import User

class SqlUserRepository(UserRepository):

    def save(self, user: User) -> None:
        print(f"[SQL] User with email {user.email} saved to the database.")
    
    def exists(self, email: str) -> bool:
        # Simulate a database check
        print(f"[SQL] Checking if user with email {email} exists in the database.")
        return False