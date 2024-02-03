from datetime import datetime
from package.utils import *

from package.myClass import myClass
from package.manualMapExtent import childLogActivity
from package.alert import alert
class notification(myClass):
	
	@classmethod
	def getClassAssociation(cls):
		from package.user import user
		from package.alert import alert
		from package.manualMapExtent import childLogActivity

		return {
		user:				(cardinalityType.ZeroMore,	cardinalityType.ExactlyOne),
		alert:				(cardinalityType.ExactlyOne,	cardinalityType.ZeroOne),
		childLogActivity:	(cardinalityType.ExactlyOne,	cardinalityType.ZeroOne),
		}
	
	@classmethod	
	def getClassExtent(cls):
		from package.notification import notificationExtent
		return notificationExtent
	
	def __init__(self, datetime: datetime, user, childLog: childLogActivity = None, ale: alert =None, inheritanceExtentClassList=[]):
		#Non-empty parameters
		self.__datetime = datetime
		if not self.verifyUser(user):
			return
		
		#for overlapping - complete
		if childLog == None and ale == None:
			print(f"{self.__class__.__name__} must have at least one of either {childLogActivity.__name__} or {alert.__name__}")
			return

		#Non-empty parameters verified
		inheritanceExtentClassList.append(notificationExtent)
		super().__init__(inheritanceExtentClassList)
		self.addToChildExtent()

		#object attributes
		if childLog != None:
			if not self.addLink(cardinalityType.ExactlyOne,	cardinalityType.ZeroOne, childLog):
				self.__class__.getClassExtent().removeInstance(self.getID())
				return
		if ale != None:
			if not self.addLink(cardinalityType.ExactlyOne,	cardinalityType.ZeroOne, ale):
				self.__class__.getClassExtent().removeInstance(self.getID())
				return 
		self.addLink(cardinalityType.ZeroMore,	cardinalityType.ExactlyOne, user)
	
	def verifyUser(self,inst):
		from package.user import user, userExtent
		if not isinstance(inst,user):
			print(f"Error on {self} and {user}")
			print(f"{inst} is not instance of {user.__name__}")
			return False
		id = inst.getID()
		#check if exist in extent
		if not userExtent.getInstance(id):
			print(f"Error on {self} and {inst}")
			print(f"Object ID is not in the extent, {id}")
			return False
		return True


from package.classExtent import *
class notificationExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		return notification