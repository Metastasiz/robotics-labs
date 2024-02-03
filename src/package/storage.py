from enum import Enum
from package.utils import *

class storageType(Enum):
		local = 0
		cloud = 1

from package.myClass import myClass
class storage(myClass):
	
	@classmethod
	def getClassAssociation(cls):
		from package.recording import recording

		return {
		recording:	(cardinalityType.OneMore,	cardinalityType.ZeroMore),
		}
	
	@classmethod	
	def getClassExtent(cls):
		from package.storage import alertExtent
		return alertExtent
	
	def __init__(self, capacity, inheritanceExtentClassList=[]):
		#Non-empty parameters
		self.__capacity = None
		self.setCapacity(capacity)

		#Non-empty parameters verified
		inheritanceExtentClassList.append(alertExtent)
		super().__init__(inheritanceExtentClassList)
		self.addToChildExtent()

		#object attributes
		self.storageType = storageType.local

	def setStorageType(self, type: storageType):
		self.storageType = type
	def getStorageType(self):
		return self.storageType

	def setCapacity(self,version):
		self.__capacity = version

	def getCapacity(self):
		return self.__capacity
	
	def getSortedRecording(self):
		from package.recording import recording, recordingExtent
		cardinality = self.__class__.getClassAssociation()[recording]
		return self.getLinkDict()[recording].sort(key=lambda x: recordingExtent.getInstance(x).getDatetime())

from package.classExtent import *
class alertExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		return storage