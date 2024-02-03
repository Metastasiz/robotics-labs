from package.utils import *

from package.user import user
class childUser(user):

	@classmethod
	def getClassAssociation(cls):
		from package.drone import drone
		from package.dock import dock
		
		return {
		drone:		(cardinalityType.ZeroOne,	cardinalityType.ZeroMore),
		dock:		(cardinalityType.ZeroOne,	cardinalityType.ZeroMore),
		user:	(cardinalityType.ZeroMore,	cardinalityType.ZeroOne),
		}
	
	def __init__(self, name, inheritanceExtentClassList=[]):
		#Non-empty parameters

		#Non-empty parameters verified
		super().__init__(name, inheritanceExtentClassList)

		#object attributes

	#for self link
	def getSelfLinkType(self):
		from package.parentUser import parentUser
		return parentUser
