# Recursion to print largest elements in a list

def largest(listis):
    if len(listis) == 1:
        return listis
    else:
        for i in listis:
            for j in listis:
                if i>i+1:
                    print(i)
                else:
                    print(j)
        # if listis[0] > (listis[1:]):
        #     return listis[0]
        # else:
        #     largest(largest(listis[:]))

# print(largest([1,2]))
li = [1,2,3,4,5]
larg = li[0]
end = 1
def large(lis,n):
    maxis = lis[0]
    for i in range(1, n):
        if lis[i]>maxis:
            maxis = lis[i]
        else:
            maxis = lis[0]
    return maxis


def lengthrecursively(lists):
    if len(lists) == 1:
        return lists[0]
    else:
        return 1 + lengthrecursively(lists[1:])

# print(lengthrecursively([1,2,3,4,5,5]))
def largestnumber(listelements):
    if len(listelements) == 1:
        return listelements[0]
    else:
        maxis = largestnumber(listelements[1:])
        if maxis > listelements[0]:
            return maxis
        else:
            return listelements[0]
print('large number is',largestnumber([10,2,12,4,8888,1,1,1,1,1,1,1,1,1,1,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,1000]))

# This below step is important which helps to traverse through list
# maxis = largestnumber(listelements[1:])