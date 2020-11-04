# https://leetcode.com/problems/3sum/discuss/919309/Detailed-Explanation-with-Steps-and-Code
# Solved with 2 pointer approach

class Solution:
    def threeSum(self, nums):
        ans = []
        nums = sorted(nums)
        print((nums))
        for i in range(len(nums)):
            # len(nums) length will start from 1
            if i > 0 and nums[i] == nums[i - 1]:
                # When two integers are equal, that time this condition
                # follows print like below, 1st and 2nd index elements are 
                # same
                # print('here i and i-1',i,i-1,nums[i],nums[i-1])

                continue
            low,high = i+1,len(nums)-1
            print('low and high beforr while.....',low,high)
# Simple when you sort an array 0th element will be lowest last element of 
# array is highest
# low = i+1 means index of them used them in further steps
            # print('low,high',low,high)#,i+1,len(nums)-1)
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                print('low and high after while....',low,high)
# here low won't be equal to 4 because above condtion is there
# if i>0 so loop starts from 1st index in 0th index -4 will be there after sorting
# low= i+1 so low=1 nums[low] = -1 at 1st index
                # print('for s',nums[i],nums[low], nums[high])

                # 1st condition increasing from low to high
                if i+1 < low < len(nums) -1 and nums[low] == nums[low-1]:
                    print('low and high inside if 1...',low,high)
                    # print('',i+1,low,len(nums)-1,nums[low],nums[low-1])
                    # low was 2 previously
                    low += 1
                    # print(low,nums[low])
                    continue
                # 2nd condition increasing from high to low
                if i+1 < high < len(nums) -1 and nums[high] == nums[high+1]:
                    # print('',i+1,high,len(nums)-1,nums[high],nums[high-1])
                    print('low and high inside if 2....',low,high)
                    high -= 1
                    # print(high,nums[high])
                    continue
                #  # 3rd condition checking whether sum is 0
                if  s == 0:
                    ans.append([nums[i],nums[low],nums[high]])
                    print('low and high inside if 3....',low,high)
                    low += 1
                    high -= 1
                    print('low and high inside if 4....',low,high)
                elif s > 0:
                    high = high - 1
                    print('low and high inside if 5...',low,high)
                else:
                    low += 1
                    print('low and high inside if 6...',low,high)
        return ans
#Moving from low to high on the other hand moving from high to low in if conditions

ob = Solution()
print(ob.threeSum([-1,0,1,2,-1,-4]))


#--------------------------------------------------Readable code:
class Solution:
    def threeSum(self, nums):
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low,high = i+1,len(nums)-1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if i+1 < low < len(nums) -1 and nums[low] == nums[low-1]:
                    low += 1
                    continue
                if i+1 < high < len(nums) -1 and nums[high] == nums[high+1]:
                    high -= 1
                    continue
                if  s == 0:
                    ans.append([nums[i],nums[low],nums[high]])
                    low += 1
                    high -= 1
                elif s > 0:
                    high = high - 1
                else:
                    low += 1
        return ans