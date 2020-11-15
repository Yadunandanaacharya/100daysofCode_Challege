class Solution:
    def intersection(self, nums1, nums2):
        common = [i for i in nums1 if i in nums2]
        return (list(set(common)))
        

obj2 = Solution()
print(obj2.intersection([1,2,2,1],[2,2]))