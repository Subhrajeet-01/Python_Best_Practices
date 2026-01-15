from command import Command

class CreateUserCommand(Command):
    def execute(self) -> None:
        print("User created successfully.")
        