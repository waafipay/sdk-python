from sys import exc_info

from waafipay.pg.request.InitiateTransactionRequest import InitiateTransactionRequest
from waafipay.pg.request.InitiateTransactionRequestBody import InitiateTransactionRequestBody


from waafipay.pg.response.CommitInitiateTransactionResponse import CommitInitiateTransactionResponse
from waafipay.pg.response.CommitInitiateTransactionResponseBody import CommitInitiateTransactionResponseBody


from waafipay.pg.request.NativePaymentStatusRequest import NativePaymentStatusRequest

from waafipay.pg.response.InitiateTransactionResponse import InitiateTransactionResponse
from waafipay.pg.response.InitiateTransactionResponseBody import InitiateTransactionResponseBody
from waafipay.pg.response.NativePaymentStatusResponse import NativePaymentStatusResponse

from waafipay.pg.utils.CommonUtil import CommonUtil
from waafipay.pg.utils.stringUtil import is_empty, format_string

from waafipay.pg.constants.MerchantProperty import MerchantProperty
from waafipay.pg.constants.LibraryConstants import LibraryConstants

from waafipay.pg.models.PayerInfo import PayerInfo
from waafipay.pg.models.TransactionInfo import TransactionInfo
from waafipay.pg.models.ServiceParamsRefund import ServiceParamsRefund
from waafipay.pg.models.ServiceParams import ServiceParams

from waafipay.pg.SDKException import SDKException
from waafipay.pg.Request import Request
from waafipay.merchant.models.PaymentDetail import PaymentDetail
from waafipay.merchant.models.PaymentHppDetail import PaymentHppDetail
from waafipay.merchant.models.PaymentDetailHppResponseBuilder import PaymentDetailHppResponseBuilder
from waafipay.merchant.models.PaymentHppResponseDetail import PaymentHppResponseDetail
from waafipay.merchant.models.PaymentDetailCommit import PaymentDetailCommit
from waafipay.merchant.models.PaymentRefund import PaymentRefund
from waafipay.merchant.models.SDKResponse import SDKResponse



class Payment:
    """This class handle all call(which is from DemoApp) related to create transaction and payment status  
    """
    @classmethod
    def CheckHppresp(cls, payment_details):
        """
        :param payment_details: has all mandatory parameter and some others
        :return: SDKResponse {jsonData, InitiateTransactionResponse}
        """
        MerchantProperty.set_logger_name(CommonUtil.get_unique_request_id())
        try:
            if not MerchantProperty.is_initialized:
                return CommonUtil.get_sdk_response(SDKException.get_merchant_property_initialization_exception(), InitiateTransactionResponse())
            MerchantProperty.logger.info("Payment :: create_txn_token payment_details: {}".format(payment_details))
            cls.__validate_create_hppresp_txn_token(payment_details)
            request = cls.__create_initiate_hppresp_transaction_request(payment_details)
            response = InitiateTransactionResponse()
            url = MerchantProperty.get_initiate_txn_url()
            return Request.processHppresp(request.get_body(), url, response, MerchantProperty.get_connect_timeout())
            # return response
        except Exception:
            return CommonUtil.get_sdk_response(exc_info()[1], InitiateTransactionResponse())

    @staticmethod
    def __create_initiate_hppresp_transaction_request(payment_details):
        """This method convert payment_details into InitiateTransactionRequestBody()
        :param payment_details: has all mandatory parameter and some others
        :return: InitiateTransactionRequest object
        """
        head = None
        body = payment_details._PaymentHppResponseDetail__create_Hpp_initiate_request_body()
        return InitiateTransactionRequest().set_head(head).set_body(body)

    @staticmethod
    def __validate_create_hppresp_txn_token(payment_details):
        """Checking mandatory field it has or not
        :param payment_details:
        :return: if mandatory parameter is not there return SDKException
        """
        MerchantProperty.logger.info("Payment :: __validate_create_hppresp_txn_token for payment_details: {0} ".format(payment_details))
        if is_empty(payment_details.get_orderId()) or is_empty(payment_details.get_hppResultToken()) or is_empty(payment_details.get_channelId()):
            raise SDKException.get_missing_mandatory_parameters_exception()

    @classmethod
    def CreateHppTxn(cls, payment_details):
        """
        :param payment_details: has all mandatory parameter and some others
        :return: SDKResponse {jsonData, InitiateTransactionResponse}
        """
        MerchantProperty.set_logger_name(CommonUtil.get_unique_request_id())
        try:
            if not MerchantProperty.is_initialized:
                return CommonUtil.get_sdk_response(SDKException.get_merchant_property_initialization_exception(), InitiateTransactionResponse())
            MerchantProperty.logger.info("Payment :: create_txn_token payment_details: {}".format(payment_details))
            cls.__validate_create_hpp_txn_token(payment_details)
            request = cls.__create_initiate_hpp_transaction_request(payment_details)
            response = InitiateTransactionResponse()
            url = MerchantProperty.get_initiate_txn_url()
            return Request.processHpp(request.get_body(), url, response, MerchantProperty.get_connect_timeout())
            # return response
        except Exception:
            return CommonUtil.get_sdk_response(exc_info()[1], InitiateTransactionResponse())

    @staticmethod
    def __create_initiate_hpp_transaction_request(payment_details):
        """This method convert payment_details into InitiateTransactionRequestBody()
        :param payment_details: has all mandatory parameter and some others
        :return: InitiateTransactionRequest object
        """
        head = None
        body = payment_details._PaymentHppDetail__create_initiate_Hpp_transaction_request_body()
        return InitiateTransactionRequest().set_head(head).set_body(body)


    @staticmethod
    def __validate_create_hpp_txn_token(payment_details):
        """Checking mandatory field it has or not
        :param payment_details:
        :return: if mandatory parameter is not there return SDKException
        """
        MerchantProperty.logger.info("Payment :: validateCreateHppTxnToken for payment_details: {0} ".format(payment_details))
        transactionInfo = payment_details.get_transactionInfo()
        if is_empty(payment_details.get_orderId()) or is_empty(transactionInfo.get_referenceId())\
                or is_empty(transactionInfo.get_amount()) or is_empty(transactionInfo.get_currency())\
                or is_empty(payment_details.get_succallbackurl()) or is_empty(payment_details.get_failcallbackurl())\
                or is_empty(transactionInfo.get_description()) or is_empty(transactionInfo.get_invoiceId()):
            raise SDKException.get_missing_mandatory_parameters_exception()

    @classmethod
    def CreateTxn(cls, payment_details):
        """
        :param payment_details: has all mandatory parameter and some others
        :return: SDKResponse {jsonData, InitiateTransactionResponse}
        """
        MerchantProperty.set_logger_name(CommonUtil.get_unique_request_id())
        try:
            if not MerchantProperty.is_initialized:
                return CommonUtil.get_sdk_response(SDKException.get_merchant_property_initialization_exception(), InitiateTransactionResponse())
            MerchantProperty.logger.info("Payment :: create_txn_token payment_details: {}".format(payment_details))
            cls.__validate_create_txn_token(payment_details)
            request = cls.__create_initiate_transaction_request(payment_details)
            response = InitiateTransactionResponse()
            url = MerchantProperty.get_initiate_txn_url()
            return Request.process(request.get_body(), url, response, MerchantProperty.get_connect_timeout())
            # return response
        except Exception:
            return CommonUtil.get_sdk_response(exc_info()[1], InitiateTransactionResponse())

    @staticmethod
    def __create_initiate_transaction_request(payment_details):
        """This method convert payment_details into InitiateTransactionRequestBody()
        :param payment_details: has all mandatory parameter and some others
        :return: InitiateTransactionRequest object
        """
        head = None
        body = payment_details._PaymentDetail__create_initiate_transaction_request_body()
        return InitiateTransactionRequest().set_head(head).set_body(body)

    
    @staticmethod
    def __validate_create_txn_token(payment_details):
        """Checking mandatory field it has or not
        :param payment_details:
        :return: if mandatory parameter is not there return SDKException
        """
        MerchantProperty.logger.info("Payment :: validateCreateTxnToken for payment_details: {0} ".format(payment_details))
        payerInfo = payment_details.get_payerInfo()
        transactionInfo = payment_details.get_transactionInfo()
        if is_empty(payment_details.get_orderId()) or is_empty(payerInfo.get_accountNo())\
                or is_empty(payerInfo.get_accountPwd()) or is_empty(transactionInfo.get_referenceId())\
                or is_empty(transactionInfo.get_amount()) or is_empty(transactionInfo.get_currency())\
                or is_empty(transactionInfo.get_description()) or is_empty(transactionInfo.get_invoiceId()):
            raise SDKException.get_missing_mandatory_parameters_exception()
	
    @classmethod
    def CreateCommitTxn(cls, payment_details):
        """
        :param payment_details: has all mandatory parameter and some others
        :return: SDKResponse {jsonData, CommitInitiateTransactionResponse}
        """
        MerchantProperty.set_logger_name(CommonUtil.get_unique_request_id())
        try:
            if not MerchantProperty.is_initialized:
                return CommonUtil.get_sdk_response(SDKException.get_merchant_property_initialization_exception(), CommitInitiateTransactionResponse())
            MerchantProperty.logger.info("Payment :: create_txn_token payment_details: {}".format(payment_details))
            cls.__validate_create_commit_txn_token(payment_details)
            request = cls.__create_initiate_commit_transaction_request(payment_details)
            # response = SDKResponse().set_response_object(CommitInitiateTransactionResponse())
            response = CommitInitiateTransactionResponse()
            url = MerchantProperty.get_initiate_txn_url()
            return Request.processcommit(request.get_body(), url, response, MerchantProperty.get_connect_timeout())
            # return response
        except Exception:
            return CommonUtil.get_sdk_response(exc_info()[1], CommitInitiateTransactionResponse())

    @staticmethod
    def __create_initiate_commit_transaction_request(payment_details):
        """This method convert payment_details into InitiateTransactionRequestBody()
        :param payment_details: has all mandatory parameter and some others
        :return: InitiateTransactionRequest object
        """
        head = None
        body = payment_details._PaymentDetailCommit__create_initiate_transaction_request_body()
        return InitiateTransactionRequest().set_head(head).set_body(body)

    @staticmethod
    def __validate_create_commit_txn_token(payment_details):
        """Checking mandatory field it has or not
        :param payment_details:
        :return: if mandatory parameter is not there return SDKException
        """
        MerchantProperty.logger.info("Payment :: validateCreateCommitTxnToken for payment_details: {0} ".format(payment_details))
        serviceParams = payment_details.get_serviceParams()
        if is_empty(serviceParams.get_transactionId()) or is_empty(serviceParams.get_description())\
                or is_empty(serviceParams.get_referenceId()):
            raise SDKException.get_missing_mandatory_parameters_exception()

    @classmethod
    def CreateCancelCommitTxn(cls, payment_details):
        """
        :param payment_details: has all mandatory parameter and some others
        :return: SDKResponse {jsonData, CommitInitiateTransactionResponse}
        """
        MerchantProperty.set_logger_name(CommonUtil.get_unique_request_id())
        try:
            if not MerchantProperty.is_initialized:
                return CommonUtil.get_sdk_response(SDKException.get_merchant_property_initialization_exception(), CommitInitiateTransactionResponse())
            MerchantProperty.logger.info("Payment :: create_txn_token payment_details: {}".format(payment_details))
            cls.__validate_create_commit_txn_token(payment_details)
            request = cls.__create_initiate_cancel_commit_transaction_request(payment_details)
            # response = SDKResponse().set_response_object(CommitInitiateTransactionResponse())
            response = CommitInitiateTransactionResponse()
            url = MerchantProperty.get_initiate_txn_url()
            return Request.processcommit(request.get_body(), url, response, MerchantProperty.get_connect_timeout())
            # return response
        except Exception:
            return CommonUtil.get_sdk_response(exc_info()[1], CommitInitiateTransactionResponse())

    @staticmethod
    def __create_initiate_cancel_commit_transaction_request(payment_details):
        """This method convert payment_details into InitiateTransactionRequestBody()
        :param payment_details: has all mandatory parameter and some others
        :return: InitiateTransactionRequest object
        """
        head = None
        body = payment_details._PaymentDetailCommit__create_cancel_transaction_request_body()
        return InitiateTransactionRequest().set_head(head).set_body(body)

    @classmethod
    def CreatePurchaseCancelTxn(cls, payment_details):
        """
        :param payment_details: has all mandatory parameter and some others
        :return: SDKResponse {jsonData, CommitInitiateTransactionResponse}
        """
        MerchantProperty.set_logger_name(CommonUtil.get_unique_request_id())
        try:
            if not MerchantProperty.is_initialized:
                return CommonUtil.get_sdk_response(SDKException.get_merchant_property_initialization_exception(), CommitInitiateTransactionResponse())
            MerchantProperty.logger.info("Payment :: create_txn_token payment_details: {}".format(payment_details))
            cls.__validate_create_commit_txn_token(payment_details)
            request = cls.__create_purchase_cancel_commit_transaction_request(payment_details)
            # response = SDKResponse().set_response_object(CommitInitiateTransactionResponse())
            response = CommitInitiateTransactionResponse()
            url = MerchantProperty.get_initiate_txn_url()
            return Request.processcommit(request.get_body(), url, response, MerchantProperty.get_connect_timeout())
            # return response
        except Exception:
            return CommonUtil.get_sdk_response(exc_info()[1], CommitInitiateTransactionResponse())

    @staticmethod
    def __create_purchase_cancel_commit_transaction_request(payment_details):
        """This method convert payment_details into InitiateTransactionRequestBody()
        :param payment_details: has all mandatory parameter and some others
        :return: InitiateTransactionRequest object
        """
        head = None
        body = payment_details._PaymentDetailCommit__create_pcancel_transaction_request_body()
        return InitiateTransactionRequest().set_head(head).set_body(body)

    @classmethod
    def CreateRefundTxn(cls, payment_details):
        """
        :param payment_details: has all mandatory parameter and some others
        :return: SDKResponse {jsonData, CommitInitiateTransactionResponse}
        """
        MerchantProperty.set_logger_name(CommonUtil.get_unique_request_id())
        try:
            if not MerchantProperty.is_initialized:
                return CommonUtil.get_sdk_response(SDKException.get_merchant_property_initialization_exception(), CommitInitiateTransactionResponse())
            MerchantProperty.logger.info("Payment :: create_txn_token payment_details: {}".format(payment_details))
            cls.__validate_refund_commit_txn_token(payment_details)
            request = cls.__create_refund_transaction_request(payment_details)
            # response = SDKResponse().set_response_object(CommitInitiateTransactionResponse())
            response = CommitInitiateTransactionResponse()
            url = MerchantProperty.get_initiate_txn_url()
            return Request.processcommit(request.get_body(), url, response, MerchantProperty.get_connect_timeout())
            # return response
        except Exception:
            return CommonUtil.get_sdk_response(exc_info()[1], CommitInitiateTransactionResponse())

    @staticmethod
    def __create_refund_transaction_request(payment_details):
        """This method convert payment_details into InitiateTransactionRequestBody()
        :param payment_details: has all mandatory parameter and some others
        :return: InitiateTransactionRequest object
        """
        head = None
        body = payment_details._PaymentRefund__create_refund_initiate_request_body()
        return InitiateTransactionRequest().set_head(head).set_body(body)

    @staticmethod
    def __validate_refund_commit_txn_token(payment_details):
        """Checking mandatory field it has or not
        :param payment_details:
        :return: if mandatory parameter is not there return SDKException
        """
        MerchantProperty.logger.info("Payment :: validateCreateCommitTxnToken for payment_details: {0} ".format(payment_details))
        serviceParams = payment_details.get_serviceParams()
        if is_empty(serviceParams.get_transactionId()) or is_empty(serviceParams.get_description())\
                or is_empty(serviceParams.get_referenceId()) or is_empty(serviceParams.get_amount()):
            raise SDKException.get_missing_mandatory_parameters_exception()
	

    def __dir__(self):
        return ""


