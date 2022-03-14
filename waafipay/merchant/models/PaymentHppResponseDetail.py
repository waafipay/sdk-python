from waafipay.pg.constants.MerchantProperty import MerchantProperty
from waafipay.pg.constants.LibraryConstants import LibraryConstants
from waafipay.pg.models.ServiceParamsRefund import ServiceParamsRefund
from waafipay.pg.request.InitiateHppTransactionResponseBody import InitiateHppTransactionResponseBody
from waafipay.pg.utils.stringUtil import make_string, equals
import time

class PaymentHppResponseDetail:

    def __init__(self, PaymentDetailHppResponseBuilder):
        self.channelId = PaymentDetailHppResponseBuilder.channelId
        self.orderId = PaymentDetailHppResponseBuilder.orderId
        self.hppResultToken = PaymentDetailHppResponseBuilder.hppResultToken

    def get_channelId(self):
        return self.channelId

    def get_orderId(self):
        return self.orderId

    def get_hppResultToken(self):
        return self.hppResultToken

    

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self)

    def __dir__(self):
        return ""

    def __create_Hpp_initiate_request_body(self):
        hpp_initiate_request_body = InitiateHppTransactionResponseBody()
        hpp_initiate_request_body.set_serviceName(LibraryConstants.REQUEST_TYPE_GETRESULTINFO)
        hpp_initiate_request_body.setschemaVersion(LibraryConstants.SCHEMA_VERSION)
        hpp_initiate_request_body.set_timestamp(MerchantProperty.get_merchantUid())
        hpp_initiate_request_body.setrequestId(self.get_orderId())
        hpp_initiate_request_body.setchannelName(self.get_channelId())
        serviceparams = {}
        serviceparams['merchantUid'] = MerchantProperty.get_merchantUid()
        serviceparams['storeId'] = MerchantProperty.get_apiUserId()
        serviceparams['hppKey'] = MerchantProperty.get_apiKey()
        serviceparams['hppResultToken'] = self.get_hppResultToken()
        
		
        hpp_initiate_request_body.setserviceParams(serviceparams)

        return hpp_initiate_request_body


