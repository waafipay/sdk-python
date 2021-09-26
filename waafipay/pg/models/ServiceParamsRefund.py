from waafipay.pg.utils.stringUtil import make_string, equals
from waafipay.pg.constants.MerchantProperty import MerchantProperty


class ServiceParamsRefund:

    def __init__(self):
        self.amount = None
        self.transactionId = None
        self.description = None
        self.referenceId = None
        self.merchantUid = MerchantProperty.get_merchantUid()
        self.apiUserId = MerchantProperty.get_apiUserId()
        self.apiKey = MerchantProperty.get_apiKey()

    def set_amount(self, amount):
        self.amount = amount

    def set_transactionId(self, transactionId):
        self.transactionId = transactionId
		
    def set_description(self, description):
	    self.description = description

    def set_referenceId(self, referenceId):
        self.referenceId = referenceId

    def get_amount(self):
        return self.amount

    def get_transactionId(self):
        return self.transactionId
		
    def get_description(self):
        return self.description

    def get_referenceId(self):
        return self.referenceId

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
