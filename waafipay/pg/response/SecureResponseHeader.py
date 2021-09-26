from waafipay.pg.response.ResponseHeader import ResponseHeader
from waafipay.pg.utils.stringUtil import make_string, equals


class SecureResponseHeader(ResponseHeader):

    def __init__(self):
        self.clientId = None
        self.signature = None
        super(SecureResponseHeader, self).__init__()

    def get_client_id(self):
        return self.clientId

    def set_client_id(self, client_id):
        self.clientId = client_id

    def get_signature(self):
        return self.signature

    def set_signature(self, signature):
        self.signature = signature

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
