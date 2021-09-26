from waafipay.pg.response.BaseResponseBody import BaseResponseBody
from waafipay.pg.utils.stringUtil import make_string, equals


class AsyncRefundResponseBody(BaseResponseBody):

    def __init__(self):
        self.refundId = None
        self.mid = None
        self.txnId = None
        self.orderId = None
        self.txnAmount = None
        self.refundAmount = None
        self.refId = None
        super(AsyncRefundResponseBody, self).__init__()

    def set_refund_id(self, refund_id):
        self.refundId = refund_id

    def get_refund_id(self):
        return self.refundId

    def set_mid(self, mid):
        self.mid = mid

    def get_mid(self):
        return self.mid

    def set_txn_id(self, txn_id):
        self.txnId = txn_id

    def get_txn_id(self):
        return self.txnId

    def set_order_id(self, order_id):
        self.orderId = order_id

    def get_order_id(self):
        return self.orderId

    def set_txn_amount(self, txn_amount):
        self.txnAmount = txn_amount

    def get_txn_amount(self):
        return self.txnAmount

    def set_refund_amount(self, refund_amount):
        self.refundAmount = refund_amount

    def get_refund_amount(self):
        return self.refundAmount

    def set_ref_id(self, ref_id):
        self.refId = ref_id

    def get_ref_id(self):
        return self.refId

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
