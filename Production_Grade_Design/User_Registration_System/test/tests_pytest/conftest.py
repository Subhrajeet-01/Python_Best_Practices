import pytest

from application.use_cases.register_user import RegisterUser
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository

@pytest.fixture
def user_repository():
    return InMemoryUserRepository()

@pytest.fixture
def register_user_use_case(user_repository):
    return RegisterUser(user_repository)
