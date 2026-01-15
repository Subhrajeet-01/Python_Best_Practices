# Invoker

from command import Command

class CLI:
    def run(self, command: Command) -> None:
        command.execute()