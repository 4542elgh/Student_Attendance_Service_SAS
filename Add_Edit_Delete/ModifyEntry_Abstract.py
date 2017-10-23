from abc import ABCMeta, abstractmethod

class ModifyEntry_Abstract:
    @abstractmethod
    def Add_Entry(self):
        pass

    @abstractmethod
    def Edit_Entry(self):
        pass

    @abstractmethod
    def Delete_Entry(self):
        pass
