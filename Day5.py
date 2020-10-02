#find index of element if it is present else return -1
import sys
# def search(lst, item):
#     if item not in lst:
#         indexis = -1
#     else:
#         indexis = search(lst[0:],item)
#     return indexis






# print(search([1,23,4,5],23))

listis = [1,2,3,4,5]
position = 0
start_element = listis[0]
element_to_search = 5
# for element in range(len(listis)):
#     if listis[element] == element_to_search:
#         print(element)
    
# print('index of elemenet is',position)





newlist1 = [-11,9,1,2,3,18,0,-1]
newlist2 = [5,5,5]
newlist3 = [5]
n1 = len(newlist1)
smallest = newlist3[0]
# smallest = newlist2[0]
# smallest = newlist3[0]

for elements in range(1,len(newlist2)):
    if newlist2[elements] < smallest:
        # print('smallest are ',newlist1[elements])
        smallest = newlist2[elements]
        # print(smallest)
   

print('smallest ',smallest)