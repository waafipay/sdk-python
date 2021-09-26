from waafipay.pg.utils.stringUtil import make_string, equals


class SDKResponse:

    response_object = None
    json_response = None

    def __init__(self):
        self.response_object = None
        self.json_response = None

    def get_response_object(self):
        return self.response_object

    def get_json_response(self):
        return self.json_response

    def set_response_object(self, response_object):
        self.response_object = response_object
        return self

    def set_json_response(self, json_response):
        self.json_response = json_response
        return self

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
