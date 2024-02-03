from collections import defaultdict
from abc import ABC, abstractclassmethod, abstractmethod

from package.utils import *

from package.classExtent import classExtent
class myClass(ABC):

    @classmethod
    @abstractmethod
    def getClassAssociation(cls) -> dict:
        pass

    @classmethod
    @abstractmethod
    def getClassExtent(cls) -> classExtent:
        pass
    
    def __init__(self, inheritanceExtentClassList: list, **kwargs):
        self.inheritanceExtentClassList = inheritanceExtentClassList
        self.__id = None
        self.setID()
        self.link_dict = defaultdict(list)
        
    def deleteObject(self):
        link_dict = self.getLinkDict()
        for key in link_dict.keys():
            #get extent
            extent = key.getClassExtent()
            for id in link_dict[key]:
                inst = extent.getInstance(id)
                #delete self link
                self.link_dict[key].remove(id)
                #delete obj link
                print(inst.getLinkDict()[self.getChildClass()])
                inst.getLinkDict()[self.getChildClass()].remove(self.getID())
        self.getClassExtent().removeInstance(self.getID())

    def removeLink(self,selfCardinality: cardinalityType,objCardinality: cardinalityType,*obj):
        for inst in obj:
            if not self.verifyLink(selfCardinality,objCardinality,inst):
                continue
            id = None
            try:
                id = inst.getID()
            except:
                continue
            linkID = inst.getChildClass()
            #check if exist in link
            if id in self.link_dict[linkID]:
                #check cardinality
                #ExactlyOne / ZeroOne
                if  objCardinality == cardinalityType.ZeroOne:
                    self.link_dict[linkID].clear()
                    continue
                if (objCardinality == cardinalityType.ExactlyOne or\
                    objCardinality == cardinalityType.OneMore) and\
                    len(self.link_dict[linkID]) <= 1:
                    print(f"Error on {self} and {inst}")
                    print(f"Link must have at least 1 instance of {inst}")
                    continue
                self.link_dict[linkID].remove(id)
                #recursive
                try:
                    inst.removeLink(objCardinality,selfCardinality,self)
                except:
                    print(f"Error on {inst} and {self}")
                    print(f"Object is not instance of {myClass.__name__}")
                    break
    
    def addLinkById(self,cls,idList: list):
        obj = []
        association = self.__class__.getClassAssociation()[cls]
        for id in idList:
            inst = None
            try:
                obj.append(cls.getClassExtent().getInstance(id))
            except:
                print(f"{cls} does not inherites from myClass")
                continue
        self.addLink(association[0],association[1],*obj)

    def removeLinkById(self,cls,idList: list):
        obj = []
        association = self.__class__.getClassAssociation()[cls]
        for id in idList:
            inst = None
            try:
                obj.append(cls.getClassExtent().getInstance(id))
            except:
                print(f"{cls} does not inherites from myClass")
                continue
        self.removeLink(association[0],association[1],*obj)
    
    def addLinkByObj(self,cls,objList: list):
        association = self.__class__.getClassAssociation()[cls]
        self.addLink(association[0],association[1],*objList)

    def addLink(self,selfCardinality: cardinalityType,objCardinality: cardinalityType,*obj):
        for inst in obj:
            if not self.verifyLink(selfCardinality,objCardinality,inst):
                return False
            id = None
            try:
                id = inst.getID()
            except:
                return False
            linkID = inst.getChildClass()
            
            #check if exist in link
            if id not in self.link_dict[linkID]:
                #check cardinality
                #ExactlyOne / ZeroOne
                if  objCardinality == cardinalityType.ZeroOne:
                    self.link_dict[linkID].clear()
                if  objCardinality == cardinalityType.ExactlyOne and\
                    len(self.link_dict[linkID]) == 1:
                    print(f"Error on {self} and {inst}")
                    print(f"Composite link cannot be changed")
                    return False
                self.link_dict[linkID].append(id)
                #recursive
                try:
                    if not inst.addLink(objCardinality,selfCardinality,self):
                        return False
                except:
                    print(f"Error on {inst} and {self}")
                    print(f"Object is not instance of {myClass.__name__}")
                    return False
        return True
                

    def verifyLink(self,selfCardinality: cardinalityType,objCardinality: cardinalityType,inst):
            #check if self link
            if isinstance(inst,self.getChildClass()):
                if not (type(inst) == self.getSelfLinkType() and\
                        type(self) == inst.getSelfLinkType()):
                    print(f"Error on {self} and {inst}")
                    print(f"Self Link is not allowed")
                    print(f"{self} allows {self.getSelfLinkType().__name__}")
                    print(f"{inst} allows {inst.getSelfLinkType().__name__}")
                    return False
            
            #check if allowed association
            classTuple = tuple(self.__class__.getClassAssociation().keys())
            if not isinstance(inst,classTuple):
                print(f"Error on {self} and {inst}")
                print(f"Not allowed association of {inst.__class__.__name__}")
                print(f"Allowed association")
                for i, cls in enumerate(self.__class__.getClassAssociation()):
                    print(f" {i+1})", cls.__name__)
                return False

            cardinality = (selfCardinality,objCardinality)
            #check if allowed cardinality
            if not self.__class__.getClassAssociation().get(inst.getChildClass()) == cardinality:
                print(f"Error on {self} and {inst}")
                print(f"Not allowed cardinality {cardinality}")
                print(f"Allowed association {self.__class__.getClassAssociation().get(inst.__class__)}")
                return False

            #check if id
            id = None
            try:
                id = inst.getID()
            except:
                print(f"Error on {self} and {inst}")
                print(f"Object is not inheritance of class {myClass.__name__}")
                return False

            #check if extent
            extent = None
            try:
                extent = inst.__class__.getClassExtent().getExtent()
            except:
                print(f"Error on {self} and {inst}")
                print(f"Failed to get class extent")
                return False
            
            #check if exist in extent
            if id not in extent:
                print(f"Error on {self} and {inst}")
                print(f"Object ID is not in the extent, {id}")
                return False
            
            return True

    def getLinkDict(self):
        return self.link_dict
    
    #for self link
    def getSelfLinkType(self):
        return None
    
    def getLink(self,cls):
        #check if allowed association
        if not self.__class__.getClassAssociation().get(cls):
            print(f"Error on {self} and {cls}")
            print(f"Association is not contained of {cls.__name__}")
            print(f"Allowed association")
            for i, cls in enumerate(self.__class__.getClassAssociation()):
                print(f" {i+1})", cls.__name__)
            return None
        return self.getLinkDict[cls]

    def setID(self):
        idPrefix = type(self).__name__+"-"
        assignID = idPrefix+idGenerator(8)
        extent = self.getChildExtent()
        while assignID in extent:
            assignID = idPrefix+idGenerator(8)
        self.__id = assignID

    def getID(self):
        return self.__id
    
    def getChildClass(self):
        return self.getChildExtentClass().getClass()
    
    def getChildExtentClass(self):
        return next(iter(self.inheritanceExtentClassList))
    
    def getChildExtent(self):
        return self.getChildExtentClass().getExtent()
    
    def addToChildExtent(self):
        self.getChildExtentClass().addInstance(self)

    def __str__(self):
        return f"{self.__class__.__name__.capitalize()}: {self.getID()}"


    def getDescription(self):
        out = f"{self.__class__.__name__.capitalize()}: {self.getID()}"
        link_dict = self.getLinkDict()
        for key in link_dict.keys():
            out += f"\n Association: {key.__name__}"
            if len(link_dict[key]) == 0:
                out += "\n  Link: Empty"
                continue
            for id in link_dict[key]:
                inst = key.getClassExtent().getInstance(id)
                out += f"\n  Link: {inst}"
        out += "\n"
        return out
    