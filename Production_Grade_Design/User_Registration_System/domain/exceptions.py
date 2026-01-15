
class InvalidEmailException(Exception):
    """Exception raised for invalid email addresses."""
    pass
class UserAlreadyExistsException(Exception):
    """Exception raised when trying to register a user that already exists."""
    pass