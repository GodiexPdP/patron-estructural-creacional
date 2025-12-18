from providers.external_mocks import gateway_sdk
from rules.commission import calculate_commission
from rules.validation import validate_payment
from infra.logger import log
from infra.audit import audit

class GatewayProvider:

    def process(self, payment):
        validate_payment(payment)
        log("Ejecutando SDK de PASARELA")

        response = gateway_sdk({
            "value": payment.amount,
            "currency": payment.currency
        })

        commission = calculate_commission(payment.amount)
        audit(payment)

        return {
            "provider": "GATEWAY",
            "response": response,
            "commission": commission
        }
