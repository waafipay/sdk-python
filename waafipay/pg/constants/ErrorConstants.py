class ErrorConstants:
    """This class is used to store error constants Merchant can update these
    constants according to his need
    """

    UTILITY_CLASS_EXCEPTION = "Utility class cannot be instantiated"

    def __init__(self):
        raise Exception(self.UTILITY_CLASS_EXCEPTION)

    """Result Status In case of Failure"""
    FAILURE = "failure"

    class ErrorMessage:
        """Result messages in case of failure"""
        def __init__(self):
            raise Exception(ErrorConstants.UTILITY_CLASS_EXCEPTION)

        """Result message when verify signature returns false"""
        SIGNATURE_VALIDATION_FAILED = "Signature Validation Failed"

        """Result message when verify signature returns exception"""
        VALIDATE_SIGNATURE_EXCEPTION = "Validate Signature Exception"

        """Result message when verify signature returns exception"""
        GENERATE_SIGNATURE_EXCEPTION = "Generate Signature Exception"

        """Result message when any required parameter is missing in api calling"""
        MISSING_MANDATORY_PARAMETERS = "Missing Mandatory Parameters"

        """ Result message when Transaction token is missing if required in api """
        MISSING_TRANSACTION_TOKEN = "Missing Transaction Token"

        """ Result message when Merchant Property are not initialized """
        MISSING_MERCHANT_PROPERTY = "Missing Merchant Property"

        """ Result message when String to object conversion failed """
        JSONSTRING_TO_OBJECT_CONVERSION_FAILED = "JsonString to object conversion failure"

        """ Result message when Object to string conversion failed """
        OBJECT_TO_JSONSTRING_CONVERSION_FAILED = "Object to JsonString conversion failure"

    class ErrorCode:

        def __init__(self):
            raise Exception(ErrorConstants.UTILITY_CLASS_EXCEPTION)

        """Result code in case of failure"""
        DEFAULT = "501"
