from waafipay.pg.utils.stringUtil import make_string, equals


class PaymentMode:

    def __init__(self, mode):
        self.channels = None
        self.mode = mode

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode

    def set_channels(self, channels):
        self.channels = channels

    def get_channels(self):
        return self.channels

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)

    def __repr__(self):
        return make_string(self)
