import unittest

from application.use_cases.register_user import RegisterUser
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from application.dto import RegisterUserRequest
from domain.exceptions import UserAlreadyExistsException, InvalidEmailException

class TestRegisterUser(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryUserRepository()
        self.use_case = RegisterUser(self.repo)

    def test_register_user_success(self):
        request = RegisterUserRequest("test@example.com")
        user = self.use_case.execute(request)

        self.assertEqual(user.email, "test@example.com")

    def test_duplicate_user(self):
        request = RegisterUserRequest("test@example.com")
        self.use_case.execute(request)

        with self.assertRaises(UserAlreadyExistsException):
            self.use_case.execute(request)

    def test_invalid_email(self):
        request = RegisterUserRequest("invalid")

        with self.assertRaises(InvalidEmailException):
            self.use_case.execute(request)

if __name__ == "__main__":
    unittest.main()
