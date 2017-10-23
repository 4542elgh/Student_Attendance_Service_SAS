class Sorting_List:
    # def quickSort(self,unorderList):
    #     Sorting_List.quickSortAlgorithm(self,unorderList,0,len(unorderList)-1)
    #
    # def quickSortAlgorithm(self,unorderList,first,last):
    #     if first<last:
    #         splitpoint = Sorting_List.partition(self,unorderList,first,last)
    #         Sorting_List.quickSortAlgorithm(self,unorderList,first,splitpoint-1)
    #         Sorting_List.quickSortAlgorithm(self,unorderList, splitpoint + 1, last)
    #
    # def partition(self,unorderList,first,last):
    #     pivotValue=unorderList[first].getCIN()
    #     leftMark = first+1
    #     rightMark=last
    #
    #     done = False
    #     while not done:
    #         while leftMark <=rightMark and unorderList[leftMark].getCIN()<=pivotValue:
    #             leftMark=leftMark+1
    #
    #         while unorderList[rightMark].getCIN()>=pivotValue and rightMark >=leftMark:
    #             rightMark=rightMark-1
    #         if rightMark < leftMark:
    #             done = True
    #         else:
    #             temp = unorderList[leftMark]
    #             unorderList[leftMark] = unorderList[rightMark]
    #             unorderList[rightMark] = temp
    #
    #         temp = unorderList[first]
    #         unorderList[first] = unorderList[rightMark]
    #         unorderList[rightMark] = temp
    #
    #         return rightMark
    # ___________________________________________________________________________________________________________________
    def quickSort(alist):
        Sorting_List.quicksortAlgorithm(alist, 0, len(alist) - 1)
    #
    # def quickSortHelper(alist, first, last):
    #     if first < last:
    #         splitpoint = Sorting_List.partition(alist, first, last)
    #
    #         Sorting_List.quickSortHelper(alist, first, splitpoint - 1)
    #         Sorting_List.quickSortHelper(alist, splitpoint + 1, last)
    #
    # def partition(alist, first, last):
    #     pivotvalue = alist[first].getCIN()
    #
    #     leftmark = first + 1
    #     rightmark = last
    #
    #     done = False
    #     while not done:
    #
    #         while leftmark <= rightmark and alist[leftmark].getCIN() <= pivotvalue:
    #             leftmark = leftmark + 1
    #
    #         while alist[rightmark].getCIN() >= pivotvalue and rightmark >= leftmark:
    #             rightmark = rightmark - 1
    #
    #         if rightmark < leftmark:
    #             done = True
    #         else:
    #             temp = alist[leftmark]
    #             alist[leftmark] = alist[rightmark]
    #             alist[rightmark] = temp
    #
    #     temp = alist[first]
    #     alist[first]= alist[rightmark]
    #     alist[rightmark] = temp
    #
    #     return rightmark

    def quicksortAlgorithm(myList, start, end):
        if start < end:
            # partition the list
            pivot = Sorting_List.partition(myList, start, end)
            # sort both halves
            Sorting_List.quicksortAlgorithm(myList, start, pivot - 1)
            Sorting_List.quicksortAlgorithm(myList, pivot + 1, end)
        return myList

    def partition(myList, start, end):
        pivot = myList[start].getCIN()
        left = start + 1
        right = end
        done = False
        while not done:
            while left <= right and myList[left].getCIN() <= pivot:
                left = left + 1
            while myList[right].getCIN() >= pivot and right >= left:
                right = right - 1
            if right < left:
                done = True
            else:
                # swap places
                temp = myList[left]
                myList[left] = myList[right]
                myList[right] = temp
        # swap start with myList[right]
        temp = myList[start]
        myList[start] = myList[right]
        myList[right] = temp
        return right