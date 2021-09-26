import json

from waafipay.pg.constants.ErrorConstants import ErrorConstants
from waafipay.pg.SDKException import SDKException
from waafipay.pg.constants.MerchantProperty import MerchantProperty


class JsonToObject:
    """Used to put received response (by posting request) into corresponding object
    """

    def __init__(self, arg, obj):
        """
        :param arg: this is <class 'dict'> or str which is called by Request.py for putting these value in obj
        :param obj: Response object in which value of arg to be putted
        """
        if type(arg) is str:
            arg = json.loads(arg)
        self.convert_json(arg, obj)

    def convert_json(self, arg, obj):
        """This method iterate over arg if it is list or dict
        and set the value of corresponding attribute
        :param arg: dict form of data
        :param obj: arg is putted into obj recursively
        :return: void or raise exception if attribute is not correct
        """
        self.__dict__ = {}
        for key, value in arg.items():
            if type(value) is dict:
                value = JsonToObject(value, getattr(obj, key))
            elif hasattr(obj, key):
                    obj.__dict__[key] = value
            else:
                MerchantProperty.logger.debug(
                    "ConverterUtil :: convert json :: key:{} with value:{} is not a valid attribute".format(key, value))
                # raise SDKException.get_sdk_exception_with_json_data(
                #    ErrorConstants.ErrorMessage.JSONSTRING_TO_OBJECT_CONVERSION_FAILED, str(arg))
            self.__dict__[key] = value
