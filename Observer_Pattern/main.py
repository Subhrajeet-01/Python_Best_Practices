from user_event_manager import UserEventManager
from concrete_observer.email_observer import EmailObserver
from concrete_observer.sms_observer import SmsObserver
from concrete_observer.push_observer import PushObserver
from concrete_observer.slack_observer import SlackObserver


def main() -> None:
    event_manager = UserEventManager()

    email_observer = EmailObserver()
    sms_observer = SmsObserver()
    push_observer = PushObserver()
    slack_observer = SlackObserver()

    event_manager.attach(email_observer)
    event_manager.attach(sms_observer)
    event_manager.attach(push_observer)
    event_manager.attach(slack_observer)
    event_manager.detach(slack_observer)

    event_manager.notify("User signed up for the newsletter.")
    event_manager.notify("User made a purchase.")

if __name__ == "__main__":
    main()
