from providers.bank_provider import BankProvider
from providers.gateway_provider import GatewayProvider
from providers.instant_provider import InstantProvider

class PaymentProcessor:

    def execute(self, payment_type, payment):
        if payment_type == "BANK":
            provider = BankProvider()
        elif payment_type == "GATEWAY":
            provider = GatewayProvider()
        elif payment_type == "INSTANT":
            provider = InstantProvider()
        else:
            raise Exception("Proveedor no soportado")

        return provider.process(payment)
