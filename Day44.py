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
            maindict[diff] = i
        result = [maindict[diff],i]
    print(result)


# print(sum2([mainarr],9))
arris = [1,288,3748,4,5]
for i,j in enumerate(arris):
    sumis = i + j
    print(sumis,i,j)