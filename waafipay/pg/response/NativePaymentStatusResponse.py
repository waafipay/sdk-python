from waafipay.pg.response.NativePaymentStatusResponseBody import NativePaymentStatusResponseBody
from waafipay.pg.response.SecureResponseHeader import SecureResponseHeader
from waafipay.pg.utils.stringUtil import make_string, equals


class NativePaymentStatusResponse:

    def __init__(self):
        self.head = SecureResponseHeader()
        self.body = NativePaymentStatusResponseBody()

    def set_head(self, head):
        self.head = head

    def set_body(self, body):
        self.body = body

    def get_head(self):
        return self.head

    def get_body(self):
        return self.body

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
