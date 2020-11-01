# Count uppercase through list comprehension
# count_uppercase(["SOLO", "hello", "Tea", "wHat"]) ➞ 6

# Example
# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 
  
# # Nested List Comprehension to flatten a given 2-D matrix 
# flatten_matrix = [val for sublist in matrix for val in sublist] 



def count_uppercase(lst):
	return (sum([letter.isupper() for word in lst for letter in word]))



# triplet sum
# ex:{1,5,3,2}
# ans=2
# 1+2 =3 and 2+3=5

def countriple(arr):
	countis = 0
	for i in range(0,len(arr)):
		for j in range(i):
			sumis = arr[i]+arr[j]
			if sumis in arr:
				countis+=1
	return countis

############################################################
# import time 
# begin = time.time() 

# # print(countriple([1,5,3,2]))
# #User function Template for python3
# class Solution:
# 	def countTriplet(self, arr, n):
# 		countis = 0
# 		for i in range(0,len(arr)):
# 			for j in range(i):
# 				sumis = arr[i]+arr[j]
# 				if sumis in arr:
# 					countis+=1
# 		return (countis)

# 	#User function Template for python3
# ob = Solution()
# ob.countTriplet([1,5,3,2],4)
# # print(ob.countTriplet([1,5,3,2],4))

# time.sleep(1) 
# end = time.time()  
# print(f"Total runtime of the program is {end - begin}") 
#################################################################

#######################################################
# Runtime Error:
# Runtime ErrorTime Limit Exceeded

# Your program took more time than expected.Time Limit Exceeded
# Expected Time Limit 2.80sec
# Hint : Please optimize your code and submit again.
# Error for above solution
# below I'm changing
#####################################################
# Still not optimized
# class Solution:
# 	def countTriplet(self, arr, n):
# 		result = [arr[i]+arr[j] for i in range(0,len(arr)) for  j in range(i) if arr[i]+arr[j] in arr]
# 		return len(result)
####################################################

import time 
begin = time.time() 

# class Solution:
# 	def countTriplet(self, arr, n):
# 		countis = 0
# 		for i in arr:
# 			first = i
# 			nextis = i+1
# 			sumis = first + nextis
# 			print(sumis)
# 			if sumis in arr:
# 				countis+=1
# 		return (countis)


# ob = Solution()
# # ob.countTriplet([4,3,2],3)
# time.sleep(1) 
# end = time.time()  
# print(f"Total runtime of the program is {end - begin}") 
# print(ob.countTriplet([12, 8, 2, 11, 5, 14, 10],7))



class Solution:
	def countTriplet(A, arr_size, sum):
		A.sort()
		for i in range(0, arr_size-2):
			l = i + 1
			r = arr_size-1
			while (l < r):
				if( A[i] + A[l] + A[r] == sum):
					print("Triplet is", A[i],', ', A[l], ', ', A[r]);
					return True
				elif (A[i] + A[l] + A[r] < sum):
					l += 1
				else: # A[i] + A[l] + A[r] > sum
					r -= 1
		return False
 
j = Solution()
print(j.countTriplet([12, 8, 2, 11, 5, 14, 10],7))