from payment_factory import PaymentFactory
from payment_service import PaymentService
from logging_Payment import LoggingPayment

def main() -> None:
    method = PaymentFactory.create("net_banking")
    logging_method = LoggingPayment(method)
    service = PaymentService(logging_method)
    service.process(500)


if __name__ == "__main__":
    main()
