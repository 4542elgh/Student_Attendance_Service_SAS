from Import_Export import Import_Abstract
import xml.etree.ElementTree as ET

class importXML(Import_Abstract.Import_Abstract):
    def toList(self):
        tree = ET.parse("../FileIO/Student_Roll_Sheet.xml")
        root = tree.getroot()
        for childNode in root:
            print(childNode.tag,childNode.text)
            for grandChildNode in childNode:
                print(grandChildNode.tag,grandChildNode.text)
        
        
class importCSV(Import_Abstract.Import_Abstract):
    def toList(self):
        pass
        #implement object to list here

class importJSON(Import_Abstract.Import_Abstract):
    def toList(self):
        pass
        #implement object to list here