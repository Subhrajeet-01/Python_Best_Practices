# Usage

from cli import CLI
from create_user import CreateUserCommand
from delete_user import DeleteUserCommand
from update_user import UpdateUserCommand

cli = CLI()
cli.run(CreateUserCommand())
cli.run(UpdateUserCommand())
cli.run(DeleteUserCommand())