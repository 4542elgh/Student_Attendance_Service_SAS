from abc import ABCMeta,abstractmethod

class Import_Abstract():
    __metaclass__=ABCMeta
    
    @abstractmethod
    def importParser(self):
        pass
    
    @abstractmethod
    def toList(self):
        pass