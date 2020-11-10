class Solution(object):
    def twoSum(self, nums, target):
        # nums.sort()
        result = []
        if len(nums)<2:
            return result 
        for i in range(len(nums)):
            for j in range(i):
                print(nums[i],nums[j])
                if nums[i] + nums[j] == target:
                    result.append([i,j])
        result[0].sort()
        return result[0]
# Above taking much time, time limit exceeded.

class Solutionn(object):
    def twoSum(self, nums, target):
        result = []
        pointer1 = 0
        pointer2 = len(nums)-1
        sumis = nums[pointer1] + nums[pointer2]
        while pointer1 < pointer2:
            
            if sumis == target:
                result.append([[pointer1],[pointer2]])
            elif sumis > target:
                pointer2 -= 1
            elif sumis < target:
                pointer1 +=1
        return result
obj = Solutionn()
# print(obj.twoSum([1,2,3],4)),
# print(obj.twoSum([2,7,,11,15],9))

# https://algodaily.com/lessons/using-the-two-pointer-technique



# oj = hashmap2sum()
# print(oj.sum2([2,8,3,1,0,11,7],9))

dictis= {'a':0,'b':2,'c':3}
dictis.update('a',3)
print(dictis)