class Student:

    def __init__(self,serial,firstName,lastName,cin,attendance=None):
        setattr(self, "serial", serial)
        setattr(self, "firstName", firstName)
        setattr(self, "lastName", lastName)
        setattr(self, "cin", cin)
        if attendance is None:
            setattr(self,"attendance", "Absent")
        else:
            setattr(self, "attendance", attendance)

    def getSerial(self):
        return getattr(self,"serial")
    
    def getFirstName(self):
        return getattr(self,"firstName")
    
    def getLastName(self):
        return getattr(self,"lastName")

    def getCIN(self):
        return getattr(self,"cin")

    def getAttendance(self):
        return getattr(self,"attendance")

    def setSerial(self,serialID):
        setattr(self,"serial",serialID)

    def setFirstName(self,firstName):
        setattr(self, "firstName", firstName)

    def setLastName(self,lastName):
        setattr(self, "lastName", lastName)

    def setCIN(self,cin):
        setattr(self, "cin", cin)

    def setAttendance(self,attendance):
        return getattr(self, "attendance",attendance)

    def toList(self):
        return [self.serial , self.firstName , self.lastName , self.cin]

    def toDict(self):
        return {self.serial , self.firstName , self.lastName , self.cin}

