from command import Command

class UpdateUserCommand(Command):
    def execute(self) -> None:
        print("User updated successfully.")