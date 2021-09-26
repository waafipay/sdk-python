from uuid import uuid4
from waafipay.pg.constants.ErrorConstants import ErrorConstants
from waafipay.pg.constants.LibraryConstants import LibraryConstants
from waafipay.pg.constants.MerchantProperty import MerchantProperty

from waafipay.pg.request.SecureRequestHeader import SecureRequestHeader
from waafipay.pg.response.ResultInfo import ResultInfo
from waafipay.merchant.models.Time import current_time_millis
from waafipay.pg.SDKException import SDKException
from waafipay.merchant.models.SDKResponse import SDKResponse


class CommonUtil:
    """
        This class receive the Waafipay response objects and translate the to their
        respective merchant response objects and returns call to Merchant Application
    """

    @staticmethod
    def get_secure_request_header(client_id, channel_id=None):
        """This will make secure header
        :param client_id: client_id of merchant
        :param channel_id: channel id from which call is made WEB or WAP
        :return: SecureRequestHeader object
        """
        head = SecureRequestHeader()
        head.set_version(LibraryConstants.VERSION)
        head.set_channel_id(channel_id)
        head.set_request_timestamp(str(current_time_millis()))
        head.set_client_id(client_id)
        return head

    @staticmethod
    def get_sdk_response(e, obj):
        """
        :param e: Exception_response body
        :param obj: object of response body which is to be set with result_info
        :return: SDKResponse {raw_data, response obj}
        """
        MerchantProperty.logger.critical("CommonUtil :: get_sdk_response ExceptionResponseBody: {}".format(e))
        MerchantProperty.logger.debug("CommonUtil :: get_sdk_response type of e is {}".format(type(e)))
        result = ResultInfo()
        result.set_result_status(ErrorConstants.FAILURE)
        result.set_result_code(ErrorConstants.ErrorCode.DEFAULT)
        if isinstance(e, SDKException):
            result.set_result_msg(e.get_msg())
        else:
            result.set_result_msg(e)
        obj.get_body().set_result_info(result)
        if isinstance(e, SDKException):
            MerchantProperty.logger.debug("CommonUtil :: get_sdk_response obj: {}".format(obj))
            return SDKResponse().set_response_object(obj).set_json_response(e.get_raw_data())
        return SDKResponse().set_response_object(obj)

    @staticmethod
    def get_unique_request_id():
        return LibraryConstants.PYTHON_SDK_TEXT + ":" + LibraryConstants.PYTHON_SDK_VERSION + ":" + str(uuid4())
