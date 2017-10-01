from Import_Export import Import_Abstract
import xml.etree.ElementTree as ET
import csv
import json

class importXML(Import_Abstract.Import_Abstract):
    def toList(self):
        tree = ET.parse("../FileIO/Student_Roll_Sheet.xml")
        root = tree.getroot()
        for childNode in root: #parent root this is each student's header
            print(childNode.tag,childNode.text) #node.text will give the element value (the value in between <>xxx<> )
            for grandChildNode in childNode: #this is the attribute that specific student will have
                print(grandChildNode.tag,grandChildNode.text)
        
        
class importCSV(Import_Abstract.Import_Abstract):
    def toList(self):
        with open("../FileIO/Student_Roll_Sheet.csv","r") as import_File:
            spamreader = csv.reader(import_File, delimiter=',', quotechar='|')
            for element in spamreader:
                print(element)


def recursive_iter(obj):
    if isinstance(obj, dict):
        for item in obj.values():
            yield from recursive_iter(item)
    elif any(isinstance(obj, t) for t in (list, tuple)):
        for item in obj:
            yield from recursive_iter(item)
    else:
        yield obj

class importJSON(Import_Abstract.Import_Abstract):



    def toList(self):
        with open("../FileIO/Student_Roll_Sheet.json","r") as import_File:
            jsonData=json.load(import_File)
            for item in recursive_iter(jsonData):
                print(item)


