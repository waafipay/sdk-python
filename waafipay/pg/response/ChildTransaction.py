from waafipay.pg.utils.stringUtil import make_string, equals


class ChildTransaction:

    def __init__(self):
        self.txnId = None
        self.paymentMode = None
        self.txnAmount = None
        self.gateway = None
        self.bankTxnId = None
        self.bankName = None
        self.status = None
        self.cardIndexNo = None
        self.maskedCardNo = None

    def set_txn_id(self, txn_id):
        self.txnId = txn_id

    def get_txn_id(self):
        return self.txnId

    def set_payment_mode(self, payment_mode):
        self.paymentMode = payment_mode

    def get_payment_mode(self):
        return self.paymentMode

    def set_txn_amount(self, txn_amount):
        self.txnAmount = txn_amount

    def get_txn_amount(self):
        return self.txnAmount

    def set_gateway(self, gateway):
        self.gateway = gateway

    def get_gateway(self):
        return self.gateway

    def set_bank_txn_id(self, bank_txn_id):
        self.bankTxnId = bank_txn_id

    def get_bank_txn_id(self):
        return self.bankTxnId

    def set_bank_name(self, bank_name):
        self.bankName = bank_name

    def get_bank_name(self):
        return self.bankName

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_card_index_no(self, card_index_no):
        self.cardIndexNo = card_index_no

    def get_card_index_no(self):
        return self.cardIndexNo

    def set_masked_card_no(self, masked_card_no):
        self.maskedCardNo = masked_card_no

    def get_masked_card_no(self):
        return self.maskedCardNo

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
