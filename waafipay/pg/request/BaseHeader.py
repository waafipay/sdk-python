from waafipay.pg.utils.stringUtil import make_string, equals


class BaseHeader(object):

    def __init__(self):
        self.version = None
        self.channelId = None

    def set_version(self, version):
        self.version = version

    def get_version(self):
        return self.version

    def get_channel_id(self):
        return self.channelId

    def set_channel_id(self, channel_id):
        self.channelId = channel_id

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)


