from Import_Export import Export_File
from Import_Export import Import_File
from Add_Edit_Delete import ModifyEntry
from User_Interface import Display_Roster
from Student import Student
from Import_Export import Sorting_List
import time
import os
import csv
from Student import Student

class Main(): #do every entry in string, export will handle the datatype

    # temp = [Student.Student("1","Evan","Liu","304706199")]
    # Export_File.exportCSV.exportToFile(object,temp)
    #This is the method to use the import and export for 3 file types --------------------------------------------
    # temp={}
    # temp["Evan"]={}
    # temp["Evan"]["SerialID"]="id"
    # print(temp)
    # Export_File.exportCSV.exportToFile(object,[["1","Evan","Liu","922"],["3","Sherry","Liu","10284"],["1","Evan","Liu","1974"],["3","Sherry","Liu","1092"],["3","Sherry","Liu","4125"]])
    file_name="C:/Users/Huahuo/Desktop/roster.csv"
    studentList = [Student.Student("1", "ming", "liu", "304", "onTime")]
    file_path_prefix = file_name[0:file_name.rfind("/")]
    file_name = file_name[file_name.rfind("/") + 1:file_name.rfind(".")]


    path = file_path_prefix + "/Attendance_For_" + file_name + "/" + str(time.localtime()[1]) + "_" + str(time.localtime()[2]) + "_" + str(time.localtime()[0]) + "_attendance.csv"
    if not os.path.exists(file_path_prefix + "/Attendance_For_" + file_name):
        os.makedirs(file_path_prefix + "/Attendance_For_" + file_name)
        with open(path, "w", newline='') as csv_Output:
            writer = csv.writer(csv_Output)
            writer.writerow(["CIN", "FirstName", "LastName", "Attendance"])  # first row of csv as attributes
            for subEntries in studentList:  # loop through 2d list and write row for each student entry
                writer.writerow([subEntries.getCIN(), subEntries.getFirstName(), subEntries.getLastName(),
                                 subEntries.getAttendance()])
    else:
        with open(path, "w", newline='') as csv_Output:
            writer = csv.writer(csv_Output)
            writer.writerow(["CIN", "FirstName", "LastName", "Attendance"])  # first row of csv as attributes
            for subEntries in studentList:  # loop through 2d list and write row for each student entry
                writer.writerow([subEntries.getCIN(), subEntries.getFirstName(), subEntries.getLastName(),
                                 subEntries.getAttendance()])

    # print(len(xml2))
    # print(xml2[0].getFirstName())
    # print(xml2[1].getFirstName())
    # determine,xml3=ModifyEntry.Modify_Entry.Delete_Entry(object,xml2,"922")
    # print(len(xml3))
    # print(determine)
    # determine2, xml4 = ModifyEntry.Modify_Entry.Edit_Entry(object, xml3,"1","Juno","Zhang" ,"253")
    # print(xml4[0].getFirstName())
    # print(determine2)

    # print(xml[0].getCIN())
    # print(xml[1].getCIN())
    # for element in xml:
    #     print(element)


    # print(xml)
    # Export_File.exportCSV.exportToFile(object,[["1","Evan","Liu","30417199"],["3","Sherry","Liu","2039812411"]])
    # csv = Import_File.importCSV.toList(object)
    # print(type(csv))
    # for element in csv:
    #     print(element)
    # Export_File.exportJSON.exportToFile(object,[["1","Evan","Liu","30417199"], ["3","Sherry","Liu","2039812411"]])
    # json = Import_File.importJSON.toList(object)
    # print(type(json))
    # for element in json:
    #     print(element)
