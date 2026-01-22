from application.dto import RegisterUserRequest

def test_register_user_success(register_user_use_case):
    request = RegisterUserRequest("TEST@EXAMPLE.COM")
    user = register_user_use_case.execute(request)  
    assert user.email == "test@example.com"