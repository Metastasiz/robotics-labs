from enum import Enum
from package.utils import *

from package.myClass import myClass
from package.childUser import childUser
class childLogActivity(myClass):
	
	@classmethod
	def getClassAssociation(cls):
		from package.notification import notification

		return {
		notification:	(cardinalityType.ZeroOne,	cardinalityType.ExactlyOne),
		}
	
	@classmethod	
	def getClassExtent(cls):
		from package.manualMapExtent import childLogActivityExtent
		return childLogActivityExtent
	
	def __init__(self, child: childUser, inheritanceExtentClassList=[]):
		#Non-empty parameters
		self.childUser = child

		#Non-empty parameters verified
		inheritanceExtentClassList.append(childLogActivityExtent)
		super().__init__(inheritanceExtentClassList)
		self.addToChildExtent()

		#object attributes

	def getChildUser(self):
		return self.childUser
	
	def verifyUser(self,inst):
		from package.childUser import childUser
		from package.user import userExtent
		if not isinstance(inst,childUser):
			print(f"Error on {self} and {childUser}")
			print(f"{inst} is not instance of {childUser.__name__}")
			return False
		id = inst.getID()
		#check if exist in extent
		if not userExtent.getInstance(id):
			print(f"Error on {self} and {inst}")
			print(f"Object ID is not in the extent, {id}")
			return False
		return True

from package.classExtent import *
class childLogActivityExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		return childLogActivity