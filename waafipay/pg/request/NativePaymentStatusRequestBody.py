from waafipay.pg.utils.stringUtil import make_string, equals


class NativePaymentStatusRequestBody:

    def __init__(self):
        self.mid = None
        self.orderId = None
        self.txnType = None
        self.fromAoaMerchant = None

    def set_mid(self, mid):
        self.mid = mid

    def get_mid(self):
        return self.mid

    def set_order_id(self, order_id):
        self.orderId = order_id

    def get_order_id(self):
        return self.orderId

    def set_txn_type(self, txn_type):
        self.txnType = txn_type

    def get_txn_type(self):
        return self.txnType

    def set_from_aoa_merchant(self, from_aoa_merchant):
        self.fromAoaMerchant = from_aoa_merchant

    def get_from_aoa_merchant(self):
        return self.fromAoaMerchant

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
