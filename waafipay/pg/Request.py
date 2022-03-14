from requests import post

from waafipay.pg.constants.MerchantProperty import MerchantProperty
from waafipay.pg.constants.LibraryConstants import LibraryConstants

from waafipay.pg.response.InitiateTransactionResponseBody import InitiateTransactionResponseBody
from waafipay.pg.response.InitiateTransactionResponse import InitiateTransactionResponse

from waafipay.pg.response.ResultInfo import ResultInfo
from waafipay.pg.utils.ConverterUtil import JsonToObject
from waafipay.pg.SDKException import SDKException
from waafipay.pg.utils.stringUtil import is_empty, format_string
import json


class Request:

    headers = {'Content-type': LibraryConstants.APPLICATION_JSON_TEXT}

    @classmethod
    def processHppresp(cls, request, url, response, read_timeout=30):
        """
        :param request: it contain head and body which we want to transmit over network
        :param url: on which we want to make hit
        :param response: object in which value of response will be putted
        :param read_timeout: this is in "Second" unit
        :return: None, it is just setting value in response object
        """
        cls.headers[LibraryConstants.X_REQUEST_ID] = MerchantProperty.request_id
        post_args = {
            'headers': cls.headers,
            'timeout': (MerchantProperty.connect_timeout, read_timeout),
            'data': format_string(request)
        }
        res = post(url, **post_args)
        request_response = res.json()
        return request_response

    @classmethod
    def processHpp(cls, request, url, response, read_timeout=30):
        """
        :param request: it contain head and body which we want to transmit over network
        :param url: on which we want to make hit
        :param response: object in which value of response will be putted
        :param read_timeout: this is in "Second" unit
        :return: None, it is just setting value in response object
        """
        cls.headers[LibraryConstants.X_REQUEST_ID] = MerchantProperty.request_id
        post_args = {
            'headers': cls.headers,
            'timeout': (MerchantProperty.connect_timeout, read_timeout),
            'data': format_string(request)
        }
        res = post(url, **post_args)
        request_response = res.json()
        return request_response

    @classmethod
    def process(cls, request, url, response, read_timeout=30):
        """
        :param request: it contain head and body which we want to transmit over network
        :param url: on which we want to make hit
        :param response: object in which value of response will be putted
        :param read_timeout: this is in "Second" unit
        :return: None, it is just setting value in response object
        """
        cls.headers[LibraryConstants.X_REQUEST_ID] = MerchantProperty.request_id
        post_args = {
            'headers': cls.headers,
            'timeout': (MerchantProperty.connect_timeout, read_timeout),
            'data': format_string(request)
        }
        res = post(url, **post_args)
        request_response = res.json()
        # print(request_response['schemaVersion'])
        # newresponse = {}
        # newresponse['schemaVersion'] = request_response['schemaVersion']
        # newresponse['timestamp'] = request_response['timestamp']
        # newresponse['requestId'] = request_response['requestId']
        # newresponse['responseCode'] = request_response['responseCode']
        # newresponse['responseMsg'] = request_response['responseMsg']
        # newresponse['errorCode'] = request_response['errorCode']
        # newresponse['transactionId'] = request_response['params']['transactionId']
        # newresponse['referenceId'] = request_response['params']['referenceId']
        # newresponse['state'] = request_response['params']['state']
        # newresponse['description'] = request_response['params']['description']
        # newresponse['txAmount'] = request_response['params']['txAmount']
        # resultInfo = ResultInfo()
        # if is_empty(request_response['params']['transactionId']):
        	# resultInfo.set_result_status(request_response['responseMsg'])
        # else:
        	# resultInfo.set_result_status(request_response['responseMsg'])
        # resultInfo.set_result_code(request_response['responseCode'])
        # resultInfo.set_result_msg(request_response)
        # respbody = InitiateTransactionResponseBody()
        # respbody.set_schemaVersion(request_response['schemaVersion'])
        # respbody.set_timestamp(request_response['timestamp'])
        # respbody.set_requestId(request_response['requestId'])
        # respbody.set_responseCode(request_response['responseCode'])
        # respbody.set_responseMsg(request_response['responseMsg'])
        # respbody.set_errorCode(request_response['errorCode'])
        # respbody.set_transactionId(request_response['params']['transactionId'])
        # respbody.set_referenceId(request_response['params']['referenceId'])
        # respbody.set_state(request_response['params']['state'])
        # respbody.set_description(request_response['params']['description'])
        # respbody.set_txAmount(request_response['params']['txAmount'])
        # response = InitiateTransactionResponse()
        # response.set_body(respbody)
        # response.set_body(respbody)
        return request_response

    @classmethod	
    def processcommit(cls, request, url, response, read_timeout=30):
        """
        :param request: it contain head and body which we want to transmit over network
        :param url: on which we want to make hit
        :param response: object in which value of response will be putted
        :param read_timeout: this is in "Second" unit
        :return: None, it is just setting value in response object
        """
        cls.headers[LibraryConstants.X_REQUEST_ID] = MerchantProperty.request_id
        post_args = {
            'headers': cls.headers,
            'timeout': (MerchantProperty.connect_timeout, read_timeout),
            'data': format_string(request)
        }
        res = post(url, **post_args)
        request_response = res.json()
        # print(request_response['schemaVersion'])
        # newresponse = {}
        # newresponse['schemaVersion'] = request_response['schemaVersion']
        # newresponse['timestamp'] = request_response['timestamp']
        # newresponse['requestId'] = request_response['requestId']
        # newresponse['responseCode'] = request_response['responseCode']
        # newresponse['responseMsg'] = request_response['responseMsg']
        # newresponse['errorCode'] = request_response['errorCode']
        # newresponse['transactionId'] = request_response['params']['transactionId']
        # newresponse['referenceId'] = request_response['params']['referenceId']
        # newresponse['state'] = request_response['params']['state']
        # newresponse['description'] = request_response['params']['description']
        # newresponse['txAmount'] = request_response['params']['txAmount']
        # resultInfo = ResultInfo()
        # if is_empty(request_response['params']['transactionId']):
        	# resultInfo.set_result_status(request_response['responseMsg'])
        # else:
        	# resultInfo.set_result_status(request_response['responseMsg'])
        # resultInfo.set_result_code(request_response['responseCode'])
        # resultInfo.set_result_msg(request_response)
        # respbody = InitiateTransactionResponseBody()
        # respbody.set_schemaVersion(request_response['schemaVersion'])
        # respbody.set_timestamp(request_response['timestamp'])
        # respbody.set_requestId(request_response['requestId'])
        # respbody.set_responseCode(request_response['responseCode'])
        # respbody.set_responseMsg(request_response['responseMsg'])
        # respbody.set_errorCode(request_response['errorCode'])
        # respbody.set_transactionId(request_response['params']['transactionId'])
        # respbody.set_referenceId(request_response['params']['referenceId'])
        # respbody.set_state(request_response['params']['state'])
        # respbody.set_description(request_response['params']['description'])
        # respbody.set_txAmount(request_response['params']['txAmount'])
        # response = InitiateTransactionResponse()
        # response.set_body(respbody)
        # response.set_body(respbody)
        return request_response
        

    