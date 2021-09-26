from waafipay.pg.request.BaseHeader import BaseHeader
from waafipay.pg.utils.stringUtil import make_string, equals


class RequestHeader(BaseHeader):

    def __init__(self):
        super(RequestHeader, self).__init__()
        self.requestTimestamp = None

    def set_request_timestamp(self, request_timestamp):
        self.requestTimestamp = request_timestamp

    def get_request_timestamp(self):
        return self.requestTimestamp

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)

