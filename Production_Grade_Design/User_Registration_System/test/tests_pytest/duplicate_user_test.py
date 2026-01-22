import pytest

from application.dto import RegisterUserRequest
from domain.exceptions import UserAlreadyExistsException

def test_duplicate_user(register_user_use_case):
    request = RegisterUserRequest("test@example.com")

    register_user_use_case.execute(request)

    with pytest.raises(UserAlreadyExistsException):
        register_user_use_case.execute(request)