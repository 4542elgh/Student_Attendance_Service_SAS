class Student:
    def __init__(self,idNum,name,cin,enrolled,serialNumber,major,yearAttend):
        self.idNum=idNum;
        self.name=name;
        self.cin=cin;
        self.enrolled=enrolled;
        self.serialNumber=serialNumber;
        self.major=major;
        self.yearAttend=yearAttend;
   
    def getID(self):
        return self.idNum;
    
    def getName(self):
        return self.name;
    
    def getCIN(self):
        return self.cin;
    
    def getEnrolled(self):
        return self.enrolled;
    
    def getSerialNumber(self):
        return self.serialNumber;
    
    def getMajor(self):
        return self.major;
    
    def getYearAttend(self):
        return self.yearAttend;
    
    def setID(self,idNum):
        self.idNum=idNum;
    
    def setName(self,name):
        self.name=name;
    
    def setCIN(self,cin):
        self.cin=cin;
    
    def setEnrolled(self,enrolled):
        self.enrolled=enrolled;
    
    def setSerialNumber(self,serialNumber):
        self.serialNumber=serialNumber;
    
    def setMajor(self,major):
        self.major=major;
    
    def setYearAttend(self,year):
        self.yearAttend=year;
        
    def toList(self):
        return [self.idNum , self.name , self.cin , self.enrolled , self.serialNumber , self.major , self.yearAttend]