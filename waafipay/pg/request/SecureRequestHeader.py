from waafipay.pg.request.RequestHeader import RequestHeader
from waafipay.pg.utils.stringUtil import make_string, equals


class SecureRequestHeader(RequestHeader):

    def __init__(self):
        super(SecureRequestHeader, self).__init__()
        self.clientId = None
        self.signature = None

    def set_signature(self, signature):
        self.signature = signature

    def get_signature(self):
        return self.signature

    def set_client_id(self, client_id):
        self.clientId = client_id

    def get_client_id(self):
        return self.clientId

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
