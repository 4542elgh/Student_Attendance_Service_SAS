class Student:
    def __init__(self,serial,firstName,lastName,cin):
        self.serial=serial;
        self.firstName=firstName
        self.lastName=lastName
        self.cin=cin
   
    def getSerial(self):
        return self.serial;
    
    def getFirstName(self):
        return self.firstName;
    
    def getLastName(self):
        return self.lastName;

    def getCIN(self):
        return self.cin

    def setSerial(self,serial):
        self.serial=serial

    def setFirstName(self,firstName):
        self.firstName=firstName

    def setLastName(self,lastName):
        self.lastName=lastName

    def setCIN(self,cin):
        self.cin=cin

    def toList(self):
        return [self.serial , self.firstName , self.lastName , self.cin]