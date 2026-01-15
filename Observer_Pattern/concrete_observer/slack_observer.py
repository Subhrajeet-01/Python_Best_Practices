from observer import Observer

class SlackObserver(Observer):

    def update(self, message: str) -> None:
        print(f"Slack Notification: {message}")