class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        arr.sort()
        print(arr)
        for i in range(0,len(arr)-1):
            if arr[i] == arr[i+1]:
                duplicate = arr[i]
        nondupli = list(set(arr))
        print(nondupli)
        total = 0
        for i in range(1,n+1):    
            total += i
            print(total)
            missing = total - sum(nondupli)
        return duplicate, missing

# arr = [4, 3, 6, 2, 1, 1,5,7,8,9,10,11,12,13]
arr = [2,2]
n = len(arr)
obj = Solution()
print(obj.findTwoElement(arr,n))
