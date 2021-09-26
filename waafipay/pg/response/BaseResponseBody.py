from waafipay.pg.request.ExtraParameterMap import ExtraParameterMap
from waafipay.pg.response.ResultInfo import ResultInfo
from waafipay.pg.utils.stringUtil import make_string, equals


class BaseResponseBody(ExtraParameterMap):

    def __init__(self):
        self.resultInfo = ResultInfo()
        super(BaseResponseBody, self).__init__()

    def get_result_info(self):
        return self.resultInfo

    def set_result_info(self, result_info):
        self.resultInfo = result_info

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
