from observer import Observer

class EmailObserver(Observer):

    def update(self, message: str) -> None:
        print(f"Email Notification: {message}")