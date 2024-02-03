from datetime import datetime
from package.utils import *

from package.myClass import myClass
class recording(myClass):
	
	@classmethod
	def getClassAssociation(cls):
		from package.storage import storage
		from package.drone import drone

		return {
		storage:	(cardinalityType.ZeroMore,	cardinalityType.OneMore),
		drone:		(cardinalityType.ZeroMore,	cardinalityType.ExactlyOne),
		}
	
	@classmethod	
	def getClassExtent(cls):
		from package.recording import recordingExtent
		return recordingExtent
	
	def __init__(self, datetime: datetime, drone, storage, inheritanceExtentClassList=[]):
		#Non-empty parameters
		self.__datetime = datetime
		if not self.verifyStorage(storage):
			return
		if not self.verifyDrone(drone):
			return
		
		#Non-empty parameters verified
		inheritanceExtentClassList.append(recordingExtent)
		super().__init__(inheritanceExtentClassList)
		self.addToChildExtent()

		#object attributes
		self.addLink(cardinalityType.ZeroMore,	cardinalityType.OneMore, storage)
		self.addLink(cardinalityType.ZeroMore,	cardinalityType.ExactlyOne, drone)

	def getDatetime(self):
		return self.__datetime

	def getVersion(self):
		return self.__datetime
        
	def verifyStorage(self,inst):
		from package.storage import storage, alertExtent
		if not isinstance(inst,storage):
			print(f"Error on {self} and {storage}")
			print(f"{inst} is not instance of {storage.__name__}")
			return False
		id = inst.getID()
		#check if exist in extent
		if not alertExtent.getInstance(id):
			print(f"Error on {self} and {inst}")
			print(f"Object ID is not in the extent, {id}")
			return False
		return True
	
	def verifyDrone(self,inst):
		from package.drone import drone, droneExtent
		if not isinstance(inst,drone):
			print(f"Error on {self} and {drone}")
			print(f"{inst} is not instance of {drone.__name__}")
			return False
		id = inst.getID()
		#check if exist in extent
		if not droneExtent.getInstance(id):
			print(f"Error on {self} and {inst}")
			print(f"Object ID is not in the extent, {id}")
			return False
		return True


from package.classExtent import *
class recordingExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		return recording