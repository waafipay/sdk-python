from waafipay.pg.utils.stringUtil import make_string, equals


class PayerInfo:

    def __init__(self):
        self.accountNo = None
        self.accountPwd = None
        self.accountExpDate = None
        self.accountHolder = None

    def set_accountNo(self, accountNo):
        self.accountNo = accountNo

    def get_accountNo(self):
        return self.accountNo

    def set_accountPwd(self, accountPwd):
        self.accountPwd = accountPwd

    def get_accountPwd(self):
        return self.accountPwd

    def set_accountExpDate(self, accountExpDate):
        self.accountExpDate = accountExpDate

    def get_accountExpDate(self):
        return self.accountExpDate

    def set_accountHolder(self, accountHolder):
        self.accountHolder = accountHolder

    def get_accountHolder(self):
        return self.accountHolder

    
    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
