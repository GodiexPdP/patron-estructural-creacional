def validate_payment(payment):
    if payment.amount <= 0:
        raise ValueError("Monto inválido")
    if not payment.currency:
        raise ValueError("Moneda requerida")
