class Sorting_List:
# # ___________________________________________________________________________________________________________________
#     def quickSort(alist):
#         Sorting_List.quicksortAlgorithm(alist, 0, len(alist) - 1)
#
#
#     def quicksortAlgorithm(myList, start, end):
#         if start < end:
#             # partition the list
#             pivot = Sorting_List.partition(myList, start, end)
#             # sort both halves
#             Sorting_List.quicksortAlgorithm(myList, start, pivot - 1)
#             Sorting_List.quicksortAlgorithm(myList, pivot + 1, end)
#         return myList
#
#     def partition(myList, start, end):
#         pivot = myList[start].getCIN()
#         left = start + 1
#         right = end
#         done = False
#         while not done:
#             while left <= right and myList[left].getCIN() <= pivot:
#                 left = left + 1
#             while myList[right].getCIN() >= pivot and right >= left:
#                 right = right - 1
#             if right < left:
#                 done = True
#             else:
#                 # swap places
#                 temp = myList[left]
#                 myList[left] = myList[right]
#                 myList[right] = temp
#         # swap start with myList[right]
#         temp = myList[start]
#         myList[start] = myList[right]
#         myList[right] = temp
#         return right

    def ins_sort(k):
        for i in range(1, len(k)):  # since we want to swap an item with previous one, we start from 1
            j = i  # bcoz reducing i directly will mess our for loop, so we reduce its copy j instead
            temp = k[j] # temp will be used for comparison with previous items, and sent to the place it belongs
            while j > 0 and temp.getCIN() < k[j - 1].getCIN():  # j>0 bcoz no point going till k[0] since there is no seat available on its left, for temp
                k[j] = k[j - 1]  # Move the bigger item 1 step right to make room for temp
                j = j - 1  # take k[j] all the way left to the place where it has a smaller/no value to its left.
            k[j] = temp
        return k