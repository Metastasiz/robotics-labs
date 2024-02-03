from package.drone import drone, droneExtent
from package.dock import dock, dockExtent
from package.user import user, userExtent
from package.storage import storage, alertExtent
from package.recording import recording, recordingExtent
from package.parentUser import parentUser
from package.childUser import childUser
from package.alert import alert
from package.manualMapExtent import childLogActivity, childUser
from package.notification import notification
#from package.window import mainWindow

from package.utils import *
from datetime import datetime
#mainWindow()

print("=================")

dock1 = dock(124)
drone1 = drone(123)
drone2 = drone(123)
storage1 = storage(123)
storage2 = storage(123)
parentUser1 = parentUser(123)
childUser1 = childUser(123)
childUser2 = childUser(123)

record1 = recording(datetime.now(),drone1,storage1)

record1.addLink(cardinalityType.ZeroMore,	cardinalityType.OneMore,storage2)

dock1.addLink(cardinalityType.ZeroMore,cardinalityType.ZeroMore,*[drone1,drone1])

dock1.addLink(cardinalityType.ZeroMore,cardinalityType.ZeroOne,parentUser1)
drone1.addLink(cardinalityType.ZeroMore,cardinalityType.ZeroOne,parentUser1)
drone1.addLink(cardinalityType.ZeroMore,cardinalityType.ZeroOne,childUser1)
childUser1.addLink(cardinalityType.ZeroOne,cardinalityType.ZeroMore,dock1)
childUser1.removeLink(cardinalityType.ZeroOne,cardinalityType.ZeroMore,dock1)

childUser1.addLink(cardinalityType.ZeroMore,	cardinalityType.ZeroOne, parentUser1)

childUser1.addLink(cardinalityType.ZeroMore,	cardinalityType.ZeroOne, childUser2)
print("EXPECTED ERROR\n")

childLog1 = childLogActivity(childUser1)
alert1 = alert(alertType.low)

noti1 = notification(datetime.now(), parentUser1, childLog1,ale=alert1)

#noti2 = notification(datetime.now(), parentUser1,childLog1,ale=alert1)
#print("EXPECTED ERROR\n")

for inst in userExtent.getExtent().values():
	print(inst.getDescription())

childUser1.deleteObject()
print("deleted")
for inst in userExtent.getExtent().values():
	print(inst.getDescription())
