from enum import Enum
from package.utils import *

from package.myClass import myClass
class slamMap(myClass):
	
	@classmethod
	def getClassAssociation(cls):
		from package.dock import dock

		return {
		dock:	(cardinalityType.ZeroOne,	cardinalityType.ExactlyOne),
		}
	
	@classmethod	
	def getClassExtent(cls):
		from package.slamMap import slamMapExtent
		return slamMapExtent
	
	def __init__(self, confidentLevel, dock, inheritanceExtentClassList=[]):
		#Non-empty parameters
		self.confidentLevel = confidentLevel
		if not self.verifyDock(dock):
			return

		#Non-empty parameters verified
		inheritanceExtentClassList.append(slamMapExtent)
		super().__init__(inheritanceExtentClassList)
		self.addToChildExtent()

		#object attributes
		self.addLink(cardinalityType.ZeroOne,	cardinalityType.ExactlyOne, dock)
		dock.setSlamMap(self)

	def getConfidentLevel(self):
		return self.confidentLevel
	
	def verifyDock(self,inst):
		from package.dock import dock , dockExtent
		if not isinstance(inst,dock):
			print(f"Error on {self} and {dock}")
			print(f"{inst} is not instance of {dock.__name__}")
			return False
		id = inst.getID()
		#check if exist in extent
		if not dockExtent.getInstance(id):
			print(f"Error on {self} and {inst}")
			print(f"Object ID is not in the extent, {id}")
			return False
		return True

from package.classExtent import *
class slamMapExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		return slamMap