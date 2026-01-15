import unittest

from application.use_cases.register_user import RegisterUser
from application.dto import RegisterUserRequest
from domain.exceptions import InvalidEmailException, UserAlreadyExistsException
from test.fakes.fake_user_repository import FakeUserRepository

class TestRegisterUser(unittest.TestCase):

    def setUp(self) -> None:
        self.repo = FakeUserRepository()
        self.use_case = RegisterUser(self.repo)
    
    def test_register_user_success(self):
        request = RegisterUserRequest("test@example.com")
        user = self.use_case.execute(request)

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(len(self.repo.users), 1)

    def test_duplicate_email_raises_exception(self):
        request = RegisterUserRequest("test@example.com")
        self.use_case.execute(request)

        with self.assertRaises(UserAlreadyExistsException):
            self.use_case.execute(request)
        
    def test_invalid_email_raises_exception(self):
        request = RegisterUserRequest("invalid-email")

        with self.assertRaises(InvalidEmailException):
            self.use_case.execute(request)
    
    def test_nomalize_email(self):
        request = RegisterUserRequest(" Test@example.com")
        user = self.use_case.execute(request)

        self.assertEqual(user.email, "test@example.com")
        
    