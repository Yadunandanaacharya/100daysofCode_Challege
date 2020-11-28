# Merge Two Sorted Linked Lists

# SImple linked list:
# class node:
#     def __init__(self,data = None):
#         self.data = data
#         self.next = None
    
# class linklist:
#     def __init__(self):
#         self.head = None
    
#     def printingelemnts(self):
#         printvalue = self.head
#         while printvalue is not None:
#             print(printvalue.data)
#             printvalue = printvalue.next

#     def add_to_head(self,new_element):
#         nodeis = node(new_element)
#         nodeis.next = self.head
#         self.head = nodeis
#         return nodeis
    
#     def add_to_end(self,new_node):
#         new_nodeis = node(new_node)
#         if self.head is None:
#             self.head = new_nodeis
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_nodeis 
# first_node = linklist()
# first_node.head = node(1)

# second_node = node(2)
# third_node = node(3)

# first_node.head.next = second_node
# second_node.next = third_node

# first_node.add_to_head(5)
# first_node.add_to_head(11)
# first_node.add_to_end(12)
########################################################
########################################################
########################################################
########################################################
# first_node.printingelemnts()

# merging two separate linked list nodes
class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class linklist:
    def __init__(self,head = None):
        self.head = None
    
    def printall(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    
class merging:
    def merging2linklist(self, first, second, newnode = None):
        merged_node = node(newnode)
        current1 = first.head
        current2 = second.head
firstlinklist1 = linklist()
firstlinklist1.head = node(1)

firstlinklist2 = node(2)
firstlinklist3 = node(4)

firstlinklist1.head.next = firstlinklist2
firstlinklist2.next = firstlinklist3

# firstlinklist1.printall()

############################################
secondlinklist1 = linklist()
secondlinklist1.head = node(1)

secondlinklist2 = node(3)
secondlinklist3 = node(4)

secondlinklist1.head.next = secondlinklist2
secondlinklist2.next = secondlinklist3

# secondlinklist1.printall()

mergeobj = merging()
mergeobj.merging2linklist(firstlinklist1,secondlinklist1,0)
