# In this post a different solution is discussed.
# 1) We can compare the first digit and the last digit, then we repeat the process.
# 2) For the first digit, we need the order of the number. Say, 12321. Dividing this by 10000 would get us the leading 1. The trailing 1 can be retrieved by taking the mod with 10.
# 3 ) Now, to reduce this to 232.

# (12321 % 10000)/10 = (2321)/10 = 232 
# 4 ) And now, the 10000 would need to be reduced by a factor of 100.
# Here is the implementation of the above algorithm :

# Palindrome without converting to string
def palindrome(num):
    reveris = 0
    while num > 0:
        reveris =  reveris*10+(num%10)
        # print(reveris)
        num = num // 10
        # reveris = reveris + num%10
    print((reveris))

print(palindrome(-101))
# ################################
# ################################
# ################################
# Below solution passed all test cases of leetcode:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if    -(2**31) <= x < 0:
            return False
        elif x == 0:
            return True
        else:
            reverse = 0
            intis = x
            while 0 < x <= (2**31)-1:
                reverse = reverse*10 + x%10
                x = x//10
            if reverse == intis and reverse > 0:
                return True
            else:
                return False
        





# 123:
# 0 + 123%10  = 3
# 3*10 + 2 = 32
# 32*10 + 1 = 321

# Try to simplify problem like this.
# 121 = 120 + 1
# 12*10 + 1
# ((1*10)+2) + 1



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Anangram or not:
class Solution1:
    def isAnagram(self, s, t):
        print('Hai')    
# obj1  = Solution1()
# print(obj1.isAnagram('anagram','nagaram'))



# print(range(-(2**31),(2**31)-1))