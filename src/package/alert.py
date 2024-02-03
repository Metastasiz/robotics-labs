from enum import Enum
from package.utils import *

from package.myClass import myClass
class alert(myClass):
	
	@classmethod
	def getClassAssociation(cls):
		from package.notification import notification

		return {
		notification:	(cardinalityType.ZeroOne,	cardinalityType.ExactlyOne),
		}
	
	@classmethod	
	def getClassExtent(cls):
		from package.alert import alertExtent
		return alertExtent
	
	def __init__(self, alert: alertType, inheritanceExtentClassList=[]):
		#Non-empty parameters
		self.alert = alert

		#Non-empty parameters verified
		inheritanceExtentClassList.append(alertExtent)
		super().__init__(inheritanceExtentClassList)
		self.addToChildExtent()

		#object attributes

	def getAlert(self):
		return self.alert

from package.classExtent import *
class alertExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		return alert