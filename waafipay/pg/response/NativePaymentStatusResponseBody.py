from waafipay.pg.response.BaseResponseBody import BaseResponseBody
from waafipay.pg.response.ChildTransaction import ChildTransaction
from waafipay.pg.utils.stringUtil import make_string, equals


class NativePaymentStatusResponseBody(BaseResponseBody):

    def __init__(self):
        self.customMerchantResponse = None
        self.customChecksumString = None
        self.txnId = None
        self.bankTxnId = None
        self.orderId = None
        self.txnAmount = None
        self.txnType = None
        self.gatewayName = None
        self.bankName = None
        self.mid = None
        self.paymentMode = None
        self.refundAmt = None
        self.txnDate = None
        self.refundId = None
        self.refId = None
        self.childTransaction = None
        self.subsId = None
        self.merchantUniqueReference = None
        self.blockedAmount = None
        self.preAuthId = None
        self.maskedCardNo = None
        self.cardIndexNo = None
        self.maskedCustomerMobileNumber = None
        self.posId = None
        self.uniqueReferenceLabel = None
        self.uniqueReferenceValue = None
        self.pccCode = None
        self.prn = None
        self.udf1 = None
        self.udf2 = None
        self.udf3 = None
        self.comments = None
        self.currentTxnCount = None
        self.loyaltyPoints = None
        super(NativePaymentStatusResponseBody, self).__init__()

    def set_txn_id(self, txn_id):
        self.txnId = txn_id

    def get_txn_id(self):
        return self.txnId

    def set_bank_txn_id(self, bank_txn_id):
        self.bankTxnId = bank_txn_id

    def get_bank_txn_id(self):
        return self.bankTxnId

    def set_order_id(self, order_id):
        self.orderId = order_id

    def get_order_id(self):
        return self.orderId

    def set_txn_amount(self, txn_amount):
        self.txnAmount = txn_amount

    def get_txn_amount(self):
        return self.txnAmount

    def set_txn_type(self, txn_type):
        self.txnType = txn_type

    def get_txn_type(self):
        return self.txnType

    def set_gateway_name(self, gateway_name):
        self.gatewayName = gateway_name

    def get_gateway_name(self):
        return self.gatewayName

    def set_bank_name(self, bank_name):
        self.bankName = bank_name

    def get_bank_name(self):
        return self.bankName

    def set_mid(self, mid):
        self.mid = mid

    def get_mid(self):
        return self.mid

    def set_payment_mode(self, payment_mode):
        self.paymentMode = payment_mode

    def get_payment_mode(self):
        return self.paymentMode

    def set_refund_amt(self, refund_amt):
        self.refundAmt = refund_amt

    def get_refund_amt(self):
        return self.refundAmt

    def set_txn_date(self, txn_date):
        self.txnDate = txn_date

    def get_txn_date(self):
        return self.txnDate

    def set_refund_id(self, refund_id):
        self.refundId = refund_id

    def get_refund_id(self):
        return self.refundId

    def set_ref_id(self, ref_id):
        self.refId = ref_id

    def get_ref_id(self):
        return self.refId

    def set_child_transaction(self, child_transaction):
        self.childTransaction = child_transaction

    def get_child_transaction(self):
        return self.childTransaction

    def set_subs_id(self, subs_id):
        self.subsId = subs_id

    def get_subs_id(self):
        return self.subsId

    def set_merchant_unique_reference(self, merchant_unique_reference):
        self.merchantUniqueReference = merchant_unique_reference

    def get_merchant_unique_reference(self):
        return self.merchantUniqueReference

    def set_blocked_amount(self, blocked_amount):
        self.blockedAmount = blocked_amount

    def get_blocked_amount(self):
        return self.blockedAmount

    def set_pre_auth_id(self, pre_auth_id):
        self.preAuthId = pre_auth_id

    def get_pre_auth_id(self):
        return self.preAuthId

    def set_masked_card_no(self, masked_card_no):
        self.maskedCardNo = masked_card_no

    def get_masked_card_no(self):
        return self.maskedCardNo

    def set_card_index_no(self, card_index_no):
        self.cardIndexNo = card_index_no

    def get_card_index_no(self):
        return self.cardIndexNo

    def set_masked_customer_mobile_number(self, masked_customer_mobile_number):
        self.maskedCustomerMobileNumber = masked_customer_mobile_number

    def get_masked_customer_mobile_number(self):
        return self.maskedCustomerMobileNumber

    def set_pos_id(self, pos_id):
        self.posId = pos_id

    def get_pos_id(self):
        return self.posId

    def set_unique_reference_label(self, unique_reference_label):
        self.uniqueReferenceLabel = unique_reference_label

    def get_unique_reference_label(self):
        return self.uniqueReferenceLabel

    def set_unique_reference_value(self, unique_reference_value):
        self.uniqueReferenceValue = unique_reference_value

    def get_unique_reference_value(self):
        return self.uniqueReferenceValue

    def set_pcc_code(self, pcc_code):
        self.pccCode = pcc_code

    def get_pcc_code(self):
        return self.pccCode

    def set_prn(self, prn):
        self.prn = prn

    def get_prn(self):
        return self.prn

    def set_udf1(self, udf1):
        self.udf1 = udf1

    def get_udf1(self):
        return self.udf1

    def set_udf2(self, udf2):
        self.udf2 = udf2

    def get_udf2(self):
        return self.udf2

    def set_udf3(self, udf3):
        self.udf3 = udf3

    def get_udf3(self):
        return self.udf3

    def set_comments(self, comments):
        self.comments = comments

    def get_comments(self):
        return self.comments

    def set_current_txn_count(self, current_txn_count):
        self.currentTxnCount = current_txn_count

    def get_current_txn_count(self):
        return self.currentTxnCount

    def set_loyalty_points(self, loyalty_points):
        self.loyaltyPoints = loyalty_points

    def get_loyalty_points(self):
        return self.loyaltyPoints

    def set_custom_merchant_response(self, custom_merchant_response):
        self.customMerchantResponse = custom_merchant_response

    def get_custom_merchant_response(self):
        return self.customMerchantResponse

    def set_custom_checksum_string(self, custom_checksum_string):
        self.customChecksumString = custom_checksum_string

    def get_custom_checksum_string(self):
        return self.customChecksumString

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
