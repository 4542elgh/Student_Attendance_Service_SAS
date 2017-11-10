from Import_Export import Export_Abstract
import xml.etree.ElementTree as ET
import csv
import json

#inheret from super class Export_Abstract
class exportCSV(Export_Abstract.Export_Abstract):
    def exportToFile(self,path,StudentList): #inheret from parent class
        with open(path,"w",newline='') as csv_Output:
            writer = csv.writer(csv_Output)
            writer.writerow(["FirstName","LastName","CIN","FingerprintIndex"]) #first row of csv as attributes
            for subEntries in StudentList: #loop through 2d list and write row for each student entry
                writer.writerow([subEntries.getFirstName(),subEntries.getLastName(),subEntries.getCIN(),subEntries.getFingerprintIndex()])
    
class exportJSON(Export_Abstract.Export_Abstract):
    def exportToFile(self,path,StudentList): #inheret from parent class
        Alias = ["FirstName", "LastName", "CIN"]
        studentDictionary={} #initalize an empty 1D dict
        with open(path, 'w') as json_Output:
            for student in StudentList:
                studentDictionary[student.getCIN()]={} #initalize 2d dict for header ID aka element[0]
                studentDictionary[student.getCIN()]["FirstName"] = student.getFirstName()
                studentDictionary[student.getCIN()]["LastName"] = student.getLastName()
                studentDictionary[student.getCIN()]["CIN"] = student.getCIN()
                studentDictionary[student.getCIN()]["FingerprintIndex"] = student.getFingerprintIndex()
            json.dump(studentDictionary, json_Output)

class exportXML(Export_Abstract.Export_Abstract):
    def exportToFile(self,path,StudentList):
        doc=ET.Element("Data") #within doc you can have child as code below, put student id as this head
        for student in StudentList:
            temp = ET.SubElement(doc,"Student",SerialID=student.getCIN())
            ET.SubElement(temp, "FirstName").text = student.getFirstName()
            ET.SubElement(temp, "LastName").text = student.getLastName()
            ET.SubElement(temp, "CIN").text = student.getCIN()#add the attribute to tree
            ET.SubElement(temp, "FingerprintIndex").text = student.getFingerprintIndex()  # add the attribute to tree
        tree = ET.ElementTree(doc) #set your root to your file io
        tree.write(path,encoding="utf-8",xml_declaration=True) #this filename should contain classroom info and section number