class Student:

    def __init__(self,serial,firstName,lastName,cin):
        setattr(self, "serial", serial)
        setattr(self, "firstName", firstName)
        setattr(self, "lastName", lastName)
        setattr(self, "cin", cin)

    def getSerial(self):
        return getattr(self,"serial")
    
    def getFirstName(self):
        return getattr(self,"firstName")
    
    def getLastName(self):
        return getattr(self,"lastName")

    def getCIN(self):
        return getattr(self,"cin")

    def setSerial(self,serialID):
        setattr(self,"serial",serialID)

    def setFirstName(self,firstName):
        setattr(self, "firstName", firstName)

    def setLastName(self,lastName):
        setattr(self, "lastName", lastName)

    def setCIN(self,cin):
        setattr(self, "cin", cin)

    def toList(self):
        return [self.serial , self.firstName , self.lastName , self.cin]

    def toDict(self):
        return {self.serial , self.firstName , self.lastName , self.cin}

