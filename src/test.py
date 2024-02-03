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

from package.utils import *
from datetime import datetime

#droneExtent.read()
#for inst in droneExtent.getExtent().values():
#	print(inst)
#dockExtent.read()
#for inst in dockExtent.getExtent().values():
#	print(inst)

#for _ in range(5):
#	dock(idNumGenerator(3))
#dockExtent.write()
#
#for _ in range(5):
#	drone(idNumGenerator(3))
#droneExtent.write()

for _ in range(3):
	childUser(idNumGenerator(3))
childUser1 = childUser(123)
childUser2 = childUser(456)

for _ in range(4):
	parentUser(idNumGenerator(3))
parentUser1 = parentUser(123)

for inst in userExtent.getExtent().values():
	print(inst)
userExtent.write()
userExtent.clearExtent()
print(len(userExtent.getExtent().values()))
userExtent.read()
for inst in userExtent.getExtent().values():
	print(inst)


childUser1.addLink(cardinalityType.ZeroMore,	cardinalityType.ZeroOne, parentUser1)
print("EXPECTED ERROR")
childUser1.addLink(cardinalityType.ZeroMore,	cardinalityType.ZeroOne, childUser2)
print()

childLog1 = childLogActivity(childUser1)
childLog2 = childLogActivity(childUser1)
alert1 = alert(alertType.low)
alert2 = alert(alertType.low)

noti1 = notification(datetime.now(), parentUser1, childLog=childLog1)
noti2 = notification(datetime.now(), parentUser1, ale=alert1)
noti3 = notification(datetime.now(), parentUser1, childLog=childLog1, ale=alert1)
noti4 = notification(datetime.now(), parentUser1, childLog=childLog2, ale=alert2)

print("===")
print(parentUser1.getLinkDict())