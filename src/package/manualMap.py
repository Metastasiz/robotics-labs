from enum import Enum
from package.utils import *

from package.myClass import myClass
class manualMap(myClass):
	
	@classmethod
	def getClassAssociation(cls):
		from package.dock import dock

		return {
		dock:	(cardinalityType.ZeroOne,	cardinalityType.ZeroMore),
		}
	
	@classmethod	
	def getClassExtent(cls):
		from package.manualMap import manualMapExtent
		return manualMapExtent
	
	def __init__(self, message, inheritanceExtentClassList=[]):
		#Non-empty parameters
		self.message = message

		#Non-empty parameters verified
		inheritanceExtentClassList.append(manualMapExtent)
		super().__init__(inheritanceExtentClassList)
		self.addToChildExtent()

		#object attributes

	def getMessage(self):
		return self.message


from package.classExtent import *
class manualMapExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		return manualMap