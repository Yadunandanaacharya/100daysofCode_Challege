# considering number is greater than 0 
def fib(n):
    first = 1
    second = 2
    for i in range(n):
        if i<=2:
            i = n
        else:
            total = first+second
            first = second
            second = total
    return total
# print(fib(10))


def fact(n):
    factis = 1
    if n==0 and n==1:
        return 1
    else:
        for i in range(1,n+1):
            factis = factis * i
        return factis
# print(fact(5))

# Using above first method to create a  
# 2D array 
rows, cols = (5, 5) 
arr = [[0]*cols]*rows 
# print(arr) 

# Create 2 dim array
array_to_insert = ['*', '%', '$']
row = len(array_to_insert)
col = len(array_to_insert)
array = [[array_to_insert[0*3]  for i in range(3)]for j in range(3)]
# print(array)
# array_to_insert = ['*', '%', '$']
# main_array=[]
# for i in array_to_insert:
#     sub_array = []
#     for j in range(len(array_to_insert)):
#         sub_array.append()

array_to_insert = ['*', '%', '$']
# objectis = ''
enne = []
for i in range(len(array_to_insert)):
    sub = []
    for j in range(3):
        sub.append(array_to_insert[i])
    enne.append(sub)
        
# print(enne)
# My solution
def multiply(l):
	main_list = []
	for i in range(len(l)):
		sub_list = []
		for j in range(len(l)):
			sub_list.append(l[i])
		main_list.append(sub_list)
	return main_list
	

# Others solution
def multiple(n):
    length = len(n)
    return [[i]*length  for i in (n)]
print(multiple(['*', '%', '$']))


# Two Distinct Elements
def return_unique(lst):
	return [i for i in lst if lst.count(i)==1]
		

# def word_builder(ltr, pos):
# 	for i in range(0,len(ltr)):
# 		print(ltr[ltr.index(ltr[i])])

# print(word_builder(['g', 'e', 'o'],[1, 0, 2]))
dd = ['g', 'e', 'o']
pos = [1,0,2]
dd[pos[0]]  = dd['e']
print(dd)