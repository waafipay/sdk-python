from waafipay.pg.utils.stringUtil import make_string, equals


class TransactionInfo:

    def __init__(self):
        self.referenceId = None
        self.invoiceId = None
        self.amount = None
        self.currency = None
        self.description = None

    def set_referenceId(self, referenceId):
        self.referenceId = referenceId

    def get_referenceId(self):
        return self.referenceId

    def set_invoiceId(self, invoiceId):
        self.invoiceId = invoiceId

    def get_invoiceId(self):
        return self.invoiceId

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def set_currency(self, currency):
        self.currency = currency

    def get_currency(self):
        return self.currency

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
