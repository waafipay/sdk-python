from waafipay.pg.utils.stringUtil import make_string, equals


class ExtraParameterMap(object):

    def __init__(self):
        # str to object
        self.extraParamsMap = None

    def get_extra_parameter_map(self):
        return self.extraParamsMap

    def set_extra_parameter_map(self, extra_param_map):
        self.extraParamsMap = extra_param_map
        return self

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)

