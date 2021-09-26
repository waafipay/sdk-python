from waafipay.merchant.models.Time import current_time_millis
from waafipay.pg.constants.LibraryConstants import LibraryConstants
from waafipay.pg.utils.stringUtil import make_string, equals


class ResponseHeader(object):

    def __init__(self):
        self.responseTimestamp = current_time_millis()
        self.version = LibraryConstants.VERSION

    def get_response_time_stamp(self):
        return self.responseTimestamp

    def set_response_time_stamp(self, response_time_stamp):
        self.responseTimestamp = response_time_stamp

    def get_version(self):
        return self.version

    def set_version(self, version):
        self.version = version

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
