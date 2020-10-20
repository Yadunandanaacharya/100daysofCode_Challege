# Create a function that finds a target number in a list of prime numbers. 
# Implement a binary search algorithm in your function. The target number will 
# be from 2 through 97. If the target is prime then return "yes" else return "no".

# Solved above problem: Simple logic check whether num is in list if it is print "Yes"
# else "No"



# Write a program that returns a list of all the numbers from 1 to an integer argument. 
# But for multiples of three use “Fizz” instead of the number and for the multiples of 
# five use “Buzz”. For numbers which are multiples of both three and five use “FizzBuzz”.



def fizz_buzz(maximum):
	mulipleslist = []
	for i in range(maximum+1):
		if i%3 != 0 and i%5 != 0:
			mulipleslist.append(i)
		elif i%3 == 0 and i%5 ==0:
			mulipleslist.append(“FizzBuzz”)
		elif i%5 == 0:
			mulipleslist.append("Buzz")
		elif i%3 == 0:
			mulipleslist.append("Fizz")
	return mulipleslist
			
	