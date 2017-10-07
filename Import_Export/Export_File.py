from Import_Export import Export_Abstract
import xml.etree.ElementTree as ET
import csv
from Student.Student import Student
import json

#inheret from super class Export_Abstract

class exportXML(Export_Abstract.Export_Abstract):
    def exportToFile(self,StudentList):
        doc=ET.Element("Data") #within doc you can have child as code below, put student id as this head

        Alias=["ID","FirstName","LastName","CIN"] #XML Tag alias
        counter=0 #getting the Serial ID since it is the first attribute in matrix list
        for element in StudentList:
            temp = ET.SubElement(doc,"Student",SerialID=StudentList[counter][0])
            innerCounter=0 #inner counter for all the other element except ID
            for subelement in element:
                # if innerCounter==0: #skip the ID attribute
                #     innerCounter += 1
                #     continue
                ET.SubElement(temp,Alias[innerCounter]).text=subelement #add the attribute to tree
                innerCounter+=1
            counter+=1

        tree = ET.ElementTree(doc) #set your root to your file io
        tree.write("../FileIO/Student_Roll_Sheet.xml",encoding="utf-8",xml_declaration=True) #this filename should contain classroom info and section number
        #this write method also generate xml head  
    
class exportCSV(Export_Abstract.Export_Abstract):
    def exportToFile(self,StudentList): #inheret from parent class
        with open("../FileIO/Student_Roll_Sheet.csv","w") as csv_Output:
            writer = csv.writer(csv_Output)
            writer.writerow(["SerialNumber","FirstName","LastName","CIN"]) #first row of csv as attributes
            for subEntries in StudentList: #loop through 2d list and write row for each student entry
                writer.writerow(subEntries)
    
class exportJSON(Export_Abstract.Export_Abstract):
    def exportToFile(self,StudentList): #inheret from parent class
        Alias = ["", "FirstName", "LastName", "CIN"]
        studentDictionary={} #initalize an empty 1D dict
        with open('../FileIO/Student_Roll_Sheet.json', 'w') as json_Output:
            for element in StudentList:
                studentDictionary[element[0]]={} #initalize 2d dict for header ID aka element[0]
                innerCounter=0 #keep track of Alias
                for subelement in element:
                    if innerCounter==0: #skip alias attribute
                        innerCounter += 1
                        continue
                    studentDictionary[element[0]][Alias[innerCounter]]=subelement #at 1D with attribute ID at 2D at attribute ALIAS set the value of 2D list
                    innerCounter+=1
            json.dump(studentDictionary, json_Output)
    