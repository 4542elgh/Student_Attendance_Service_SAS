from Import_Export import Export_Abstract
import xml.etree.ElementTree as ET
import csv
from Student.Student import Student
import json

#inheret from super class Export_Abstract

class exportXML(Export_Abstract.Export_Abstract):
    
    
    def exportToFile(self,idNum,stuName,cin,enrolled,serialNumber,major,yearAttend):    
        doc=ET.Element("Student") #within doc you can have child as code below, put student id as this head
        ET.SubElement(doc, "ID", name="ID").text = idNum
        ET.SubElement(doc, "Name", name="Name").text = stuName
        ET.SubElement(doc, "CIN", name="CIN").text = cin
        ET.SubElement(doc, "Enrolled", name="Enrolled").text = enrolled
        ET.SubElement(doc, "SerialNumber", name="SerialNumber").text = serialNumber
        ET.SubElement(doc, "Major", name="Major").text = major
        ET.SubElement(doc, "YearAttend", name="YearAttend").text = yearAttend
        
        tree = ET.ElementTree(doc) #set your root to your file io
        tree.write("../FileIO/xmlStudentExport.xml",encoding="utf-8",xml_declaration=True) #this filename should contain classroom info and section number
        #this write method also generate xml head  
    
class exportCSV(Export_Abstract.Export_Abstract):
    def exportToFile(self,idNum,stuName,cin,enrolled,serialNumber,major,yearAttend):
        with open("../FileIO/csvOutput.csv","w") as csv_Output:
            writer = csv.writer(csv_Output)
            Stu = Student(idNum,stuName,cin,enrolled,serialNumber,major,yearAttend)
            studentArg=Stu.toList()
            for i in studentArg:
                writer.writerow(i)
    
class exportJSON(Export_Abstract.Export_Abstract):
    def exportToFile(self,idNum,stuName,cin,enrolled,serialNumber,major,yearAttend):
        data={"ID":idNum,"Student Name":stuName,"CIN":cin,"Enrolled":enrolled,"Serial Number":serialNumber,"Major":major,"Year Attend":yearAttend}
        with open('../FileIO/student.json', 'w') as outfile:
            json.dump(data, outfile)
    