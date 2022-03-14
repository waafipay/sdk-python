import logging

from waafipay.pg.constants.LibraryConstants import LibraryConstants


class MerchantProperty:
    """This class is used to store all the merchant related constants that are
     common to all payments and orders
    """
    """This is true if merchant initialized the required parameter
    which is set by calling initialize method of this class.
    """
    is_initialized = False

    environment = LibraryConstants.STAGING_ENVIRONMENT

    """timeout constants in seconds default"""
    connect_timeout = 30
    read_timeout = 80

    """providing key and merchant id"""
    apiUserId = None
    merchantUid = None
    apiKey = None
    redirecturlsuc = None
    redirecturlfail = None
    

    """callback url on which waafipay will respond for api calls"""
    callback_url = ""

    initiate_txn_url = "https://sandbox.safarifoneict.com/asm"
    
    """Logging instance 
    Used for logging information according to set level which can be changed while initializing parameter of merchant
    """
    logger = logging.getLogger("Waafipay")
    log_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(name)s: %(levelname)s: %(message)s")
    log_handler.setFormatter(formatter)
    logger_disable = True
    logging_level = logging.DEBUG
    request_id = ""

    @classmethod
    def set_logger_name(cls, request_id):
        cls.logger.name = "Waafipay " + request_id
        cls.request_id = request_id

    @classmethod
    def get_redirecturlsuc(cls):
        return cls.redirecturlsuc

    @classmethod
    def set_redirecturlsuc(cls, redirecturlsuc):
        cls.redirecturlsuc = redirecturlsuc

    @classmethod
    def get_redirecturlfail(cls):
        return cls.redirecturlfail

    @classmethod
    def set_redirecturlfail(cls, redirecturlfail):
        cls.redirecturlfail = redirecturlfail

    @classmethod
    def get_apiUserId(cls):
        return cls.apiUserId

    @classmethod
    def set_apiUserId(cls, apiUserId):
        cls.apiUserId = apiUserId

    @classmethod
    def get_environment(cls):
        return cls.environment

    @classmethod
    def set_log_handler(cls, handler):
        if type(handler) is type(logging.StreamHandler()) or str(type(handler)) == str("<class 'logging.FileHandler'>"):
            cls.log_handler = handler

    @classmethod
    def set_logging_disable(cls, logger_disable):
        if type(logger_disable) is bool:
            cls.logger_disable = logger_disable

    @classmethod
    def set_logging_level(cls, logging_level):
        if type(logging_level) is type(cls.logging_level):
            cls.logging_level = logging_level

    @classmethod
    def initialize(cls, environment, apiUserId, merchantUid, apiKey):
        """
        :param environment:
        :param apiUserId:
        :param merchantUid:
        :param apiKey:
        :return:
        """
        cls.is_initialized = True

        """initiate logger"""
        cls.logger.setLevel(cls.logging_level)
        cls.logger.addHandler(cls.log_handler)
        cls.logger.disabled = cls.logger_disable

        cls.set_environment(environment)
        cls.set_apiUserId(apiUserId)
        cls.set_merchantUid(merchantUid)
        cls.set_apiKey(apiKey)

    @classmethod
    def hppinitialize(cls, environment, apiUserId, merchantUid, apiKey, redirecturlsuc, redirecturlfail):
        """
        :param environment:
        :param apiUserId:
        :param merchantUid:
        :param apiKey:
        :return:
        """
        cls.is_initialized = True

        """initiate logger"""
        cls.logger.setLevel(cls.logging_level)
        cls.logger.addHandler(cls.log_handler)
        cls.logger.disabled = cls.logger_disable

        cls.set_environment(environment)
        cls.set_apiUserId(apiUserId)
        cls.set_merchantUid(merchantUid)
        cls.set_apiKey(apiKey)
        cls.set_redirecturlfail(redirecturlfail)
        cls.set_redirecturlsuc(redirecturlsuc)

    @classmethod
    def set_merchantUid(cls, merchantUid):
        cls.merchantUid = merchantUid

    @classmethod
    def get_merchantUid(cls):
        return cls.merchantUid
		
    @classmethod
    def get_connect_timeout(cls):
        return cls.connect_timeout

    @classmethod
    def set_connect_timeout(cls, connect_timeout):
        cls.connect_timeout = connect_timeout

    @classmethod
    def set_read_timeout(cls, read_timeout):
        cls.read_timeout = read_timeout

    @classmethod
    def get_read_timeout(cls):
        return cls.read_timeout

    @classmethod
    def set_timeout(cls, connect_timeout, read_timeout):
        cls.connect_timeout = connect_timeout
        cls.read_timeout = read_timeout

    @classmethod
    def set_environment(cls, environment):
        cls.environment = environment
        if cls.environment == LibraryConstants.PRODUCTION_ENVIRONMENT:
            cls.initiate_txn_url = "https://sandbox.safarifoneict.com/asm"

    @classmethod
    def set_apiKey(cls, apiKey):
        cls.apiKey = apiKey

    @classmethod
    def get_apiKey(cls):
        return cls.apiKey


    @classmethod
    def get_initiate_txn_url(cls):
        return cls.initiate_txn_url

