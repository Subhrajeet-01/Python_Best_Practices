from application.use_cases.register_user import RegisterUser
from application.dto import RegisterUserRequest
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from infrastructure.repositories.logging_user_repository import LoggingUserRepository
from domain.exceptions import InvalidEmailException, UserAlreadyExistsException


def main():
    base_repo = InMemoryUserRepository()
    repo = LoggingUserRepository(base_repo)
    use_case = RegisterUser(repo)

    try: 
        request1 = RegisterUserRequest("  Test@example.com")
        request2 = RegisterUserRequest("invalid-email")
        user = use_case.execute(request1)  # DTO usage
        print(f"User registered successfully: {user.email}")
        # use_case.execute(request1)  # Duplicate email
        use_case.execute(request2)  # Invalid email

    except UserAlreadyExistsException as e:
        print(e)
    except InvalidEmailException as e:
        print(e)
    # try:
    #     repo = InMemoryUserRepository()
    #     use_case = RegisterUser(repo)
    #     use_case.execute("test@example.com")
    #     use_case.execute("test@example.com")  # Duplicate email
    #     use_case.execute("testexample.com")  # Invalid email
    # except Exception as e:
    #     print(e)

if __name__ == "__main__":
    main()