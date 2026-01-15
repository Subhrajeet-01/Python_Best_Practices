import unittest
from unittest.mock import Mock

from application.use_cases.register_user import RegisterUser
from application.dto import RegisterUserRequest
from domain.exceptions import InvalidEmailException

class TestRegisterUserMock(unittest.TestCase):

    def setUp(self):
        self.repository = Mock()
        self.use_case = RegisterUser(self.repository)

    def test_success(self):
        self.repository.exists.return_value = False

        request = RegisterUserRequest("test@example.com")
        user = self.use_case.execute(request)

        self.repository.exists.assert_called_once_with("test@example.com")
        self.repository.save.assert_called_once()
        self.assertEqual(user.email, "test@example.com")

    def test_invalid_email_does_not_touch_repo(self):
        request = RegisterUserRequest("invalid")

        with self.assertRaises(InvalidEmailException):
            self.use_case.execute(request)

        self.repository.exists.assert_not_called()
        self.repository.save.assert_not_called()

    def test_repository_failure(self):
        self.repository.exists.return_value = False
        self.repository.save.side_effect = Exception("DB failure")

        request = RegisterUserRequest("test@example.com")

        with self.assertRaises(Exception):
            self.use_case.execute(request)

