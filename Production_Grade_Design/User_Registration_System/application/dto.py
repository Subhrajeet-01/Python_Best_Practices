# In backend engineering, a DTO (Data Transfer Object) is a simple object
# used to pass data between different layers of an application—most commonly between the API
# (Controller) and the Service Layer.
# The primary goal of a DTO is to carry data without containing any business logic.

class RegisterUserRequest:
    def __init__(self, email: str) -> None:
        self.email = email