from waafipay.pg.utils.stringUtil import make_string, equals


class InitiateTransactionRequest:

    def get_head(self):
        return self.head

    def set_head(self, head):
        self.head = head
        return self

    def get_body(self):
        return self.body

    def set_body(self, body):
        self.body = body
        return self

    def __init__(self):
        self.head = None
        self.body = None

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
