from waafipay.VERSION import package_version


class LibraryConstants:
    """ Below constants are used in API calling
    """
    SCHEMA_VERSION = '1.0'
    VERSION = "v1"
    DATE_FORMAT = "yyyy.MM.dd.HH.mm.ss z"
    STAGING_ENVIRONMENT = "STAGE"
    PRODUCTION_ENVIRONMENT = "PROD"

    """Status message can be returned in case of Api Success"""
    SUCCESS_STATUS = "S"
    PENDING_STATUS = "PENDING"
    TXN_SUCCESS_STATUS = "TXN_SUCCESS"
    """Test String used in API callings"""
    TRUE_TEXT = 'true'
    FALSE_TEXT = 'false'
    MID_TEXT = 'mid'
    ORDER_ID_TEXT = 'orderId'
    CONTENT_TYPE_TEXT = 'Content-Type'
    APPLICATION_JSON_TEXT = 'application/json'
    UTF_8_TEXT = 'UTF-8'
    SUCCESS_TEXT = 'SUCCESS'
    HEAD_TEXT = 'head'
    BODY_TEXT = 'body'
    SIGNATURE_TEXT = 'signature'
    PYTHON_SDK_TEXT = "PYTHON-SDK"
    X_REQUEST_ID = "X-Request-ID"
    """below text as these are used input name for redirection
    flow in process transaction api calling"""
    
    # this jsp is used in redirection flow
    REQUEST_TYPE_PREAUTHORIZE = "API_PREAUTHORIZE"
    REQUEST_TYPE_PREAUTHCOMMIT = "API_PREAUTHORIZE_COMMIT"
    REQUEST_TYPE_PREAUTHCANCEL = "API_PREAUTHORIZE_CANCEL"
    REQUEST_TYPE_CANCELPURCHASE = "API_CANCELPURCHASE"
    REQUEST_TYPE_REFUND = "API_REFUND"
    REQUEST_TYPE_GETRESULTINFO = "HPP_GETRESULTINFO"
    MEDIA_TYPE_JSON = "application/json; charset=utf-8"

    PYTHON_SDK_VERSION = package_version

