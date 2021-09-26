from waafipay.pg.response.AsyncRefundResponseBody import AsyncRefundResponseBody
from waafipay.pg.response.SecureResponseHeader import SecureResponseHeader
from waafipay.pg.utils.stringUtil import make_string, equals


class AsyncRefundResponse:

    head = None
    body = None

    def __init__(self):
        self.head = SecureResponseHeader()
        self.body = AsyncRefundResponseBody()

    def get_head(self):
        return self.head

    def set_head(self, head):
        self.head = head

    def get_body(self):
        return self.body

    def set_body(self, body):
        self.body = body

    def __str__(self):
        return make_string(self)

    def __setattr__(self, key, value):
        if not hasattr(self, key):
            raise AttributeError(" Can not be set ".format(key))
        self.__dict__[key] = value

    def __eq__(self, other):
        return equals(self, other)


