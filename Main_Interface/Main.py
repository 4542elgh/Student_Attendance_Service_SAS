from Import_Export import Import_File

class Main():
    json=Import_File.importJSON().toList()
    for element in json:
        print(element)