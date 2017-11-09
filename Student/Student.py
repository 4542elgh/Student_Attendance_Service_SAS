class Student:

    def __init__(self,firstName,lastName,cin,fingerprintIndex=None,attendance=None):
        setattr(self, "firstName", firstName)
        setattr(self, "lastName", lastName)
        setattr(self, "cin", cin)

        if attendance is None:
            setattr(self,"fingerprintIndex", "-1")
        else:
            setattr(self, "attendance", fingerprintIndex)

        if attendance is None:
            setattr(self,"attendance", "Absent")
        else:
            setattr(self, "attendance", attendance)

    def getFingerprintIndex(self):
        return getattr(self,"fingerprintIndex")

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
        setattr(self, "attendance",attendance)

    def setFingerprintIndex(self, fingerprintIndex):
        setattr(self, "fingerprintIndex", fingerprintIndex)

    def toList(self):
        return [self.serial , self.firstName , self.lastName , self.cin]

    def toDict(self):
        return {self.serial , self.firstName , self.lastName , self.cin}

