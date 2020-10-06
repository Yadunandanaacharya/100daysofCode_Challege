# STOP SOLVING EASY PROBLEMS START SOLVING MEDIUM PROBLEMS

def sum_of_evens(lst):
	even_elements = [j for i in lst  for j in i if j%2==0]
	print(sum(even_elements))
	
	
# print(sum_of_evens([
# 		[1, 5, 1, 3], 
# 		[4, 1, 2, 0], 
# 		[6, 9, 7, 4], 
# 		[5, 1, 2, 6]
# 	]))

class Calculator():
	# Write methods to add(), subtract(), multiply() and divide()
	def __init__(self,a,b):
		self.a = a
		self.b = b
		
	def add(self,c,d):
        self.a = c
        self.b = d
		print(self.a + self.b)
		return self.a + self.b
		
calculator = Calculator(2,3)
calculator.add(2,3)