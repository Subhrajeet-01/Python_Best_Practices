from command import Command

class DeleteUserCommand(Command):
    def execute(self) -> None:
        print("User deleted successfully.")