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
        while pointer1 < pointer2:
            sumis = nums[pointer1] + nums[pointer2]
            if sumis > target:
                pointer2 -= 1
            elif sumis < target:
                pointer1 +=1
            elif sumis == target:
                return True
        if True:
            result.append([pointer1,pointer2])
        print(result)
        return nums
obj = Solutionn()
print(obj.twoSum([3,2,4],6))
# print(obj.twoSum([2,7,11,15],9))