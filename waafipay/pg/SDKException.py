from waafipay.pg.constants.ErrorConstants import ErrorConstants
from waafipay.pg.constants.MerchantProperty import MerchantProperty
from waafipay.pg.utils.stringUtil import make_string


class SDKException(Exception):
    """RequestValidationException creates exception which are originated from Merchant code
    """
    raw_data = None

    def __init__(self, msg):
        self.msg = msg
        self.raw_data = None
        MerchantProperty.logger.critical("SDKException")

    def get_msg(self):
        return self.msg

    def set_raw_data(self, raw_data):
        self.raw_data = raw_data
        return self

    def get_raw_data(self):
        return self.raw_data

    def __str__(self):
        return make_string(self)

    @staticmethod
    def get_merchant_property_initialization_exception():
        """
        :return: SDKException when merchant have not initialized parameter
        """
        MerchantProperty.logger.critical("SDKException :: " + ErrorConstants.ErrorMessage.MISSING_MERCHANT_PROPERTY)
        return SDKException(ErrorConstants.ErrorMessage.MISSING_MERCHANT_PROPERTY);

    @staticmethod
    def get_missing_mandatory_parameters_exception():
        """
        :return: SDKException when any mandatory parameter is missing
        """
        MerchantProperty.logger.critical("SDKException :: " + ErrorConstants.ErrorMessage.MISSING_MANDATORY_PARAMETERS)
        return SDKException(ErrorConstants.ErrorMessage.MISSING_MANDATORY_PARAMETERS)

    @staticmethod
    def get_transaction_token_exception():
        """
        :return: SDKException when transaction token is missing
        """
        MerchantProperty.logger.critical("SDKException :: " + ErrorConstants.ErrorMessage.MISSING_TRANSACTION_TOKEN)
        return SDKException(ErrorConstants.ErrorMessage.MISSING_TRANSACTION_TOKEN)

    @staticmethod
    def get_signature_validation_failed_exception(response_received):
        """
        :param response_received: response received in api hit
        :return: SDKException when Signature validation failed at merchant side
        """
        MerchantProperty.logger.critical("SDKException :: " + ErrorConstants.ErrorMessage.SIGNATURE_VALIDATION_FAILED)
        return SDKException(ErrorConstants.ErrorMessage.SIGNATURE_VALIDATION_FAILED).set_raw_data(response_received)

    @staticmethod
    def get_sdk_exception_with_json_data(exception_message, json_object):
        """
        :param exception_message: exception message
        :param json_object: json object received in api hit
        :return: SDKException when exception occur after api hit
        """
        MerchantProperty.logger.critical("SDKException :: " + exception_message)
        return SDKException(exception_message).set_raw_data(json_object)

    @staticmethod
    def get_sdk_exception(exception_message):
        """
        :param exception_message: exception message
        :return: SDKException when exception occur before api hit
        """
        MerchantProperty.logger.critical("SDKException :: " + exception_message)
        return SDKException(exception_message)
