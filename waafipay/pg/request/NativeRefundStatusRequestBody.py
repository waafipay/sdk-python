from waafipay.pg.utils.stringUtil import make_string, equals


class NativeRefundStatusRequestBody:

    def __init__(self):
        self.mid = None
        self.orderId = None
        self.refId = None

    def set_mid(self, mid):
        self.mid = mid
        return self

    def get_mid(self):
        return self.mid

    def set_order_id(self, order_id):
        self.orderId = order_id
        return self

    def get_order_id(self):
        return self.orderId

    def set_ref_id(self, ref_id):
        self.refId = ref_id
        return self

    def get_ref_id(self):
        return self.refId

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
