class Payment:

    def __init__(self, amount, currency, reference, tenant, channel, metadata):
        self.amount = amount
        self.currency = currency
        self.reference = reference
        self.tenant = tenant
        self.channel = channel
        self.metadata = metadata
