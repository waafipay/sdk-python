from waafipay.pg.constants.MerchantProperty import MerchantProperty
from waafipay.pg.constants.LibraryConstants import LibraryConstants
from waafipay.pg.models.ServiceParams import ServiceParams
from waafipay.pg.request.InitiateCommitTransactionRequestBody import InitiateCommitTransactionRequestBody
from waafipay.pg.request.InitiateRefundTransactionRequestBody import InitiateRefundTransactionRequestBody
from waafipay.pg.utils.stringUtil import make_string, equals
import time

class PaymentDetailCommit:

    def __init__(self, payment_detail_com_builder):
        self.channelId = payment_detail_com_builder.channelId
        self.orderId = payment_detail_com_builder.orderId
        self.serviceParams = payment_detail_com_builder.serviceParams

    def get_channelId(self):
        return self.channelId

    def get_serviceParams(self):
        return self.serviceParams

    def get_orderId(self):
        return self.orderId    
    
    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)

    def __dir__(self):
        return ""

    def __create_initiate_transaction_request_body(self):
        body = InitiateCommitTransactionRequestBody()

        body.set_serviceName(LibraryConstants.REQUEST_TYPE_PREAUTHCOMMIT)
        body.setschemaVersion(LibraryConstants.SCHEMA_VERSION)
        body.settimestamp(MerchantProperty.get_merchantUid())
        

        body.setrequestId(self.get_orderId())
        body.setserviceParams(self.get_serviceParams())
        body.setchannelName(self.get_channelId())
        return body
		
    def __create_cancel_transaction_request_body(self):
        body = InitiateCommitTransactionRequestBody()

        body.set_serviceName(LibraryConstants.REQUEST_TYPE_PREAUTHCANCEL)
        body.setschemaVersion(LibraryConstants.SCHEMA_VERSION)
        body.settimestamp(MerchantProperty.get_merchantUid())

        body.setrequestId(self.get_orderId())
        body.setserviceParams(self.get_serviceParams())
        body.setchannelName(self.get_channelId())
        return body
		
    def __create_pcancel_transaction_request_body(self):
        body = InitiateCommitTransactionRequestBody()

        body.set_serviceName(LibraryConstants.REQUEST_TYPE_CANCELPURCHASE)
        body.setschemaVersion(LibraryConstants.SCHEMA_VERSION)
        body.settimestamp(MerchantProperty.get_merchantUid())

        body.setrequestId(self.get_orderId())
        body.setserviceParams(self.get_serviceParams())
        body.setchannelName(self.get_channelId())
        return body


class PaymentCommitDetailBuilder:

    channelId = None
    serviceParams = None
    orderId = None
    readTimeout = None

    def __init__(self, channel_id, serviceParams):
        self.channelId = channel_id
        self.serviceParams = serviceParams
        self.orderId = 'RPYWP'+str(int(time.time()))
        self.readTimeout = 30

    def build(self):
        return PaymentDetailCommit(self)

    def set_channelId(self, channelId):
        self.channelId = channelId
        return self

    def set_serviceParams(self, serviceParams):
        self.serviceParams = serviceParams
        return self

    def set_orderId(self, orderId):
        self.orderId = orderId
        return self

    
    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)

    def __setattr__(self, key, value):
        if not hasattr(self, key):
            raise AttributeError(" Can not be set ".format(key))
        self.__dict__[key] = value
