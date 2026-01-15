from observer import Observer

class SmsObserver(Observer):

    def update(self, message: str) -> None:
        print(f"SMS Sent: {message}")