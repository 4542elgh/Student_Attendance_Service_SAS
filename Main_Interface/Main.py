from Import_Export import Export_File
from Import_Export import Import_File
from Add_Edit_Delete import ModifyEntry
from User_Interface import Display_Roster
from Student import Student
from Import_Export import Sorting_List
class Main(): #do every entry in string, export will handle the datatype

    Student1= Student.Student("1","Evan","Liu","922")
    Student2 = Student.Student("3","Sherry","Liu","10284")
    Student3 = Student.Student("1","Evan","Liu","1974")
    Student4 = Student.Student("3","Sherry","Liu","1092")
    Student5 = Student.Student("3","Sherry","Liu","4125")

    #This is the method to use the import and export for 3 file types --------------------------------------------

    # Export_File.exportCSV.exportToFile(object,[["1","Evan","Liu","922"],["3","Sherry","Liu","10284"],["1","Evan","Liu","1974"],["3","Sherry","Liu","1092"],["3","Sherry","Liu","4125"]])

    xml = [Student1,Student2,Student3,Student4,Student5]
    Sorting_List.Sorting_List.merge_Sort(xml)

    for element in xml:
        print(element.getCIN())

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
