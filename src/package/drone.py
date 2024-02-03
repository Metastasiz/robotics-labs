from enum import Enum
from package.utils import *

def fakeMinServiceVersion():
	return 100

from package.myClass import myClass
class drone(myClass):
	
	@classmethod
	def getClassAssociation(cls):
		from package.dock import dock
		from package.user import user
		from package.recording import recording

		return {
		dock:		(cardinalityType.ZeroMore,	cardinalityType.ZeroMore),
		user:		(cardinalityType.ZeroMore,	cardinalityType.ZeroOne),
		recording:	(cardinalityType.ExactlyOne,cardinalityType.ZeroMore),
		}
	
	@classmethod	
	def getClassExtent(cls):
		from package.drone import droneExtent
		return droneExtent
	
	def __init__(self, version, inheritanceExtentClassList=[]):
		#Non-empty parameters
		self.__version = None
		self.setVersion(version)

		#Non-empty parameters verified
		inheritanceExtentClassList.append(droneExtent)
		super().__init__(inheritanceExtentClassList)
		self.addToChildExtent()

		#object attributes
		self.status = fakeStatus.offline
		self.minVersion = fakeMinServiceVersion()

	def setFakeStatus(self, status: fakeStatus):
		self.status = status
	def getFakeStatus(self):
		return self.status

	def setVersion(self,version):
		self.__version = version

	def getVersion(self):
		return self.__version
	
	def getRefreshMinService(self):
		self.minVersion = fakeMinServiceVersion()

	def getServiceStatus(self):
		if self.getVersion() >= self.minVersion:
			return "YES"
		return "NO"
	
	def getLiveSupport(self):
		if self.getVersion() >= self.minVersion:
			return self.getFakeConnectService()
		return self.getFakeOutOfService()
	
	def getFakeConnectService(self):
		return "Live support connected"
	
	def getFakeOutOfService(self):
		return "This drone version is out of service"
	
	def getFakeCamera(self):
		out = f"FAKE CAMERA OF\n{self}"
		return out
	
	def getSortedRecording(self):
		from package.recording import recording, recordingExtent
		cardinality = self.__class__.getClassAssociation()[recording]
		return self.getLinkDict()[recording].sort(key=lambda x: recordingExtent.getInstance(x).getDatetime())

	
from package.classExtent import *
class droneExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		return drone