from package.drone import drone, droneExtent
from package.dock import dock, dockExtent
from package.storage import storage, alertExtent
from package.recording import recording, recordingExtent

from package.utils import *
from datetime import datetime


drone1 = drone(123)
drone2 = drone(123)
storage1 = storage(123)
storage2 = storage(123)

record1 = recording(datetime.now(),drone1,storage1)

#record1.addLink(cardinalityType.ZeroMore,	cardinalityType.OneMore,storage2)
record1.addLinkById(storage,[storage2.getID()])
record1.addLinkById(drone,[drone2.getID()])