import logging
from domain.repositories.user_repository import UserRepository
from domain.entities.user import User

logger = logging.getLogger(__name__)

class LoggingUserRepository(UserRepository):
    def __init__(self, wrapped: UserRepository) -> None:
        self._wapped = wrapped

    def save(self, user: User) -> None:
        logger.info("Saving user with email: %s", user.email)
        self._wapped.save(user)
    
    def exists(self, email: str) -> bool:
        logger.info("Checking existence of user with email: %s", email)
        return self._wapped.exists(email)