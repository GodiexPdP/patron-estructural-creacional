from providers.external_mocks import instant_service
from rules.commission import calculate_commission
from rules.validation import validate_payment
from infra.logger import log
from infra.audit import audit

class InstantProvider:

    def process(self, payment):
        validate_payment(payment)
        log("Procesando pago INSTANTÁNEO")

        success = instant_service(payment.amount)

        commission = calculate_commission(payment.amount)
        audit(payment)

        return {
            "provider": "INSTANT",
            "success": success,
            "commission": commission
        }
