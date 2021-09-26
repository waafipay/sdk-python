from waafipay.pg.utils.stringUtil import make_string, equals
import time

class InitiateRefundTransactionRequestBody:

    def __init__(self):
        self.serviceName = None
        self.requestId = None
        self.schemaVersion = None
        self.timestamp = None
        self.channelName = None
        self.serviceParams = None

    def setserviceName(self, serviceName):
        self.serviceName = serviceName

    def get_serviceName(self):
        return self.serviceName

    def setrequestId(self, requestId):
        self.requestId = requestId

    def get_requestId(self):
        return self.requestId

    def setschemaVersion(self, schemaVersion):
        self.schemaVersion = schemaVersion

    def get_schemaVersion(self):
        return self.schemaVersion

    def settimestamp(self, timestamp):
        self.timestamp = int(time.time())

    def get_timestamp(self):
        return self.timestamp

    def setchannelName(self, channelName):
        self.channelName = channelName

    def get_channelName(self):
        return self.channelName

    
    def setserviceParams(self, serviceParams):
        self.serviceParams = serviceParams

    def get_serviceParams(self):
        return self.serviceParams
		
    
    
    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
