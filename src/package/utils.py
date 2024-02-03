import string
import random
from enum import Enum
from collections import defaultdict


def idNumGenerator(size = 10, chars=string.digits):
    return "".join(random.choice(chars) for _ in range(size))

def idGenerator(size = 10, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

class cardinalityType(Enum):
    ExactlyOne = "e1"
    ZeroOne = "01"
    ZeroMore = "0m"
    OneMore = "1m"

class fakeStatus(Enum):
		online = 1
		offline = 0
              
class alertType(Enum):
		low = 0
		high = 1

class mapType(Enum):
        manual = 0
        slam = 1