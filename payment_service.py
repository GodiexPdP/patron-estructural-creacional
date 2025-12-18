from payment_processor import PaymentProcessor
from models.payment import Payment
from utils.ids import generate_reference

class PaymentService:

    def process_payment(self, payment_type, amount, currency, tenant, channel):
        print("Iniciando proceso de pago...")

        payment = Payment(
            amount=amount,
            currency=currency,
            reference=generate_reference(),
            tenant=tenant,
            channel=channel,
            metadata={"source": "console"}
        )

        processor = PaymentProcessor()
        result = processor.execute(payment_type, payment)

        print("Resultado final:", result)
