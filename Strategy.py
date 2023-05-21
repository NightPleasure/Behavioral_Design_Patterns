class PaymentStrategy:
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def process_payment(self, amount):
        print(f"Procesare plată prin card de credit pentru suma de {amount}$ cu cardul {self.card_number}")

class DigitalWalletPayment(PaymentStrategy):
    def __init__(self, wallet_id, password):
        self.wallet_id = wallet_id
        self.password = password

    def process_payment(self, amount):
        print(f"Procesare plată prin portofel digital pentru suma de {amount}$ cu portofelul {self.wallet_id}")

class PaymentProcessor:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        self.payment_strategy.process_payment(amount)

payment_processor = PaymentProcessor(CreditCardPayment("1234 5678 9012 3456", "123"))

payment_processor.process_payment(100)

payment_processor.set_payment_strategy(DigitalWalletPayment("my_wallet_id", "password"))

payment_processor.process_payment(50)
