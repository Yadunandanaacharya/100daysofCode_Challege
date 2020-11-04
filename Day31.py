def sum_continu(arr,sumis):
    start = 0
    another_sum = 0
    for i in range(0,len(arr)):
        while another_sum>sumis and start<i-1:
            another_sum = another_sum - arr[start]
            start+=1
            
        if another_sum == sumis:
            print(start,i-1)
            return 1
        another_sum = another_sum + arr[i]
# print(sum_continu([1, 4, 20, 3, 10, 5,7,90,56,4],33))

def triple(arr):
    countis = 0
    for i in range(0,len(arr)):
        for j in range(i):
            sumis = arr[i]+arr[j]
            # print(sumis)
            if sumis in arr:
                countis+=1
    return countis
# print(triple([1,5,3,2]))


# *****************************
# class Solution:
#     def countTriplet(self,arr, n): 
#         arr.sort() 
#         i = n - 1
#         while(i >= 0): 
#             j = 0
#             k = i - 1
#             while (j < k): 
#                 if (arr[i] == arr[j] + arr[k]): 
#                     print( "numbers are ", arr[i], arr[j], arr[k]) 
#                     return
#                 elif (arr[i] > arr[j] + arr[k]): 
#                     j += 1
#                 else: 
#                     k -= 1
#             i -= 1
#         print("No such triplet exists")

# jj = Solution()
# print(jj.countTriplet([1,5,3,2],4))
# //////////////////////////////////////////
class Solution:
    def countTriplet(self,arr, n):
        freq = [0 for i in range(100)]
        for i in range(n):
            freq[arr[i]] += 1
            count = 0
            for i in range(n):
                for j in range(i + 1, n, 1):
                    if(freq[arr[i] + arr[j]]):
                        count += 1
        return count 
jjj = Solution()
# print(jjj.countTriplet([7, 34, 3, 9, 12, 52, 21, 23, 4] ,9))

# 2
# 5
# 1 2 3 5
# 10
# 1 2 3 4 5 6 7 8 10


def missing(arr,n):
    sumis = sum([i for i in range(1,n+1)])
    return sumis - sum(arr)
output = []
test = int(input('How many tests?'))
for i in range(test):
    array_size = int(input('Array sizze is'))
    arrays = [int(i) for i in input().split()]
    output.append(missing(arrays,array_size))
for i in output:
    print(i)
# print(missing([1,2 ,3, 5],5))