from package.utils import *

from package.user import user
class parentUser(user):

	@classmethod
	def getClassAssociation(cls):
		from package.drone import drone
		from package.dock import dock
		from package.notification import notification
		
		return {
		drone:			(cardinalityType.ZeroOne,	cardinalityType.ZeroMore),
		dock:			(cardinalityType.ZeroOne,	cardinalityType.ZeroMore),
		user:			(cardinalityType.ZeroOne,	cardinalityType.ZeroMore),
		notification:	(cardinalityType.ExactlyOne,cardinalityType.ZeroMore)
		}
	
	def __init__(self, name, inheritanceExtentClassList=[]):
		#Non-empty parameters

		#Non-empty parameters verified
		super().__init__(name, inheritanceExtentClassList)

		#object attributes

	#for self link
	def getSelfLinkType(self):
		from package.childUser import childUser
		return childUser