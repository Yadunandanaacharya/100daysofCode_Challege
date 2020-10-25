
def _sort(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            print(a[i],a[j])
            if a[i]>a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    print(a)
# pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) #, [2, 3, -2, 5, -8, 6, -2])

def _sort(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            print(a[i],a[j])
            if a[i]>a[j]:
                a[i],a[j] = a[j],a[i]
    print(a)


def pos_neg_sort(a):
    positive = [i for i in a if i>0]
    positive_index = [a.index(i) for i in positive]
    positive.sort()
    for i in range(0,len(positive)):
        (a[positive_index[i]]) = positive[i]
    print(a)
    # a[0] = positive[0]
    # a[1] = positive[1]
    # a[3] = positive[2]
    # a[5] = positive[3]

    # print(a)
pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) #, [2, 3, -2, 5, -8, 6, -2])


# SOlution of others.


# date formatting
def format_date(date):
		date = date.replace("/",'')
		date = date[4:8] + date[2:4] + date[0:2]
		return (date)

# Others solution:
def format_date(date):
	m, d, y = date.split('/')
	return ''.join((y, d, m))


def fact(n):
    factis = 1
    for i in range(1,n+1):
        factis = factis*i
    print(factis)
print(fact(5))


def longest_word(s):
	stringis = s.split(" ")
	maxlength = (max([len(i) for i in stringis]))
	for i in stringis:
		if len(i) == maxlength:
			return i
	#print( ([i for i in stringis if len(i)==maxlength]))
	

# Others solution
def longest_word(s):
	return max(s.split(), key=len)