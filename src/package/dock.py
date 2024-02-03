from package.utils import *

from package.myClass import myClass
from package.manualMap import manualMap
from package.slamMap import slamMap

class dock(myClass):

	@classmethod
	def getClassAssociation(cls):
		from package.drone import drone
		from package.user import user
		from package.manualMap import manualMap
		from package.slamMap import slamMap
		
		return {
		drone:		(cardinalityType.ZeroMore,		cardinalityType.ZeroMore),
		user:		(cardinalityType.ZeroMore,		cardinalityType.ZeroOne),
		manualMap:	(cardinalityType.ZeroMore,		cardinalityType.ZeroOne),
		slamMap:	(cardinalityType.ExactlyOne,	cardinalityType.ZeroOne),
		}
	
	@classmethod
	def getClassExtent(cls):
		from package.dock import dockExtent
		return dockExtent
	
	def __init__(self, version, map: manualMap = None, inheritanceExtentClassList=[]):
		#Non-empty parameters
		self.__version = None
		self.setVersion(version)

		#Non-empty parameters verified
		inheritanceExtentClassList.append(dockExtent)
		super().__init__(inheritanceExtentClassList)
		self.addToChildExtent()

		#object attributes
		self.status = fakeStatus.offline
		if map == None:
			map = manualMap("Auto Generated")
		self.mapType = None
		self.setManualMap(map)
		

	def setFakeStatus(self, status: fakeStatus):
		self.status = status
	def getFakeStatus(self):
		return self.status

	def setVersion(self,version):
		self.__version = version

	def getVersion(self):
		return self.__version
	
	def getMap(self):
		return self.map

	#temp solution
	def setSlamMap(self, map: slamMap):
		if self.mapType == mapType.slam and self.getMap() != None:
			self.map.deleteObject()
		if self.mapType == mapType.manual:
			self.removeLink(cardinalityType.ZeroMore,	cardinalityType.ZeroOne,self.map)
		self.mapType = mapType.slam
		self.map = map
		#links on creation

	#temp solution
	def setManualMap(self, map:manualMap):
		if self.mapType == mapType.slam and self.getMap() != None:
			self.map.deleteObject()
		if self.mapType == mapType.manual:
			self.removeLink(cardinalityType.ZeroMore,	cardinalityType.ZeroOne,self.map)
		self.mapType = mapType.manual
		self.map = map
		self.addLink(cardinalityType.ZeroMore,	cardinalityType.ZeroOne, map)


					
from package.classExtent import *
class dockExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		return dock