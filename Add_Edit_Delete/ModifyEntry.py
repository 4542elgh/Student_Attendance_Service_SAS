from Add_Edit_Delete import ModifyEntry_Abstract
from Student import Student
from Import_Export import Sorting_List

class Modify_Entry(ModifyEntry_Abstract.ModifyEntry_Abstract):

    def Add_Entry(self,list,serial,firstName,lastName,cin):
        list.append(Student.Student(serial,firstName,lastName,cin))
        Sorting_List.Sorting_List.quickSort(list)
        return list

    def Get_Info(self,list,cin):
        for x in (0,len(list)-1):
            if list[x].getCIN()==cin:
                return True,list[x].getSerial(),list[x].getFirstName(),list[x].getLastName(),list[x].getCIN() # return True for found, and 4 attributes of students
        return False,list # did not find a corresponding CIN

    def Edit_Entry(self,list,serial,firstName,lastName,cin):
        for x in (0,len(list)-1):
            if list[x].getCIN()==cin:
                list[x].setSerial(serial)
                list[x].setFirstName(firstName)
                list[x].setLastName(lastName)
                return True, list
        return False,list

    def Delete_Entry(self,list,cin): #delete a file does not affect the sorting of the entire list, no need to sort again
        for x in (0,len(list)-1):
            if list[x].getCIN()==cin:
                del list[x]
                return True,list # sucessfully delete a CIN
        return False,list # did not find a corresponding CIN




