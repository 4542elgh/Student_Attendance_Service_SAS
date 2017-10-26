from Import_Export import Import_Abstract
import xml.etree.ElementTree as ET
import csv
import json
from Student import Student
from Import_Export import Sorting_List

class importCSV(Import_Abstract.Import_Abstract):
    def toList(self, file_name):
        csvList=[]
        with open(file_name,"r") as import_File:
            spamreader = csv.reader(import_File, delimiter=',', quotechar='|') #separate values by comma, and split them into a list
            counter=0
            for element in spamreader:
                if counter ==0:
                    counter+=1
                    continue
                else:
                    csvList.append(Student.Student(element[0], element[1], element[2], element[3]))
            # for element in csvList:
            #     print(element.getCIN())
            # Sorting_List.Sorting_List.ins_sort(csvList)
            # print("\n")
            # for element in csvList:
            #     print(element.getCIN())
            newlist=sorted(csvList,key=lambda x : x.getCIN(), reverse=True)
            return newlist

        # return csvList

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
    def toList(self, file_name):
        jsonList = [] #defining datatype
        with open(file_name,"r") as import_File:
            jsonData=json.load(import_File) # print(type(jsonData)) this return dict for object type
            temp=[]
            for item in json_recursion(jsonData): # this loop will call json_recursion.next() each time the loop finishes (but this memory saving generator can be stopped at anytime rather than function with return that have to finish executing the entire loop)
                temp.append(item)
                if len(temp)==4:
                    jsonList.append(Student.Student(temp[0],temp[1],temp[2],temp[3]))
                    temp=[]
            Sorting_List.Sorting_List.quickSort(jsonList)
            return jsonList


class importXML(Import_Abstract.Import_Abstract):
    def toList(self, file_name):
        tree = ET.parse(file_name)
        root = tree.getroot()
        xmlList=[]
        for childNode in root: #parent root this is each student's header
            xmlList.append(Student.Student(childNode[0].text, childNode[1].text, childNode[2].text, childNode[3].text))
            # print(childNode.tag,childNode.text) #node.text will give the element value (the value in between <>xxx<> )
            # temp=Student.Student()
            # for grandChildNode in childNode: #this is the attribute that specific student will have
            #     # xmlList.append(grandChildNode.tag)
            #     xmlList.append(grandChildNode.text)
        Sorting_List.Sorting_List.ins_sort(xmlList)
        return xmlList
