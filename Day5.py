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
   

# print('smallest ',smallest)


def is_subset(lst1, lst2):
    twolist = lst1 + lst2
    for i in range(len(twolist)):
        print(lst1[i],lst2[i])
        # if  lst2[i] == lst1[i]:
        #     count +=1
        # print(count)
# print(is_subset([1,2],[3,4,1,2]))
def is_subset(lst1, lst2):
	twolist = lst1 + lst2
	lst1length = len(lst1)*2
	count = 0
	for i in ((twolist)):
		if twolist.count(i) > 1:
			count += 1
	if count == lst1length:
		return True
	else:
		return False
print(is_subset([1,2],[3,4,1,2]))
	

def is_subset1(lst1, lst2):
    print(set(lst1),set(lst2))
    return set(lst1) <= set(lst2)


# Adding index to list elements with respect to their index
def add_indexes(lst):
	newlist = []
	for i in range(len(lst)):
		adding_numbers = lst[i] + i
		newlist.append(adding_numbers)
	return newlist
		
	 
