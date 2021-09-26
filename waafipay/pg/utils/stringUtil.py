"""This file has functionality regarding dunder function which is used many times
"""


def make_string(arg):
    """Used to overload Dunder method __str__ of any class
    This is used to convert <class 'class_name'> to string form and this is also a valid json
    :param arg: arg ~ self, iterate over it and form key-value {attribute: value}
    :return: string value of self(arg) of any class
    """
    res = str()
    is_first = True
    for k, v in arg.__dict__.items():
        if v is not None and v is not "":
            if not is_first:
                res += ','
            if v.__str__()[0] == '{' or v.__str__()[0] == '[':
                res += '"{}":{}'.format(k, v)
            else:
                res += '"{}":"{}"'.format(k, v)
            is_first = False
    if is_first:
        return None
    return '{' + res + '}'


def equals(first, second):
    """
    used to overload Dunder method __eq__ of any class
    Compare equality of first and second
    :param first: self of one object
    :param second: self of other object
    :return: True if all attributes value are same otherwise False
    """
    for k, v in first.__dict__.items():
        if not hasattr(second, k) or v != second.__dict__[k]:
            return False
    for k, v in second.__dict__.items():
        if not hasattr(first, k) or v != first.__dict__[k]:
            return False
    return True


def is_empty(obj):
    """
    check for "", "   " and None
    :param obj:data to be tested
    :return: True if it is one of "" or "  " or None otherwise False
    """
    if not obj or not obj.strip():
        return True
    else:
        return False


def format_string(string):
    string = str(string)
    return string.replace('\'', '\"').replace(' ', '')
