import math as mt 
  
# Functoin to count the number of ways  
# to choose the triples  
def countWays(arr, n):  
  
    # compute the max value in the array  
    # and create frequency array of size  
    # max_val + 1.  
    # We can also use HashMap to store  
    # frequencies. We have used an array  
    # to keep remaining code simple.  
    max_val = 0
    for i in range(n):  
        max_val = max(max_val, arr[i]) 
        
  
    freq = [0 for i in range(max_val + 1)]  
    # print(freq)
  
    for i in range(n):  
        freq[arr[i]] += 1
        # print(freq,i,freq[arr[i]])
    ans = 0 # stores the number of ways  
  
    # Case 1: 0, 0, 0  
    ans += (freq[0] * (freq[0] - 1) * 
           (freq[0] - 2) // 6) 
  
    # Case 2: 0, x, x  
    for i in range(1, max_val + 1):  
        ans += (freq[0] * freq[i] *
               (freq[i] - 1) // 2) 
  
    # Case 3: x, x, 2*x  
    for i in range(1, (max_val + 1) // 2):  
        ans += (freq[i] *
               (freq[i] - 1) // 2 * freq[2 * i])  
  
    # Case 4: x, y, x + y  
    # iterate through all pairs (x, y)  
    for i in range(1, max_val + 1):  
        for j in range(i + 1, max_val - i + 1):  
            ans += freq[i] * freq[j] * freq[i + j]  
  
    return ans  
  
# Driver code  
arr = [1,5,3,2] 
n = len(arr) 
# print(countWays(arr, n))  

class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        countis = 0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    # print(arr[i],arr[j],arr[k])
                    if (arr[i]-arr[j])<=a and (arr[j]-arr[k])<=b and (arr[i]-arr[k])<=c:
                        countis+=1
                    else:
                        countis=0
                   
        
                return countis
cl = Solution()
# print(cl.countGoodTriplets([1,1,2,2,3],0,0,1))
# ******************************************************************
# ******************************************************************
# ******************************************************************
# ******************************************************************
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
def findTriplets(arr):
    (arris) = []
    withou_dupli = set(arris)
    for i in range(0,len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k] == 0:
    # You can append multiple items to list at time with below code
                    arris.append([arr[i],arr[j],arr[k]])
    return (withou_dupli)
print(findTriplets([-1,0,1,2,-1,-4]))



