

from domain.entities.user import User

def test_user_email_lowercase():
    user = User(0, "test@example.com")
    assert user.email == "test@example.com"