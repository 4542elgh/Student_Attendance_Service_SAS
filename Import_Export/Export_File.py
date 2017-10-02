from Import_Export import Export_Abstract
import xml.etree.ElementTree as ET
import csv
from Student.Student import Student
import json

#inheret from super class Export_Abstract

class exportXML(Export_Abstract.Export_Abstract):
    def exportToFile(self,serial,firstName,lastName,cin):
        doc=ET.Element("Student") #within doc you can have child as code below, put student id as this head
        ET.SubElement(doc, "SerialNumber", name="Serial").text = serial
        ET.SubElement(doc, "FirstName", name="FirstName").text = firstName
        ET.SubElement(doc, "LastName", name="LastName").text = lastName
        ET.SubElement(doc, "CIN", name="CIN").text = cin
        
        tree = ET.ElementTree(doc) #set your root to your file io
        tree.write("../FileIO/Student_Roll_Sheet.xml",encoding="utf-8",xml_declaration=True) #this filename should contain classroom info and section number
        #this write method also generate xml head  
    
class exportCSV(Export_Abstract.Export_Abstract):
    def exportToFile(self, serial, firstName, lastName, cin): #inheret from parent class
        with open("../FileIO/Student_Roll_Sheet.csv","w") as csv_Output:
            writer = csv.writer(csv_Output)
            Stu = Student(serial,firstName,lastName,cin)
            studentArg=Stu.toList()
            for i in studentArg:
                writer.writerow(i)
    
class exportJSON(Export_Abstract.Export_Abstract):
    def exportToFile(self, serial, firstName, lastName, cin): #inheret from parent class
        data={"Serial":serial,"FirstName":firstName,"LastName":lastName,"CIN":cin}
        with open('../FileIO/Student_Roll_Sheet.json', 'w') as json_Output:
            json.dump(data, json_Output)
    