class Sorting_List:
    def merge_Sort(studentList):
        if len(studentList) > 1:
            mid = len(studentList) // 2
            lefthalf = studentList[:mid]
            righthalf = studentList[mid:]

            Sorting_List.merge_Sort(lefthalf)
            Sorting_List.merge_Sort(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if int(lefthalf[i].getCIN()) < int(righthalf[j].getCIN()):
                    studentList[k] = lefthalf[i]
                    i = i + 1
                else:
                    studentList[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                studentList[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                studentList[k] = righthalf[j]
                j = j + 1
                k = k + 1