from waafipay.pg.utils.stringUtil import make_string, equals


class ResultInfo:

    def __init__(self):
        self.isRedirect = None
        self.resultMsg = None
        self.resultCode = None
        self.resultStatus = None

    def get_result_status(self):
        return self.resultStatus

    def set_result_status(self, result_status):
        self.resultStatus = result_status

    def set_result_code(self, result_code):
        self.resultCode = result_code

    def get_result_code(self):
        return self.resultCode

    def set_result_msg(self, result_msg):
        self.resultMsg = result_msg

    def get_result_msg(self):
        return self.resultMsg

    def is_redirect(self):
        return self.isRedirect

    def set_redirect(self, is_redirect):
        self.isRedirect = is_redirect

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
