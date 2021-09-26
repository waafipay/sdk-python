from waafipay.pg.response.BaseResponseBody import BaseResponseBody
from waafipay.pg.utils.stringUtil import make_string, equals


class InitiateTransactionResponseBody(BaseResponseBody):

    def __init__(self):
        super(InitiateTransactionResponseBody, self).__init__()
        self.schemaVersion = None
        self.timestamp = None
        self.requestId = None
        self.responseCode = None
        self.responseMsg = None
        self.errorCode = None
        self.transactionId = None
        self.referenceId = None
        self.state = None
        self.description = None
        self.txAmount = None

    def set_schemaVersion(self, schemaVersion):
        self.schemaVersion = schemaVersion

    def get_schemaVersion(self):
        return self.schemaVersion

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def get_timestamp(self):
        return self.timestamp

    def set_requestId(self, requestId):
        self.requestId = requestId

    def get_requestId(self):
        return self.requestId

    def set_responseCode(self, responseCode):
        self.responseCode = responseCode

    def get_responseCode(self):
        return self.responseCode
		
    def set_responseMsg(self, responseMsg):
        self.responseMsg = responseMsg

    def get_responseMsg(self):
        return self.responseMsg

    def set_errorCode(self, errorCode):
        self.errorCode = errorCode

    def get_errorCode(self):
        return self.errorCode

    def set_transactionId(self, transactionId):
        self.transactionId = transactionId

    def get_transactionId(self):
        return self.transactionId
		
    def set_referenceId(self, referenceId):
        self.referenceId = referenceId

    def get_referenceId(self):
        return self.referenceId
		
    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state
		
    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
		
    def set_txAmount(self, txAmount):
        self.txAmount = txAmount

    def get_txAmount(self):
        return self.txAmount

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
