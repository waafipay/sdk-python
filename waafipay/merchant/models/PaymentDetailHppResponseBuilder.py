from waafipay.pg.constants.MerchantProperty import MerchantProperty
from waafipay.pg.constants.LibraryConstants import LibraryConstants
from waafipay.merchant.models.PaymentHppResponseDetail import PaymentHppResponseDetail
from waafipay.pg.models.TransactionInfo import TransactionInfo
from waafipay.pg.request.InitiateHppTransactionRequestBody import InitiateHppTransactionRequestBody
from waafipay.pg.utils.stringUtil import make_string, equals
import json
from json import JSONEncoder
import time

class PaymentDetailHppResponseBuilder:

    channelId = None
    paymentMethod = None
    orderId = None
    hppResultToken = None
    readTimeout = None

    def __init__(self, channel_id, hppResultToken):
        self.channelId = channel_id
        self.hppResultToken = hppResultToken
        self.orderId = 'RPYWP'+str(int(time.time()))
        self.readTimeout = 30

    def build(self):
        return PaymentHppResponseDetail(self)

    def set_channelId(self, channelId):
        self.channelId = channelId
        return self


    def set_orderId(self, orderId):
        self.orderId = orderId
        return self


    def set_hppResultToken(self, hppResultToken):
        self.hppResultToken = hppResultToken
        return self
    
    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)

    def __setattr__(self, key, value):
        if not hasattr(self, key):
            raise AttributeError(" Can not be set ".format(key))
        self.__dict__[key] = value
