from waafipay.pg.constants.MerchantProperty import MerchantProperty
from waafipay.pg.constants.LibraryConstants import LibraryConstants
from waafipay.pg.models.PayerInfo import PayerInfo
from waafipay.pg.models.TransactionInfo import TransactionInfo
from waafipay.pg.request.InitiateHppTransactionRequestBody import InitiateHppTransactionRequestBody
from waafipay.pg.utils.stringUtil import make_string, equals
import json
from json import JSONEncoder
import time

class PaymentHppDetail:

    def __init__(self, payment_detail_builder):
        self.channelId = payment_detail_builder.channelId
        self.paymentMethod = payment_detail_builder.paymentMethod
        self.orderId = payment_detail_builder.orderId
        self.transactionInfo = payment_detail_builder.transactionInfo
        self.succallbackurl = payment_detail_builder.succallbackurl
        self.failcallbackurl = payment_detail_builder.failcallbackurl

    def get_channelId(self):
        return self.channelId

    def get_paymentMethod(self):
        return self.paymentMethod

    def get_orderId(self):
        return self.orderId

    def get_payerInfo(self):
        return self.payerInfo

    def get_transactionInfo(self):
        return self.transactionInfo

    def get_succallbackurl(self):
        return self.succallbackurl

    def get_failcallbackurl(self):
        return self.failcallbackurl

    
    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)

    def __dir__(self):
        return ""

    def __create_initiate_Hpp_transaction_request_body(self):
        body = InitiateHppTransactionRequestBody()

        body.set_serviceName('HPP_PURCHASE')
        body.set_timestamp(LibraryConstants.REQUEST_TYPE_PREAUTHORIZE)
        body.setschemaVersion(LibraryConstants.SCHEMA_VERSION)
        body.setrequestId(self.get_orderId())
        body.setchannelName(self.get_channelId())
        body.set_succallbackurl(self.get_succallbackurl())
        body.set_failcallbackurl(self.get_failcallbackurl())
		
        serviceparams = {}
        serviceparams['merchantUid'] = MerchantProperty.get_merchantUid()
        serviceparams['storeId'] = MerchantProperty.get_apiUserId()
        serviceparams['hppKey'] = MerchantProperty.get_apiKey()
        serviceparams['paymentMethod'] = self.get_paymentMethod()
        serviceparams['hppSuccessCallbackUrl'] = self.get_succallbackurl()
        serviceparams['hppFailureCallbackUrl'] = self.get_failcallbackurl()
        serviceparams['hppRespDataFormat'] = "1"
        serviceparams['transactionInfo'] = {}
        serviceparams['transactionInfo']['referenceId'] = self.get_transactionInfo().get_referenceId()
        serviceparams['transactionInfo']['invoiceId'] = self.get_transactionInfo().get_invoiceId()
        serviceparams['transactionInfo']['amount'] = self.get_transactionInfo().get_amount()
        serviceparams['transactionInfo']['currency'] = self.get_transactionInfo().get_currency()
        serviceparams['transactionInfo']['description'] = self.get_transactionInfo().get_description()
        
		
        body.setserviceParams(serviceparams)
        
        return body


class JSonnEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

class PaymentDetailHppBuilder:

    channelId = None
    paymentMethod = None
    orderId = None
    transactionInfo = None
    readTimeout = None
    succallbackurl = None
    failcallbackurl = None

    def __init__(self, channel_id, paymentMethod, transactionInfo, succallbackurl, failcallbackurl):
        self.channelId = channel_id
        self.paymentMethod = paymentMethod
        self.orderId = 'RPYWP'+str(int(time.time()))
        self.transactionInfo = transactionInfo
        self.succallbackurl = succallbackurl
        self.failcallbackurl = failcallbackurl
        self.readTimeout = 30

    def build(self):
        return PaymentHppDetail(self)

    def set_channelId(self, channelId):
        self.channelId = channelId
        return self

    def set_paymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod
        return self

    def set_orderId(self, orderId):
        self.orderId = orderId
        return self

    def set_transactionInfo(self, transactionInfo):
        self.transactionInfo = transactionInfo
        return self

    def set_succallbackurl(self, succallbackurl):
        self.succallbackurl = succallbackurl
        return self

    def set_failcallbackurl(self, failcallbackurl):
        self.failcallbackurl = failcallbackurl
        return self
    
    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)

    def __setattr__(self, key, value):
        if not hasattr(self, key):
            raise AttributeError(" Can not be set ".format(key))
        self.__dict__[key] = value
