from waafipay.pg.constants.MerchantProperty import MerchantProperty
from waafipay.pg.constants.LibraryConstants import LibraryConstants
from waafipay.pg.models.ServiceParamsRefund import ServiceParamsRefund
from waafipay.pg.request.InitiateRefundTransactionRequestBody import InitiateRefundTransactionRequestBody
from waafipay.pg.utils.stringUtil import make_string, equals
import time

class PaymentRefund:

    def __init__(self, refund_detail_builder):
        self.channelId = refund_detail_builder.channelId
        self.orderId = refund_detail_builder.orderId
        self.serviceParams = refund_detail_builder.serviceParams

    def get_channelId(self):
        return self.channelId

    def get_orderId(self):
        return self.orderId

    def get_serviceParams(self):
        return self.serviceParams

    

    def __str__(self):
        return ""

    def __eq__(self, other):
        return equals(self)

    def __dir__(self):
        return ""

    def __create_refund_initiate_request_body(self):
        refund_initiate_request_body = InitiateRefundTransactionRequestBody()
        refund_initiate_request_body.setserviceName(LibraryConstants.REQUEST_TYPE_REFUND)
        refund_initiate_request_body.setschemaVersion(LibraryConstants.SCHEMA_VERSION)
        refund_initiate_request_body.settimestamp(MerchantProperty.get_merchantUid())
        refund_initiate_request_body.setrequestId(self.get_orderId())
        refund_initiate_request_body.setserviceParams(self.get_serviceParams())
        refund_initiate_request_body.setchannelName(self.get_channelId())
        return refund_initiate_request_body


class PaymentRefundlBuilder:
    channelId = None
    orderId = None
    serviceParams = None
    read_timeout = 30

    def __init__(self, channelId, serviceParams):
        self.channelId = channelId
        self.orderId = 'RPYWP'+str(int(time.time()))
        self.serviceParams = serviceParams

    def build(self):
        return PaymentRefund(self)

    def set_orderId(self, orderId):
        self.orderId = orderId
        return self

    def set_channelId(self, channelId):
        self.channelId = channelId
        return self

    def set_serviceParams(self, serviceParams):
        self.serviceParams = serviceParams
        return self
    
    def set_read_timeout(self, read_timeout):
        self.read_timeout = read_timeout
        return self

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self)

    def __setattr__(self, key, value):
        if not hasattr(self, key):
            raise AttributeError(" Can not be set ".format(key))
        self.__dict__[key] = value

    def __dir__(self):
        return ""
