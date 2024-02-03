from package.utils import *

from package.myClass import myClass
class user(myClass):

	@classmethod
	def getClassAssociation(cls):
		from package.drone import drone
		from package.dock import dock
		
		return {
		drone:	(cardinalityType.ZeroOne,	cardinalityType.ZeroMore),
		dock:	(cardinalityType.ZeroOne,	cardinalityType.ZeroMore)
		}
	
	@classmethod
	def getClassExtent(cls):
		from package.user import userExtent
		return userExtent
	
	def __init__(self, name, inheritanceExtentClassList=[]):
		#Non-empty parameters
		self.__name = None
		self.setName(name)

		#Non-empty parameters verified
		inheritanceExtentClassList.append(userExtent)
		super().__init__(inheritanceExtentClassList)
		self.addToChildExtent()

		#object attributes
		
	def setName(self,name):
		self.__name = name

	def getName(self):
		return self.__name

from package.classExtent import *
class userExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		from package.parentUser import parentUser
		from package.childUser import childUser
		return user