from waafipay.pg.response.BaseResponseBody import BaseResponseBody
from waafipay.pg.utils.stringUtil import make_string, equals


class NativeRefundStatusResponseBody(BaseResponseBody):

    def __init__(self):
        super(NativeRefundStatusResponseBody, self).__init__()
        self.txnId = None
        self.orderId = None
        self.txnAmount = None
        self.mid = None
        self.refundAmout = None
        self.txnDate = None
        self.totalRefundAmount = None
        self.refundDate = None
        self.refId = None
        self.bankTxnId = None
        self.txnType = None
        self.gateway = None
        self.bankName = None
        self.paymentMode = None
        self.refundId = None
        self.refundType = None
        self.ssoId = None

    def get_txn_id(self):
        return self.txnId

    def get_order_id(self):
        return self.orderId

    def get_txn_amount(self):
        return self.txnAmount

    def get_mid(self):
        return self.mid

    def get_refund_amount(self):
        return self.refundAmout

    def get_txn_date(self):
        return self.txnDate

    def get_total_refunded_amount(self):
        return self.totalRefundAmount

    def get_refund_date(self):
        return self.refundDate

    def get_ref_id(self):
        return self.refId

    def get_bank_txn_id(self):
        return self.bankTxnId

    def get_txn_type(self):
        return self.txnType

    def get_gateway_name(self):
        return self.gateway

    def get_bank_name(self):
        return self.bankName

    def get_payment_mode(self):
        return self.paymentMode

    def get_refund_id(self):
        return self.refundId

    def get_refund_type(self):
        return self.refundType

    def get_sso_id(self):
        return self.ssoId

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
