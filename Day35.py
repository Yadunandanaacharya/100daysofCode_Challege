# Hastable for solving 2 sum problem in python

# Optimal Solution
# The two-sum problem can be solved in linear time as well. 
# To accomplish this, we must utilize hash-tables, which have constant (O(1)O(1)) lookup time.

# The algorithm is as follows:

# Initialize an empty hash table.
# For each element in the array:
# Calculate the complement by subtracting the current 
# list element from the given number.
# Look up the complement in the hash table. If it exists, 
# a pair that sums up to the given number has been found.
# Insert the current element of the array into the hash table 
# after you perform the step above.

def sum2(arr, target):
    resultdict = {}
    for i, n in enumerate(arr):
        diff = target -n
         
        
        if diff in resultdict:
            print([resultdict[diff],i])
        resultdict[n] = i   
print(sum2([2,7,11,10],9))