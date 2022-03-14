from waafipay.pg.utils.stringUtil import make_string, equals
import time


class InitiateHppTransactionResponseBody:

    def __init__(self):
        self.serviceName = None
        self.hppResultToken = None
        self.channelName = None
        self.schemaVersion = None
        self.requestId = None
        self.serviceParams = None
        self.timestamp = None

    def set_timestamp(self, timestamp):
        self.timestamp = int(time.time())

    def get_timestamp(self):
        return self.timestamp

    def set_hppResultToken(self, hppResultToken):
        self.hppResultToken = hppResultToken

    def get_hppResultToken(self):
        return self.hppResultToken
	
    def set_serviceName(self, serviceName):
        self.serviceName = serviceName

    def get_serviceName(self):
        return self.serviceName

    def setschemaVersion(self, schemaVersion):
        self.schemaVersion = schemaVersion

    def get_schemaVersion(self):
        return self.schemaVersion


    def setrequestId(self, requestId):
        self.requestId = requestId

    def get_requestId(self):
        return self.requestId


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
