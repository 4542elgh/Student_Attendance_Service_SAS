from Import_Export import Export_File
from Import_Export import Import_File

class Main(): #do every entry in string, export will handle the datatype


    #This is the method to use the import and export for 3 file types --------------------------------------------

    Export_File.exportCSV.exportToFile(object,[["1","Evan","Liu","922"],["3","Sherry","Liu","253"],["1","Evan","Liu","564"],["1","Evan","Liu","179"],["3","Sherry","Liu","270"],["1","Evan","Liu","385"]])
    xml = Import_File.importCSV.toList(object)
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
