from observer import Observer

class PushObserver(Observer):

    def update(self, message: str) -> None:
        print(f"Push Notification: {message}")
        