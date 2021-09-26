from waafipay.pg.constants.MerchantProperty import MerchantProperty
from waafipay.pg.constants.LibraryConstants import LibraryConstants
from waafipay.pg.models.PayerInfo import PayerInfo
from waafipay.pg.models.TransactionInfo import TransactionInfo
from waafipay.pg.request.InitiateTransactionRequestBody import InitiateTransactionRequestBody
from waafipay.pg.utils.stringUtil import make_string, equals
import json
from json import JSONEncoder
import time

class PaymentDetail:

    def __init__(self, payment_detail_builder):
        self.channelId = payment_detail_builder.channelId
        self.paymentMethod = payment_detail_builder.paymentMethod
        self.orderId = payment_detail_builder.orderId
        self.payerInfo = payment_detail_builder.payerInfo
        self.transactionInfo = payment_detail_builder.transactionInfo

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

    
    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)

    def __dir__(self):
        return ""

    def __create_initiate_transaction_request_body(self):
        body = InitiateTransactionRequestBody()

        body.set_serviceName(LibraryConstants.REQUEST_TYPE_PREAUTHORIZE)
        body.set_timestamp(LibraryConstants.REQUEST_TYPE_PREAUTHORIZE)
        body.setschemaVersion(LibraryConstants.SCHEMA_VERSION)
        body.setrequestId(self.get_orderId())
        body.setchannelName(self.get_channelId())
		
        serviceparams = {}
        serviceparams['merchantUid'] = MerchantProperty.get_merchantUid()
        serviceparams['apiUserId'] = MerchantProperty.get_apiUserId()
        serviceparams['apiKey'] = MerchantProperty.get_apiKey()
        serviceparams['paymentMethod'] = self.get_paymentMethod()
        serviceparams['payerInfo'] = {}
        serviceparams['payerInfo']['accountNo'] = self.get_payerInfo().get_accountNo()
        serviceparams['payerInfo']['accountPwd'] = self.get_payerInfo().get_accountPwd()
        serviceparams['payerInfo']['accountExpDate'] = self.get_payerInfo().get_accountExpDate()
        serviceparams['payerInfo']['accountHolder'] = self.get_payerInfo().get_accountHolder()
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

class PaymentDetailsBuilder:

    channelId = None
    paymentMethod = None
    orderId = None
    transactionInfo = None
    payerInfo = None
    readTimeout = None

    def __init__(self, channel_id, paymentMethod, transactionInfo, payerInfo):
        self.channelId = channel_id
        self.paymentMethod = paymentMethod
        self.orderId = 'RPYWP'+str(int(time.time()))
        self.transactionInfo = transactionInfo
        self.payerInfo = payerInfo
        self.readTimeout = 30

    def build(self):
        return PaymentDetail(self)

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

    def set_payerInfo(self, payerInfo):
        self.payerInfo = payerInfo
        return self
    
    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)

    def __setattr__(self, key, value):
        if not hasattr(self, key):
            raise AttributeError(" Can not be set ".format(key))
        self.__dict__[key] = value
