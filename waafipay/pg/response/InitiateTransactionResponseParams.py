from waafipay.pg.response.BaseResponseBody import BaseResponseBody
from waafipay.pg.utils.stringUtil import make_string, equals


class InitiateTransactionResponseParams(BaseResponseBody):

    def __init__(self):
        super(InitiateTransactionResponseParams, self).__init__()
        self.transactionId = None
        self.referenceId = None
        self.state = None
        self.description = None
        self.txAmount = None

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
