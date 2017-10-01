from abc import ABCMeta,abstractmethod

class Import_Abstract():
    __metaclass__=ABCMeta
    
    @abstractmethod
    def toList(self):
        pass