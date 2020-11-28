# Remove duplicates from an array.

#  You can do this by using set but that will be take extra space, that' why doing l
# like below
########################################
# As I understood main intention is to return length of sorted array after 
# removal of duplicates.
#######################################

###########################################
###########################################
###########################################
class Solution:
    def removeDuplicates(self, nums):
        j=0
        for i in range(0,len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[j] = nums[i]
                j+=1
        nums[j] = nums[len(nums)-1]
        
        # print(j)
        return j+1

arr = [1,1,2]
obj = Solution()
# print(obj.removeDuplicates(arr))
###########################################
###########################################
###########################################
def remove(arris):
    if len(arris) == 0:
        return 0
    j = 0
    for i in range(1,len(arris)):
        if arris[j] != arris[i]:
            j += 1
            arris[j] = arris[i]
    return j+1

obj = remove([1,2,2,3,4])
# print(obj)
############################################################
############################################################
############################################################

# [2,7,11,15], target = 9
mainarr = [2,7,11,15]
targetsum = 9

def sum2(arri,target):
    if len(arri) == 0:
        return 0
    maindict = {}
    for i,j in enumerate(arri):
        diff = target - j
        if diff not in maindict:
            maindict[j] = i
        # print('dict is',maindict)
        # print('diff is',diff)   
        if diff in maindict:
            result = [maindict[diff],i]
    return (result)


# onji = sum2(mainarr,targetsum)
# print(onji)

############################################################
############################################################
############################################################
# Reverse an integer: here you should not convert 
# integer to string

numis = 123
def revrsint(num):
    reverseis = 0
    while num != 0:
        reverseis = reverseis * 10 + (num % 10)
        num = num // 10
    return reverseis

# print(revrsint(numis))


############################################################
############################################################
number = 9
def equalornot(num):
    if num in range(0,11):
        return  num == 9
    else:
        print('No')

# print(equalornot(number))
# for i in range(-4,0):
#     print(i)


# ################################################
# ################################################
# ################################################
# check palindrome or not with simple many test cases
# Important overflow test case is also included
# -231 <= x <= 231 - 1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x in range(0,10):
            return True
        elif x in range(10,2**31):
            mainnum = x
            numis = x
            reverseis = 0
            while numis != 0:
                reverseis = reverseis * 10 + (numis % 10)
                numis = numis // 10
            return reverseis == mainnum
        elif x in range(-(2**31),0):
            return False
        
arr1 = [1,2,2,3,4]  #SHould return 4
# remove duplicate from sorted array and return length
def duplicatereturnlength(arr):
    if len(arr) == 0:
        return 0
    temp = []
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1]:
            print(arr[i],arr[i+1],i,i+1)

# print(duplicatereturnlength(arr1))

arr1 = [1,2,2,3,4]  #SHould return 4

def duplicate(arr):
    j = 0
    for i in range(0,len(arr)-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j+=1

    arr[j] = arr[len(arr)-1]
    return j+1
# print(duplicate(arr1))

