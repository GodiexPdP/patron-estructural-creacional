from payment_service import PaymentService

class ConsoleApp:

    def run(self):
        print("=== SISTEMA DE PAGOS LEGACY ===")
        print("1. Pago bancario")
        print("2. Pago pasarela")
        print("3. Pago instantáneo")

        option = input("Seleccione tipo de pago: ")

        if option == "1":
            payment_type = "BANK"
        elif option == "2":
            payment_type = "GATEWAY"
        elif option == "3":
            payment_type = "INSTANT"
        else:
            print("Opción inválida")
            return

        service = PaymentService()
        service.process_payment(
            payment_type=payment_type,
            amount=1500,
            currency="COP",
            tenant="TENANT_EMPRESARIAL",
            channel="CONSOLE"
        )
