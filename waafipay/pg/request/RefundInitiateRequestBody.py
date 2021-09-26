from waafipay.pg.enums import UserSubWalletType
from waafipay.pg.request.RefundBaseRequest import RefundBaseRequest
from waafipay.pg.utils.stringUtil import make_string, equals
from waafipay.pg.utils.ConverterUtil import JsonToObject


class RefundInitiateRequestBody(RefundBaseRequest):

    def __init__(self):
        super(RefundInitiateRequestBody, self).__init__()
        self.txnId = None
        self.refundAmount = None
        self.comments = None
        self.txnType = None
        self.preferredDestination = None
        self.requestId = None
        # map of [UserSubWalletType to big_decimal]
        self.subwalletAmount = None

    # use decorator for this get

    def set_txn_id(self, txn_id):
        self.txnId = txn_id

    def get_txn_id(self):
        return self.txnId

    def set_refund_amount(self, refund_amount):
        self.refundAmount = refund_amount

    def get_refund_amount(self):
        return self.refundAmount

    def set_comments(self, comments):
        self.comments = comments

    def get_comments(self):
        return self.comments

    def set_txn_type(self, txn_type):
        self.txnType = txn_type

    def get_txn_type(self):
        return self.txnType

    def set_preferred_destination(self, preferred_destination):
        self.preferredDestination = preferred_destination

    def get_preferred_destination(self):
        return self.preferredDestination

    def set_request_id(self, request_id):
        self.requestId = request_id

    def get_request_id(self):
        return self.requestId

    def set_sub_wallet_amount(self, sub_wallet_amount):
        self.subwalletAmount = sub_wallet_amount

    def get_sub_wallet_amount(self):
        return self.subwalletAmount

    def set_sub_wallet_amount_string_map(self, sub_wallet_amount_string_dict):
        if sub_wallet_amount_string_dict is not None and len(sub_wallet_amount_string_dict) != 0:
            self.subwalletAmount = dict(UserSubWalletType(), int)
            JsonToObject(sub_wallet_amount_string_dict, self.subwalletAmount)

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
