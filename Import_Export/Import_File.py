from Import_Export import Import_Abstract
import xml.etree.ElementTree as ET
import csv
import json

class importXML(Import_Abstract.Import_Abstract):
    def toList(self):
        tree = ET.parse("../FileIO/Student_Roll_Sheet.xml")
        root = tree.getroot()
        xmlList=[]
        for childNode in root: #parent root this is each student's header
            # print(childNode.tag,childNode.text) #node.text will give the element value (the value in between <>xxx<> )
            for grandChildNode in childNode: #this is the attribute that specific student will have
                xmlList.append(grandChildNode.tag)
                xmlList.append(grandChildNode.text)
        return xmlList
        
class importCSV(Import_Abstract.Import_Abstract):
    def toList(self):
        csvList=[]
        with open("../FileIO/Student_Roll_Sheet.csv","r") as import_File:
            spamreader = csv.reader(import_File, delimiter=',', quotechar='|') #separate values by comma, and split them into a list
            for element in spamreader:
                csvList.append(element)
        return csvList

def json_recursion(obj): #this is a recursive method
    if isinstance(obj,dict): #check if this passed in object is a dictionary (json.load produce a dictionary)
        for item in obj.values(): #iterate through the json dictionary
            yield from json_recursion(item) #get generator values from json_recursion function (call that function and get its value)
    elif any(isinstance(obj, t) for t in (list,tuple)): #this is true if any of the obj element is list or tuple, T is generic object that can be either list or tuple
        for item in obj: #iterate through tuple or list
            yield from json_recursion(item) #get generator values from json_recursion function (call that function and get its value)
    else:
        yield obj #yield keyword is used as a generator -- where a value can be return, use and forget immediately, not storing in memeory and dont need to wait for entire calculation completion

class importJSON(Import_Abstract.Import_Abstract):
    def toList(self):
        jsonList = [] #defining datatype
        with open("../FileIO/Student_Roll_Sheet.json","r") as import_File:
            jsonData=json.load(import_File) # print(type(jsonData)) this return dict for object type
            for item in json_recursion(jsonData): # this loop will call json_recursion.next() each time the loop finishes (but this memory saving generator can be stopped at anytime rather than function with return that have to finish executing the entire loop)
                jsonList.append(item)
        return jsonList



