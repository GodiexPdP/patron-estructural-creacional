
from rules.commission import calculate_commission
from rules.validation import validate_payment
from infra.logger import log
from infra.audit import audit

from Practica.providers.external_mocks import bank_api


class BankProvider:

    def process(self, payment):
        validate_payment(payment)
        log("Enviando pago a BANCO")

        response = bank_api({
            "amount": payment.amount,
            "currency": payment.currency
        })

        commission = calculate_commission(payment.amount)
        audit(payment)

        return {
            "provider": "BANK",
            "response": response,
            "commission": commission
        }
