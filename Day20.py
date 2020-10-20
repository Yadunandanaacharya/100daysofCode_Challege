def matrix(x, y,z):
	return [[z for item in range(y)] for manylists in range(x)]


print(matrix(3, 4,0))
# Even though we are using list comprehension time complexity for above
# program is o(n^2)
